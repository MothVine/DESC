import numpy as np
from termcolor import colored
from desc.backend import jnp
from .derivative import QRJacobian
from .utils import (
    check_termination,
    OptimizeResult,
    evaluate_quadratic_form,
    print_header_nonlinear,
    print_iteration_nonlinear,
    status_messages,
)
from .tr_subproblems import (
    solve_trust_region_dogleg,
    solve_trust_region_2d_subspace,
    update_tr_radius,
)


def least_squares(
    fun,
    x0,
    grad,
    jac,
    init_jac=None,
    args=(),
    method="dogleg",
    x_scale=1,
    ftol=1e-6,
    xtol=1e-6,
    gtol=1e-6,
    verbose=1,
    maxiter=None,
    callback=None,
    options={},
):
    """Solve a least squares problem using a (quasi)-Newton trust region method

    Parameters
    ----------
    fun : callable
        objective to be minimized. Should have a signature like fun(x,*args)-> 1d array
    x0 : array-like
        initial guess
    grad : callable
        function to compute gradient, of 1/2fun**2. Should take the same arguments as fun
    jac : callable or 'broyden', optional:
        function to compute jacobian matrix of fun, or 'broyden' in which case the Broyden's
        method will be used to approximate the jacobian.
    init_jac : array-like, optional
        initial value for jacobian matrix, used if hess='broyden'
    args : tuple
        additional arguments passed to fun, grad, and jac
    method : 'dogleg' or 'subspace'
        method to use for trust region subproblem
    x_scale : array_like or 'hess', optional
        Characteristic scale of each variable. Setting `x_scale` is equivalent
        to reformulating the problem in scaled variables ``xs = x / x_scale``.
        An alternative view is that the size of a trust region along jth
        dimension is proportional to ``x_scale[j]``. Improved convergence may
        be achieved by setting `x_scale` such that a step of a given size
        along any of the scaled variables has a similar effect on the cost
        function. If set to 'jac', the scale is iteratively updated using the
        inverse norms of the columns of the jacobian matrix.
    ftol : float or None, optional
        Tolerance for termination by the change of the cost function. Default
        is 1e-8. The optimization process is stopped when ``dF < ftol * F``,
        and there was an adequate agreement between a local quadratic model and
        the true model in the last step. If None, the termination by this
        condition is disabled.
    xtol : float or None, optional
        Tolerance for termination by the change of the independent variables.
        Default is 1e-8. Optimization is stopped when
        ``norm(dx) < xtol * (xtol + norm(x))``. If None, the termination by
        this condition is disabled.
    gtol : float or None, optional
        Absolute tolerance for termination by the norm of the gradient. Default is 1e-8.
        Optimizer teriminates when ``norm(g) < gtol``, where
        If None, the termination by this condition is disabled.
    verbose : {0, 1, 2}, optional
        * 0 (default) : work silently.
        * 1 : display a termination report.
        * 2 : display progress during iterations
    maxiter : int, optional
        maximum number of iterations. Defaults to size(x)*100
    callback : callable, optional
        Called after each iteration. Should be a callable with
        the signature:

            ``callback(xk, OptimizeResult state) -> bool``

        where ``xk`` is the current parameter vector. and ``state``
        is an `OptimizeResult` object, with the same fields
        as the ones from the return. If callback returns True
        the algorithm execution is terminated.
    options : dict, optional
        dictionary of optional keyword arguments to override default solver settings.
        See the code for more details.

    Returns
    -------
    res : OptimizeResult
        The optimization result represented as a ``OptimizeResult`` object.
        Important attributes are: ``x`` the solution array, ``success`` a
        Boolean flag indicating if the optimizer exited successfully and
        ``message`` which describes the cause of the termination. See
        `OptimizeResult` for a description of other attributes.

    """

    nfev = 0
    ngev = 0
    njev = 0
    iteration = 0

    n = x0.size
    x = x0.copy()
    f = fun(x, *args)
    m = f.size
    nfev += 1
    g = grad(x, *args)
    ngev += 1

    if method == "dogleg":
        subproblem = solve_trust_region_dogleg
    elif method == "subspace":
        subproblem = solve_trust_region_2d_subspace
    else:
        raise ValueError(
            colored("method should be one of 'dogleg' or 'subspace'", "red")
        )

    cost = 0.5 * jnp.dot(f, f)

    if maxiter is None:
        maxiter = n * 100
    max_nfev = options.pop("max_nfev", maxiter)
    max_ngev = options.pop("max_ngev", max_nfev)
    max_njev = options.pop("max_njev", max_nfev)
    gnorm_ord = options.pop("gnorm_ord", np.inf)
    xnorm_ord = options.pop("xnorm_ord", 2)
    step_accept_threshold = options.pop("step_accept_threshold", 0.15)
    jac_recompute_freq = options.pop(
        "jac_recompute_interval", 1 if callable(jac) else 0
    )
    ga_fd_step = options.pop("ga_fd_step", 0.1)
    ga_accept_threshold = options.pop("ga_accept_threshold", 0)
    return_all = options.pop("return_all", False)
    return_tr = options.pop("return_tr", False)

    if np.size(jac_recompute_freq) == 1 and jac_recompute_freq > 0 and callable(jac):
        jac_recompute_iters = np.arange(1, maxiter, jac_recompute_freq)
    elif np.size(jac_recompute_freq) == 1 or not callable(jac):  # never recompute
        jac_recompute_iters = []
    else:
        jac_recompute_iters = jac_recompute_freq

    if jac == "broyden":
        if init_jac is None:
            init_jac = "auto"
        jac = QRJacobian(
            m,
            n,
            init_jac,
            jacfun=None,
            jacfun_args=(),
        )

    elif callable(jac):
        jac = QRJacobian(
            m,
            n,
            init_jac,
            jacfun=jac,
            jacfun_args=tuple(args),
        )
    else:
        raise ValueError(colored("jac should either be a callable or 'broyden'", "red"))

    jac_scale = isinstance(x_scale, str) and x_scale in ["jac", "auto"]
    if jac_scale:
        scale, scale_inv = jac.get_scale()
    else:
        scale, scale_inv = x_scale, 1 / x_scale

    # initial trust region radius
    g_norm = np.linalg.norm(g, ord=gnorm_ord)
    x_norm = np.linalg.norm(x, ord=xnorm_ord)
    trust_radius = options.pop("initial_trust_radius", np.linalg.norm(x * scale_inv))
    max_trust_radius = options.pop("max_trust_radius", trust_radius * 1000.0)
    min_trust_radius = options.pop("min_trust_radius", 0)
    tr_increase_threshold = options.pop("tr_increase_threshold", 0.75)
    tr_decrease_threshold = options.pop("tr_decrease_threshold", 0.25)
    tr_increase_ratio = options.pop("tr_increase_ratio", 2)
    tr_decrease_ratio = options.pop("tr_decrease_ratio", 0.25)

    if trust_radius == 0:
        trust_radius = 1.0
    if len(options) > 0:
        raise ValueError(
            colored("Unknown options: {}".format([key for key in options]), "red")
        )

    success = None
    step_norm = np.inf
    actual_reduction = np.inf
    ratio = 1  # ratio between actual reduction and predicted reduction
    dg_norm = np.inf

    if verbose > 1:
        print_header_nonlinear()

    if return_all:
        allx = [x]
    if return_tr:
        alltr = [trust_radius]

    alpha = 0.0  # "Levenberg-Marquardt" parameter

    while True:

        if iteration in jac_recompute_iters:
            jac.recompute(x)
            njev += 1
            if jac_scale:
                scale, scale_inv = jac.get_scale(scale_inv)

        success, message = check_termination(
            actual_reduction,
            cost,
            step_norm,
            x_norm,
            dg_norm,
            g_norm,
            ratio,
            ftol,
            xtol,
            gtol,
            iteration,
            maxiter,
            nfev,
            max_nfev,
            ngev,
            max_ngev,
            njev,
            max_njev,
        )
        if success is not None:
            result = OptimizeResult(
                x=x,
                success=success,
                cost=cost,
                fun=f,
                grad=g,
                jac=jac.get_matrix(),
                optimality=g_norm,
                nfev=nfev,
                ngev=ngev,
                njev=njev,
                nit=iteration,
                message=message,
            )
            break

        # Solve the sub-problem.
        # This gives us the proposed step relative to the current position
        # and it tells us whether the proposed step
        # has reached the trust region boundary or not.
        try:
            step_h, hits_boundary = subproblem(g, jac, scale, trust_radius, f)

        except np.linalg.linalg.LinAlgError:
            result = OptimizeResult(
                x=x,
                success=False,
                cost=cost,
                fun=f,
                grad=g,
                hess=jac.get_matrix(),
                optimality=g_norm,
                nfev=nfev,
                ngev=ngev,
                njev=njev,
                nit=iteration,
                message=status_messages["err"],
            )
            break

        # geodesic acceleration
        if ga_accept_threshold > 0:
            g0 = g
            g1 = grad(x + ga_fd_step * step_h * scale, *args)
            ngev += 1
            dg = (g1 - g0) / ga_fd_step ** 2
            ga_step_h = -scale_inv * jac.solve(dg) + 1 / ga_fd_step * step_h
            ga_ratio = np.linalg.norm(
                scale * ga_step_h, ord=xnorm_ord
            ) / np.linalg.norm(scale * step_h, ord=xnorm_ord)
            if ga_ratio < ga_accept_threshold:
                step_h += ga_step_h
        else:
            ga_ratio = -1
            ga_step_h = np.zeros_like(step_h)

        # calculate the predicted value at the proposed point
        predicted_reduction = cost - evaluate_quadratic_form(
            step_h, cost, g, jac, scale=scale
        )

        #         if predicted_reduction <= 0:
        #             result = OptimizeResult(x=x, success=False, fun=f, jac=g, hess=hess.get_matrix(),
        #                                     inv_hess=hess.get_inverse(), optimality=g_norm, nfev=nfev,
        #                                     ngev=ngev, nhev=nhev, nit=iteration, message=status_messages['approx'])
        #             break

        # calculate actual reduction and step norm
        step = scale * step_h
        step_norm = np.linalg.norm(step, ord=xnorm_ord)
        step_h_norm = np.linalg.norm(step_h, ord=xnorm_ord)
        x_new = x + step
        f_new = fun(x_new, *args)
        cost_new = 0.5 * np.dot(f_new, f_new)
        nfev += 1
        actual_reduction = cost - cost_new

        # update the trust radius according to the actual/predicted ratio
        trust_radius, ratio = update_tr_radius(
            trust_radius,
            actual_reduction,
            predicted_reduction,
            step_h_norm,
            hits_boundary,
            max_trust_radius,
            min_trust_radius,
            tr_increase_threshold,
            tr_increase_ratio,
            tr_decrease_threshold,
            tr_decrease_ratio,
            ga_ratio,
            ga_accept_threshold,
        )
        if return_tr:
            alltr.append(trust_radius)
        # if reduction was enough, accept the step
        if ratio > step_accept_threshold:
            x_old = x
            x = x_new
            f_old = f
            f = f_new
            cost = cost_new
            g_old = g
            g = grad(x, *args)
            ngev += 1
            dg = g - g_old
            dg_norm = np.linalg.norm(dg, ord=gnorm_ord)
            g_norm = np.linalg.norm(g, ord=gnorm_ord)
            x_norm = np.linalg.norm(x, ord=xnorm_ord)
            # don't update the hessian if we're going to recompute on the next iteration
            if iteration + 1 not in jac_recompute_iters:
                jac.update(x_new, x_old, f, f_old)

            if jac_scale:
                scale, scale_inv = jac.get_scale(scale_inv)
            if verbose > 1:
                print_iteration_nonlinear(
                    iteration, nfev, cost, actual_reduction, step_norm, g_norm
                )

            if callback is not None:
                stop = callback(np.copy(x), result)
                if stop:
                    result = OptimizeResult(
                        x=x,
                        success=None,
                        cost=cost,
                        fun=f,
                        grad=g,
                        jac=jac.get_matrix(),
                        optimality=g_norm,
                        nfev=nfev,
                        ngev=ngev,
                        njev=njev,
                        nit=iteration,
                        message=status_messages["callback"],
                    )
                    break

            if return_all:
                allx.append(x)

            iteration += 1

    if verbose > 0:
        if result["success"]:
            print(result["message"])
        else:
            print("Warning: " + result["message"])
        print("         Current function value: {:.3e}".format(result["cost"]))
        print("         Iterations: {:d}".format(result["nit"]))
        print("         Function evaluations: {:d}".format(result["nfev"]))
        print("         Gradient evaluations: {:d}".format(result["ngev"]))
        print("         Jacobian evaluations: {:d}".format(result["njev"]))

    if return_all:
        result["allvecs"] = allx
    if return_tr:
        result["alltr"] = alltr
    return result

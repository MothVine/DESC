import os
from matplotlib import rcParams, cycler
import matplotlib
import numpy as np
import re
from termcolor import colored

from desc.grid import Grid, LinearGrid
from desc.basis import FourierZernikeBasis, jacobi, fourier

__all__ = ["plot_1d", "plot_2d", "plot_3d", "plot_surfaces", "plot_section"]

colorblind_colors = [
    (0.0000, 0.4500, 0.7000),  # blue
    (0.8359, 0.3682, 0.0000),  # vermillion
    (0.0000, 0.6000, 0.5000),  # bluish green
    (0.9500, 0.9000, 0.2500),  # yellow
    (0.3500, 0.7000, 0.9000),  # sky blue
    (0.8000, 0.6000, 0.7000),  # reddish purple
    (0.9000, 0.6000, 0.0000),
]  # orange
dashes = [
    (1.0, 0.0, 0.0, 0.0, 0.0, 0.0),  # solid
    (3.7, 1.6, 0.0, 0.0, 0.0, 0.0),  # dashed
    (1.0, 1.6, 0.0, 0.0, 0.0, 0.0),  # dotted
    (6.4, 1.6, 1.0, 1.6, 0.0, 0.0),  # dot dash
    (3.0, 1.6, 1.0, 1.6, 1.0, 1.6),  # dot dot dash
    (6.0, 4.0, 0.0, 0.0, 0.0, 0.0),  # long dash
    (1.0, 1.6, 3.0, 1.6, 3.0, 1.6),
]  # dash dash dot
matplotlib.rcdefaults()
rcParams["font.family"] = "DejaVu Serif"
rcParams["mathtext.fontset"] = "cm"
rcParams["font.size"] = 10
rcParams["figure.facecolor"] = (1, 1, 1, 1)
rcParams["figure.figsize"] = (6, 4)
rcParams["figure.dpi"] = 141
rcParams["figure.autolayout"] = True
rcParams["axes.spines.top"] = False
rcParams["axes.spines.right"] = False
rcParams["axes.labelsize"] = "small"
rcParams["axes.titlesize"] = "medium"
rcParams["lines.linewidth"] = 1
rcParams["lines.solid_capstyle"] = "round"
rcParams["lines.dash_capstyle"] = "round"
rcParams["lines.dash_joinstyle"] = "round"
rcParams["xtick.labelsize"] = "x-small"
rcParams["ytick.labelsize"] = "x-small"
# rcParams['text.usetex'] = True
color_cycle = cycler(color=colorblind_colors)
dash_cycle = cycler(dashes=dashes)
rcParams["axes.prop_cycle"] = color_cycle

import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
from mpl_toolkits.mplot3d import Axes3D


_axis_labels_rtz = [r"$\rho$", r"$\theta$", r"$\zeta$"]
_axis_labels_RPZ = [r"$R ~(\mathrm{m})$", r"$\phi$", r"$Z ~(\mathrm{m})$"]
_axis_labels_XYZ = [r"$X ~(\mathrm{m})$", r"$Y ~(\mathrm{m})$", r"$Z ~(\mathrm{m})$"]


def _format_ax(ax, is3d=False, rows=1, cols=1, figsize=(6, 6)):
    """Check type of ax argument. If ax is not a matplotlib AxesSubplot, initalize one.

    Parameters
    ----------
    ax : None or matplotlib AxesSubplot instance
        axis to plot to
    is3d: bool
        default is False
    rows : int, optional
        number of rows of subplots to create
    cols : int, optional
        number of columns of subplots to create
    figsize : tuple of 2 floats
        figure size (width, height) in inches

    Returns
    -------
    fig : matplotlib.figure.Figure
        figure being plotted to
    ax : matplotlib.axes.Axes or ndarray of Axes
        axes being plotted to

    """
    if ax is None:
        if is3d:
            fig = plt.figure(figsize=figsize)
            ax = np.array(
                [
                    fig.add_subplot(
                        str(rows) + str(cols) + str(r * cols + c + 1), projection="3d"
                    )
                    for r in range(rows)
                    for c in range(cols)
                ]
            ).reshape((rows, cols))
            if ax.size == 1:
                ax = ax.flatten()[0]
            return fig, ax
        else:
            fig, ax = plt.subplots(rows, cols, figsize=figsize, squeeze=False)
            if ax.size == 1:
                ax = ax.flatten()[0]
            return fig, ax

    elif isinstance(ax, matplotlib.axes.Axes):
        return plt.gcf(), ax
    else:
        ax = np.atleast_1d(ax)
        if isinstance(ax.flatten()[0], matplotlib.axes.Axes):
            return plt.gcf(), ax
        else:
            raise TypeError(
                colored(
                    "ax agument must be None or an axis instance or array of axes",
                    "red",
                )
            )


def _get_grid(**kwargs):
    """Get grid for plotting.

    Parameters
    ----------
    kwargs
        any arguments taken by LinearGrid (Default L=1, M=1, N=1)

    Returns
    -------
    LinearGrid

    """
    grid_args = {
        "L": 1,
        "M": 1,
        "N": 1,
        "NFP": 1,
        "sym": False,
        "axis": True,
        "endpoint": True,
        "rho": None,
        "theta": None,
        "zeta": None,
    }
    for key in kwargs.keys():
        if key in grid_args.keys():
            grid_args[key] = kwargs[key]
    grid = LinearGrid(**grid_args)

    return grid


def _get_plot_axes(grid):
    """Find which axes are being plotted

    Parameters
    ----------
    grid : Grid

    Returns
    -------
    tuple

    """
    plot_axes = [0, 1, 2]
    if np.unique(grid.nodes[:, 0]).size == 1:
        plot_axes.remove(0)
    if np.unique(grid.nodes[:, 1]).size == 1:
        plot_axes.remove(1)
    if np.unique(grid.nodes[:, 2]).size == 1:
        plot_axes.remove(2)

    return tuple(plot_axes)


def plot_1d(eq, name, grid=None, ax=None, log=False, **kwargs):
    """Plots 1D profiles.

    Parameters
    ----------
    eq : Equilibrium
        object from which to plot
    name : str
        name of variable to plot
    grid : Grid, optional
        grid of coordinates to plot at
    ax : matplotlib AxesSubplot, optional
        axis to plot on
    log : bool, optional
        whether to use a log scale
    kwargs
        any arguments taken by LinearGrid

    Returns
    -------
    fig : matplotlib.figure.Figure
        figure being plotted to
    ax : matplotlib.axes.Axes or ndarray of Axes
        axes being plotted to

    """
    if grid is None:
        if kwargs == {}:
            kwargs.update({"L": 100, "NFP": eq.NFP})
        grid = _get_grid(**kwargs)
    plot_axes = _get_plot_axes(grid)
    if len(plot_axes) != 1:
        return ValueError(colored("Grid must be 1D", "red"))

    name_dict = _format_name(name)
    data = _compute(eq, name_dict, grid)
    fig, ax = _format_ax(ax)

    # reshape data to 1D
    data = data.flatten()

    if log:
        ax.semilogy(grid.nodes[:, plot_axes[0]], data)
    else:
        ax.plot(grid.nodes[:, plot_axes[0]], data)

    ax.set_xlabel(_axis_labels_rtz[plot_axes[0]])
    ax.set_ylabel(_name_label(name_dict))
    fig.set_tight_layout(True)
    return fig, ax


def plot_2d(eq, name, grid=None, ax=None, log=False, **kwargs):
    """Plots 2D cross-sections.

    Parameters
    ----------
    eq : Equilibrium
        object from which to plot
    name : str
        name of variable to plot
    grid : Grid, optional
        grid of coordinates to plot at
    ax : matplotlib AxesSubplot, optional
        axis to plot on
    log : bool, optional
        whether to use a log scale
    kwargs
        any arguments taken by LinearGrid

    Returns
    -------
    fig : matplotlib.figure.Figure
        figure being plotted to
    ax : matplotlib.axes.Axes or ndarray of Axes
        axes being plotted to

    """
    if grid is None:
        if kwargs == {}:
            kwargs.update({"L": 25, "M": 25, "NFP": eq.NFP})
        grid = _get_grid(**kwargs)
    plot_axes = _get_plot_axes(grid)
    if len(plot_axes) != 2:
        return ValueError(colored("Grid must be 2D", "red"))

    name_dict = _format_name(name)
    data = _compute(eq, name_dict, grid)
    fig, ax = _format_ax(ax)
    divider = make_axes_locatable(ax)

    # reshape data to 2D
    if 0 in plot_axes:
        if 1 in plot_axes:  # rho & theta
            data = data[:, :, 0]
        else:  # rho & zeta
            data = data[0, :, :].T
    else:  # theta & zeta
        data = data[:, 0, :].T

    imshow_kwargs = {
        "origin": "lower",
        "interpolation": "bilinear",
        "aspect": "auto",
    }
    if log:
        imshow_kwargs["norm"] = matplotlib.colors.LogNorm()
    imshow_kwargs["extent"] = [
        grid.nodes[0, plot_axes[1]],
        grid.nodes[-1, plot_axes[1]],
        grid.nodes[0, plot_axes[0]],
        grid.nodes[-1, plot_axes[0]],
    ]
    cax_kwargs = {"size": "5%", "pad": 0.05}

    im = ax.imshow(data.T, cmap="jet", **imshow_kwargs)
    cax = divider.append_axes("right", **cax_kwargs)
    cbar = fig.colorbar(im, cax=cax)
    cbar.update_ticks()

    ax.set_xlabel(_axis_labels_rtz[plot_axes[1]])
    ax.set_ylabel(_axis_labels_rtz[plot_axes[0]])
    ax.set_title(_name_label(name_dict))
    fig.set_tight_layout(True)
    return fig, ax


def plot_3d(eq, name, grid=None, ax=None, log=False, all_field_periods=True, **kwargs):
    """Plots 3D surfaces.

    Parameters
    ----------
    eq : Equilibrium
        object from which to plot
    name : str
        name of variable to plot
    grid : Grid, optional
        grid of coordinates to plot at
    ax : matplotlib AxesSubplot, optional
        axis to plot on
    log : bool, optional
        whether to use a log scale
    all_field_periods : bool, optional
        whether to plot full torus or just one field period
    kwargs
        any arguments taken by LinearGrid

    Returns
    -------
    fig : matplotlib.figure.Figure
        figure being plotted to
    ax : matplotlib.axes.Axes or ndarray of Axes
        axes being plotted to

    """
    nfp = 1 if all_field_periods else eq.NFP
    if grid is None:
        if kwargs == {}:
            kwargs.update({"M": 46, "N": 46, "NFP": nfp})
        grid = _get_grid(**kwargs)
    plot_axes = _get_plot_axes(grid)
    if len(plot_axes) != 2:
        return ValueError(colored("Grid must be 2D", "red"))

    name_dict = _format_name(name)
    data = _compute(eq, name_dict, grid)
    fig, ax = _format_ax(ax, is3d=True)

    coords = eq.compute_cartesian_coords(grid)
    X = coords["X"].reshape((grid.M, grid.L, grid.N), order="F")
    Y = coords["Y"].reshape((grid.M, grid.L, grid.N), order="F")
    Z = coords["Z"].reshape((grid.M, grid.L, grid.N), order="F")

    if 0 in plot_axes:
        if 1 in plot_axes:  # rho & theta
            data = data[:, :, 0]
            X = X[:, :, 0]
            Y = Y[:, :, 0]
            Z = Z[:, :, 0]
        else:  # rho & zeta
            data = data[0, :, :].T
            X = X[0, :, :].T
            Y = Y[0, :, :].T
            Z = Z[0, :, :].T
    else:  # theta & zeta
        data = data[:, 0, :].T
        X = X[:, 0, :].T
        Y = Y[:, 0, :].T
        Z = Z[:, 0, :].T

    minn, maxx = data.min().min(), data.max().max()
    if log:
        norm = matplotlib.colors.LogNorm(vmin=minn, vmax=maxx)
    else:
        norm = matplotlib.colors.Normalize(vmin=minn, vmax=maxx)
    m = plt.cm.ScalarMappable(cmap=plt.cm.jet, norm=norm)
    m.set_array([])

    ax.plot_surface(
        X,
        Y,
        Z,
        cmap="jet",
        facecolors=plt.cm.jet(norm(data)),
        vmin=minn,
        vmax=maxx,
        rstride=1,
        cstride=1,
    )
    fig.colorbar(m)

    ax.set_xlabel(_axis_labels_XYZ[0])
    ax.set_ylabel(_axis_labels_XYZ[1])
    ax.set_zlabel(_axis_labels_XYZ[2])
    ax.set_title(_name_label(name_dict))
    fig.set_tight_layout(True)

    # need this stuff to make all the axes equal, ax.axis('equal') doesnt work for 3d
    x_limits = ax.get_xlim3d()
    y_limits = ax.get_ylim3d()
    z_limits = ax.get_zlim3d()

    x_range = abs(x_limits[1] - x_limits[0])
    x_middle = np.mean(x_limits)
    y_range = abs(y_limits[1] - y_limits[0])
    y_middle = np.mean(y_limits)
    z_range = abs(z_limits[1] - z_limits[0])
    z_middle = np.mean(z_limits)

    # The plot bounding box is a sphere in the sense of the infinity
    # norm, hence I call half the max range the plot radius.
    plot_radius = 0.5 * max([x_range, y_range, z_range])

    ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
    ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
    ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])

    return fig, ax


def plot_section(eq, name, grid=None, ax=None, log=False, **kwargs):
    """Plots Poincare sections.

    Parameters
    ----------
    eq : Equilibrium
        object from which to plot
    name : str
        name of variable to plot
    grid : Grid, optional
        grid of coordinates to plot at
    ax : matplotlib AxesSubplot, optional
        axis to plot on
    log : bool, optional
        whether to use a log scale
    kwargs
        any arguments taken by LinearGrid

    Returns
    -------
    fig : matplotlib.figure.Figure
        figure being plotted to
    ax : matplotlib.axes.Axes or ndarray of Axes
        axes being plotted to

    """
    if grid is None:
        if eq.N == 0:
            N = 1
            nfp = 1
            rows = 1
            cols = 1
        else:
            N = 6
            nfp = eq.NFP
            rows = 2
            cols = 3
        if kwargs == {}:
            kwargs.update(
                {
                    "L": 50,
                    "NFP": nfp,
                    "axis": False,
                    "theta": np.linspace(0, 2 * np.pi, 91, endpoint=True),
                    "zeta": np.linspace(0, 2 * np.pi / nfp, N, endpoint=False),
                }
            )
        grid = _get_grid(**kwargs)
        zeta = np.unique(grid.nodes[:, 2])

    else:
        zeta = np.unique(grid.nodes[:, 2])
        N = zeta.size
        rows = np.floor(np.sqrt(N)).astype(int)
        cols = np.ceil(N / rows).astype(int)

    name_dict = _format_name(name)
    data = _compute(eq, name_dict, grid)
    figw = 5 * cols
    figh = 5 * rows
    fig, ax = _format_ax(ax, rows=rows, cols=cols, figsize=(figw, figh))
    ax = np.atleast_1d(ax).flatten()

    coords = eq.compute_toroidal_coords(grid)
    R = coords["R"].reshape((grid.M, grid.L, grid.N), order="F")
    Z = coords["Z"].reshape((grid.M, grid.L, grid.N), order="F")
    # TODO: plot multiple sections for stellarators

    imshow_kwargs = {}
    if log:
        norm = matplotlib.colors.LogNorm()
        levels = 100
        # levels=np.logspace(np.log10(data.min()), np.log10(data.max()),100)
    else:
        norm = matplotlib.colors.Normalize()
        levels = np.linspace(data.min(), data.max(), 100)

    cax_kwargs = {"size": "5%", "pad": 0.05}

    for i in range(N):
        divider = make_axes_locatable(ax[i])

        cntr = ax[i].contourf(
            R[:, :, i],
            Z[:, :, i],
            data[:, :, i],
            levels=levels,
            cmap="jet",
            norm=norm,
            **imshow_kwargs
        )
        cax = divider.append_axes("right", **cax_kwargs)
        cbar = fig.colorbar(cntr, cax=cax)
        cbar.update_ticks()

        ax[i].axis("equal")
        ax[i].set_xlabel(_axis_labels_RPZ[0])
        ax[i].set_ylabel(_axis_labels_RPZ[2])
        ax[i].set_title(
            _name_label(name_dict)
            + ", $\\zeta \\cdot NFP/2\\pi = {:.3f}$".format(nfp * zeta[i] / (2 * np.pi))
        )
    fig.set_tight_layout(True)
    return fig, ax


def plot_surfaces(eq, r_grid=None, t_grid=None, ax=None, **kwargs):
    """Plots flux surfaces.

    Parameters
    ----------
    eq : Equilibrium
        object from which to plot
    name : str
        name of variable to plot
    r_grid : Grid, optional
        grid of coordinates to plot rho contours at
    t_grid : Grid, optional
        grid of coordinates to plot theta coordinates at
    ax : matplotlib AxesSubplot, optional
        axis to plot on
    kwargs
        any arguments taken by LinearGrid

    Returns
    -------
    fig : matplotlib.figure.Figure
        figure being plotted to
    ax : matplotlib.axes.Axes or ndarray of Axes
        axes being plotted to

    """
    if r_grid is None and t_grid is None:
        if eq.N == 0:
            N = 1
            nfp = 1
            rows = 1
            cols = 1
        else:
            N = 6
            nfp = eq.NFP
            rows = 2
            cols = 3
        if kwargs == {}:
            kwargs.update(
                {
                    "L": 8,
                    "NFP": nfp,
                    "theta": np.linspace(0, 2 * np.pi, 180, endpoint=True),
                    "zeta": np.linspace(0, 2 * np.pi / nfp, N, endpoint=False),
                }
            )
        r_grid = _get_grid(**kwargs)
        zeta = np.unique(r_grid.nodes[:, 2])
        kwargs.update(
            {
                "L": 50,
                "NFP": nfp,
                "theta": np.linspace(0, 2 * np.pi, 9, endpoint=True),
                "zeta": zeta,
            }
        )
        t_grid = _get_grid(**kwargs)

    elif r_grid is None:
        zeta = np.unique(t_grid.nodes[:, 2])
        N = zeta.size
        if kwargs == {}:
            kwargs.update({"L": 8, "M": 180, "zeta": zeta})
        r_grid = _get_grid(**kwargs)
        rows = np.floor(np.sqrt(N)).astype(int)
        cols = np.ceil(N / rows).astype(int)

    elif t_grid is None:
        zeta = np.unique(r_grid.nodes[:, 2])
        N = zeta.size
        if kwargs == {}:
            kwargs.update({"L": 50, "M": 8, "zeta": zeta})
        r_grid = _get_grid(**kwargs)
        rows = np.floor(np.sqrt(zeta.size)).astype(int)
        cols = np.ceil(N / rows).astype(int)

    else:
        zeta = np.unique(r_grid.nodes[:, 2])
        t_zeta = np.unique(t_grid.nodes[:, 2])
        N = zeta.size
        rows = np.floor(np.sqrt(N)).astype(int)
        cols = np.ceil(N / rows).astype(int)
        if zeta.size != t_zeta.size or not np.allclose(zeta, t_zeta):
            raise ValueError(
                colored(
                    "r_grid and t_grid should have the same zeta planes, got r_grid={}, t_grid{}".format(
                        zeta, t_zeta
                    ),
                    "red",
                )
            )

    r_coords = eq.compute_toroidal_coords(r_grid)
    t_coords = eq.compute_toroidal_coords(t_grid)

    # theta coordinates cooresponding to linearly spaced vartheta angles
    v_nodes = t_grid.nodes
    v_nodes[:, 1] = t_grid.nodes[:, 1] - t_coords["lambda"]
    v_grid = Grid(v_nodes)
    v_coords = eq.compute_toroidal_coords(v_grid)

    # rho contours
    Rr = r_coords["R"].reshape((r_grid.M, r_grid.L, r_grid.N), order="F")
    Zr = r_coords["Z"].reshape((r_grid.M, r_grid.L, r_grid.N), order="F")

    # theta contours
    Rv = v_coords["R"].reshape((t_grid.M, t_grid.L, t_grid.N), order="F")
    Zv = v_coords["Z"].reshape((t_grid.M, t_grid.L, t_grid.N), order="F")

    figw = 4 * cols
    figh = 5 * rows
    fig, ax = _format_ax(ax, rows=rows, cols=cols, figsize=(figw, figh))
    ax = np.atleast_1d(ax).flatten()

    for i in range(N):
        ax[i].plot(
            Rv[:, :, i].T, Zv[:, :, i].T, color=colorblind_colors[2], linestyle=":"
        )
        ax[i].plot(Rr[:, :, i], Zr[:, :, i], color=colorblind_colors[0])
        ax[i].plot(Rr[:, -1, i], Zr[:, -1, i], color=colorblind_colors[1])
        ax[i].scatter(Rr[0, 0, i], Zr[0, 0, i], color=colorblind_colors[3])

        ax[i].axis("equal")
        ax[i].set_xlabel(_axis_labels_RPZ[0])
        ax[i].set_ylabel(_axis_labels_RPZ[2])
        ax[i].set_title(
            "$\\zeta \\cdot NFP/2\\pi = {:.3f}$".format(nfp * zeta[i] / (2 * np.pi))
        )

    fig.set_tight_layout(True)
    return fig, ax


def _compute(eq, name, grid):
    """Compute value specified by name on grid for equilibrium eq.

    Parameters
    ----------
    eq : Equilibrium
        object from which to plot
    name : str
        name of variable to plot
    grid : Grid
        grid of coordinates to calcuulate at

    Returns
    -------
    out, float array of shape (M, L, N)
        computed values

    """
    if not isinstance(name, dict):
        name_dict = _format_name(name)
    else:
        name_dict = name

    # primary calculations
    if name_dict["base"] in ["psi", "p", "iota"]:
        out = eq.compute_profiles(grid)[_name_key(name_dict)]
    elif name_dict["base"] in ["R", "Z", "lambda"]:
        out = eq.compute_toroidal_coords(grid)[_name_key(name_dict)]
    elif name_dict["base"] == "g":
        out = eq.compute_jacobian(grid)[_name_key(name_dict)]
    elif name_dict["base"] in ["B", "|B|"]:
        out = eq.compute_magnetic_field(grid)[_name_key(name_dict)]
    elif name_dict["base"] == "J":
        out = eq.compute_current_density(grid)[_name_key(name_dict)]
    elif name_dict["base"] in ["F", "|F|"]:
        out = eq.compute_force_error(grid)[_name_key(name_dict)]

    else:
        raise NotImplementedError(
            "No output for base named '{}'.".format(name_dict["base"])
        )

    # secondary calculations
    power = name_dict["power"]
    if power != "":
        try:
            power = float(power)
        except ValueError:
            # handle fractional exponents
            if "/" in power:
                frac = power.split("/")
                power = frac[0] / frac[1]
            else:
                raise ValueError(
                    "Could not convert string to float: '{}'".format(power)
                )
        out = out ** power

    return out.reshape((grid.M, grid.L, grid.N), order="F")


def _format_name(name):
    """Parse name string into dictionary.

    Parameters
    ----------
    name : str

    Returns
    -------
    parsed name : dict

    """
    name_dict = {
        "base": "",
        "sups": "",
        "subs": "",
        "power": "",
        "d": "",
        "units": "",
    }
    if "**" in name:
        parsename, power = name.split("**")
        if "_" in power or "^" in power:
            raise SyntaxError(
                "Power operands must come after components and derivatives."
            )
    else:
        power = ""
        parsename = name
    name_dict["power"] += power
    if "_" in parsename:
        split = parsename.split("_")
        if len(split) == 3:
            name_dict["base"] += split[0]
            name_dict["subs"] += split[1]
            name_dict["d"] += split[2]
        elif "^" in split[0]:
            name_dict["base"], name_dict["sups"] = split[0].split("^")
            name_dict["d"] = split[1]
        elif len(split) == 2:
            name_dict["base"], other = split
            if other in ["rho", "theta", "zeta"]:
                name_dict["subs"] = other
            else:
                name_dict["d"] = other
        else:
            raise SyntaxError("String format is not valid.")
    elif "^" in parsename:
        name_dict["base"], name_dict["sups"] = parsename.split("^")
    else:
        name_dict["base"] = parsename

    units = {
        "psi": r"(\mathrm{Webers})",
        "p": r"(\mathrm{Pa})",
        "iota": "",
        "R": r"(\mathrm{m})",
        "Z": r"(\mathrm{m})",
        "lambda": "",
        "g": r"(\mathrm{m}^3)",
        "B": r"(\mathrm{T})",
        "|B|": r"(\mathrm{T})",
        "J": r"(\mathrm{A}/\mathrm{m}^2)",
        "F": r"(\mathrm{N}/\mathrm{m}^3)",
        "|F|": r"(\mathrm{N})",
    }
    name_dict["units"] = units[name_dict["base"]]
    if name_dict["power"]:
        name_dict["units"] += "^" + name_dict["power"]

    return name_dict


def _name_label(name_dict):
    """Create label for name dictionary.

    Parameters
    ----------
    name_dict : dict
        name dictionary created by format_name method

    Returns
    -------
    label : str

    """
    esc = r"\\"[:-1]

    if "mag" in name_dict["base"]:
        base = "|" + re.sub("mag", "", name_dict["base"]) + "|"
    else:
        base = name_dict["base"]

    if "lambda" in base:
        idx = base.index("lambda")
        base = base[:idx] + "\\" + base[idx:]
    if "iota" in base:
        idx = base.index("iota")
        base = base[:idx] + "\\" + base[idx:]
    if "psi" in base:
        idx = base.index("psi")
        base = base[:idx] + "\\" + base[idx:]

    if name_dict["d"] != "":
        dstr0 = "d"
        dstr1 = "/d" + name_dict["d"]
        if name_dict["power"] != "":
            dstr0 = "(" + dstr0
            dstr1 = dstr1 + ")^{" + name_dict["power"] + "}"
        else:
            pass
    else:
        dstr0 = ""
        dstr1 = ""

    if name_dict["power"] != "":
        if name_dict["d"] != "":
            pstr = ""
        else:
            pstr = name_dict["power"]
    else:
        pstr = ""

    if name_dict["sups"] != "":
        supstr = "^{" + esc + name_dict["sups"] + " " + pstr + "}"
    elif pstr != "":
        supstr = "^{" + pstr + "}"
    else:
        supstr = ""

    if name_dict["subs"] != "":
        substr = "_{" + esc + name_dict["subs"] + "}"
    else:
        substr = ""
    label = (
        r"$" + dstr0 + base + supstr + substr + dstr1 + "~" + name_dict["units"] + "$"
    )
    return label


def _name_key(name_dict):
    """Reconstruct name for dictionary key used in Equilibrium compute methods.

    Parameters
    ----------
    name_dict : dict
        name dictionary created by format_name method

    Returns
    -------
    name_key : str

    """
    out = name_dict["base"]
    if name_dict["sups"] != "":
        out += "^" + name_dict["sups"]
    if name_dict["subs"] != "":
        out += "_" + name_dict["subs"]
    if name_dict["d"] != "":
        out += "_" + name_dict["d"]
    return out


def plot_logo(savepath=None, **kwargs):
    """Plots the DESC logo

    Parameters
    ----------
    savepath : str or path-like
        path to save the figure to.
        File format is inferred from the filename (Default value = None)
    **kwargs :
        additional plot formatting parameters.
        options include 'Dcolor', 'Dcolor_rho', 'Dcolor_theta',
        'Ecolor', 'Scolor', 'Ccolor', 'BGcolor', 'fig_width'


    Returns
    -------
    fig : matplotlib.figure.Figure
        handle to the figure used for plotting
    ax : matplotlib.axes.Axes
        handle to the axis used for plotting

    """

    eq = np.array(
        [
            [0, 0, 0, 3.62287349e00, 0.00000000e00],
            [1, -1, 0, 0.00000000e00, 1.52398053e00],
            [1, 1, 0, 8.59865670e-01, 0.00000000e00],
            [2, -2, 0, 0.00000000e00, 1.46374759e-01],
            [2, 0, 0, -4.33377700e-01, 0.00000000e00],
            [2, 2, 0, 6.09609205e-01, 0.00000000e00],
            [3, -3, 0, 0.00000000e00, 2.13664220e-01],
            [3, -1, 0, 0.00000000e00, 1.29776568e-01],
            [3, 1, 0, -1.67706961e-01, 0.00000000e00],
            [3, 3, 0, 2.32179123e-01, 0.00000000e00],
            [4, -4, 0, 0.00000000e00, 3.30174283e-02],
            [4, -2, 0, 0.00000000e00, -5.80394864e-02],
            [4, 0, 0, -3.10228782e-02, 0.00000000e00],
            [4, 2, 0, -2.43905484e-03, 0.00000000e00],
            [4, 4, 0, 1.81292185e-01, 0.00000000e00],
            [5, -5, 0, 0.00000000e00, 5.37223061e-02],
            [5, -3, 0, 0.00000000e00, 2.65199520e-03],
            [5, -1, 0, 0.00000000e00, 1.63010516e-02],
            [5, 1, 0, 2.73622502e-02, 0.00000000e00],
            [5, 3, 0, -3.62812195e-02, 0.00000000e00],
            [5, 5, 0, 7.88069456e-02, 0.00000000e00],
            [6, -6, 0, 0.00000000e00, 3.50372526e-03],
            [6, -4, 0, 0.00000000e00, -1.82814700e-02],
            [6, -2, 0, 0.00000000e00, -1.62703504e-02],
            [6, 0, 0, 9.37285472e-03, 0.00000000e00],
            [6, 2, 0, 3.32793660e-03, 0.00000000e00],
            [6, 4, 0, -9.90606341e-03, 0.00000000e00],
            [6, 6, 0, 6.00068129e-02, 0.00000000e00],
            [7, -7, 0, 0.00000000e00, 1.28853330e-02],
            [7, -5, 0, 0.00000000e00, -2.28268526e-03],
            [7, -3, 0, 0.00000000e00, -1.04698799e-02],
            [7, -1, 0, 0.00000000e00, -5.15951605e-03],
            [7, 1, 0, 2.29082701e-02, 0.00000000e00],
            [7, 3, 0, -1.19760934e-02, 0.00000000e00],
            [7, 5, 0, -1.43418200e-02, 0.00000000e00],
            [7, 7, 0, 2.27668988e-02, 0.00000000e00],
            [8, -8, 0, 0.00000000e00, -2.53055423e-03],
            [8, -6, 0, 0.00000000e00, -7.15955981e-03],
            [8, -4, 0, 0.00000000e00, -6.54397837e-03],
            [8, -2, 0, 0.00000000e00, -4.08366006e-03],
            [8, 0, 0, 1.17264567e-02, 0.00000000e00],
            [8, 2, 0, -1.24364476e-04, 0.00000000e00],
            [8, 4, 0, -8.59425384e-03, 0.00000000e00],
            [8, 6, 0, -7.11934473e-03, 0.00000000e00],
            [8, 8, 0, 1.68974668e-02, 0.00000000e00],
        ]
    )

    onlyD = kwargs.get("onlyD", False)
    Dcolor = kwargs.get("Dcolor", "xkcd:neon purple")
    Dcolor_rho = kwargs.get("Dcolor_rho", "xkcd:neon pink")
    Dcolor_theta = kwargs.get("Dcolor_theta", "xkcd:neon pink")
    Ecolor = kwargs.get("Ecolor", "deepskyblue")
    Scolor = kwargs.get("Scolor", "deepskyblue")
    Ccolor = kwargs.get("Ccolor", "deepskyblue")
    BGcolor = kwargs.get("BGcolor", "clear")
    fig_width = kwargs.get("fig_width", 3)
    fig_height = fig_width / 2
    contour_lw_ratio = kwargs.get("contour_lw_ratio", 0.3)
    lw = fig_width ** 0.5

    transparent = False
    if BGcolor == "dark":
        BGcolor = "xkcd:charcoal grey"
    elif BGcolor == "light":
        BGcolor = "white"
    elif BGcolor == "clear":
        BGcolor = "white"
        transparent = True

    if onlyD:
        fig_width = fig_width / 2
    fig = plt.figure(figsize=(fig_width, fig_height))
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    ax.axis("equal")
    ax.axis("off")
    ax.set_facecolor(BGcolor)
    fig.set_facecolor(BGcolor)
    if transparent:
        fig.patch.set_alpha(0)
        ax.patch.set_alpha(0)

    bottom = 0
    top = 10
    Dleft = 0
    Dw = 8
    Dh = top - bottom + 2
    DX = Dleft + Dw / 2
    DY = (top - bottom) / 2
    Dright = Dleft + Dw

    Eleft = Dright + 0.5
    Eright = Eleft + 4

    Soffset = 1
    Sleft = Eright + 0.5
    Sw = 5
    Sright = Sleft + Sw

    Ctheta = np.linspace(np.pi / 4, 2 * np.pi - np.pi / 4, 1000)
    Cleft = Sright + 0.75
    Cw = 4
    Ch = 11
    Cx0 = Cleft + Cw / 2
    Cy0 = (top - bottom) / 2

    # D
    cR = eq[:, 3]
    cZ = eq[:, 4]
    zern_idx = eq[:, :3]
    ls, ms, ns = zern_idx.T
    axis_jacobi = jacobi(0, ls, ms)
    R0 = axis_jacobi.dot(cR)
    Z0 = axis_jacobi.dot(cZ)

    nr = kwargs.get("nr", 5)
    nt = kwargs.get("nt", 8)
    Nr = 100
    Nt = 361
    rstep = Nr // nr
    tstep = Nt // nt
    r = np.linspace(0, 1, Nr)
    t = np.linspace(0, 2 * np.pi, Nt)
    r, t = np.meshgrid(r, t, indexing="ij")
    r = r.flatten()
    t = t.flatten()

    radial = jacobi(r, ls, ms)
    poloidal = fourier(t, ms)
    zern = radial * poloidal
    bdry = poloidal

    R = zern.dot(cR).reshape((Nr, Nt))
    Z = zern.dot(cZ).reshape((Nr, Nt))
    bdryR = bdry.dot(cR)
    bdryZ = bdry.dot(cZ)

    R = (R - R0) / (R.max() - R.min()) * Dw + DX
    Z = (Z - Z0) / (Z.max() - Z.min()) * Dh + DY
    bdryR = (bdryR - R0) / (bdryR.max() - bdryR.min()) * Dw + DX
    bdryZ = (bdryZ - Z0) / (bdryZ.max() - bdryZ.min()) * Dh + DY

    # plot r contours
    ax.plot(
        R.T[:, ::rstep],
        Z.T[:, ::rstep],
        color=Dcolor_rho,
        lw=lw * contour_lw_ratio,
        ls="-",
    )
    # plot theta contours
    ax.plot(
        R[:, ::tstep],
        Z[:, ::tstep],
        color=Dcolor_theta,
        lw=lw * contour_lw_ratio,
        ls="-",
    )
    ax.plot(bdryR, bdryZ, color=Dcolor, lw=lw)

    if onlyD:
        if savepath is not None:
            fig.savefig(savepath, facecolor=fig.get_facecolor(), edgecolor="none")

        return fig, ax

    # E
    ax.plot([Eleft, Eleft + 1], [bottom, top], lw=lw, color=Ecolor, linestyle="-")
    ax.plot([Eleft, Eright], [bottom, bottom], lw=lw, color=Ecolor, linestyle="-")
    ax.plot(
        [Eleft + 1 / 2, Eright],
        [bottom + (top + bottom) / 2, bottom + (top + bottom) / 2],
        lw=lw,
        color=Ecolor,
        linestyle="-",
    )
    ax.plot([Eleft + 1, Eright], [top, top], lw=lw, color=Ecolor, linestyle="-")

    # S
    Sy = np.linspace(bottom, top + Soffset, 1000)
    Sx = Sw * np.cos(Sy * 3 / 2 * np.pi / (Sy.max() - Sy.min()) - np.pi) ** 2 + Sleft
    ax.plot(Sx, Sy[::-1] - Soffset / 2, lw=lw, color=Scolor, linestyle="-")

    # C
    Cx = Cw / 2 * np.cos(Ctheta) + Cx0
    Cy = Ch / 2 * np.sin(Ctheta) + Cy0
    ax.plot(Cx, Cy, lw=lw, color=Ccolor, linestyle="-")

    if savepath is not None:
        fig.savefig(savepath, facecolor=fig.get_facecolor(), edgecolor="none")

    return fig, ax


def plot_zernike_basis(M, L, indexing, **kwargs):
    """Plots spectral basis of zernike basis functions

    Parameters
    ----------
    M : int
        maximum poloidal resolution
    L : int
        maximum difference between radial mode l and poloidal mode m
    indexing : str
        zernike indexing method. One of 'fringe', 'ansi', 'house', 'chevron'
    **kwargs :
        additional plot formatting arguments


    Returns
    -------
    fig : matplotlib.figure
        handle to figure
    ax : dict of matplotlib.axes
        nested dictionary, ax[l][m] is the handle to the
        axis for radial mode l, poloidal mode m

    """

    cmap = kwargs.get("cmap", "coolwarm")
    scale = kwargs.get("scale", 1)
    npts = kwargs.get("npts", 100)
    levels = kwargs.get("levels", np.linspace(-1, 1, npts))

    basis = FourierZernikeBasis(L=L, M=M, N=0, index=indexing)
    lmax = basis.L
    mmax = basis.M

    grid = LinearGrid(npts, npts, 0)
    r = np.linspace(0, 1, npts)
    v = np.linspace(0, 2 * np.pi, npts)
    rr, vv = np.meshgrid(r, v, indexing="ij")

    nodes = np.array([rr, vv, np.zeros_like(rr)]).T

    fig = plt.figure(figsize=(scale * mmax, scale * lmax / 2))

    ax = {i: {} for i in range(lmax + 1)}
    gs = matplotlib.gridspec.GridSpec(lmax + 1, 2 * (mmax + 1))

    Zs = basis.evaluate(nodes)

    for i, (l, m) in enumerate(zip(basis.modes[:, 0], basis.modes[:, 1])):
        Z = Zs[:, i].reshape((npts, npts))
        ax[l][m] = plt.subplot(gs[l, m + mmax : m + mmax + 2], projection="polar")
        ax[l][m].set_title("$\mathcal{Z}_{" + str(l) + "}^{" + str(m) + "}$")
        ax[l][m].axis("off")
        im = ax[l][m].contourf(v, r, Z, levels=levels, cmap=cmap)

    cb_ax = fig.add_axes([0.83, 0.1, 0.02, 0.8])
    plt.subplots_adjust(right=0.8)
    cbar = fig.colorbar(im, cax=cb_ax)
    cbar.set_ticks(np.linspace(-1, 1, 9))

    return fig, ax

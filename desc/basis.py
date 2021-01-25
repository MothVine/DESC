import numpy as np
from abc import ABC, abstractmethod
from scipy.special import factorial
from desc.utils import sign, flatten_list, equals
from desc.io import IOAble

__all__ = ["PowerSeries", "FourierSeries", "DoubleFourierSeries", "FourierZernikeBasis"]


class Basis(IOAble, ABC):
    """Basis is an abstract base class for spectral basis sets"""

    _io_attrs_ = ["_L", "_M", "_N", "_NFP", "_modes"]

    def __eq__(self, other) -> bool:
        """Overloads the == operator

        Parameters
        ----------
        other : Basis
            another Basis object to compare to

        Returns
        -------
        bool
            True if other is a Basis with the same attributes as self
            False otherwise

        """
        if self.__class__ != other.__class__:
            return False
        return equals(self.__dict__, other.__dict__)

    def _enforce_symmetry(self) -> None:
        """Enforces stellarator symmetry"""

        if self._sym in ["cos", "cosine"]:  # cos(m*t-n*z) symmetry
            non_sym_idx = np.where(sign(self._modes[:, 1]) != sign(self._modes[:, 2]))
            self._modes = np.delete(self._modes, non_sym_idx, axis=0)
        elif self._sym in ["sin", "sine"]:  # sin(m*t-n*z) symmetry
            non_sym_idx = np.where(sign(self._modes[:, 1]) == sign(self._modes[:, 2]))
            self._modes = np.delete(self._modes, non_sym_idx, axis=0)

    def _sort_modes(self) -> None:
        """Sorts modes for use with FFT"""

        sort_idx = np.lexsort((self._modes[:, 1], self._modes[:, 0], self._modes[:, 2]))
        self._modes = self._modes[sort_idx]

    @abstractmethod
    def _get_modes(self):
        """ndarray: the modes numbers for the basis"""

    @abstractmethod
    def evaluate(self, nodes, derivatives=np.array([0, 0, 0]), modes=None):
        """Evaluates basis functions at specified nodes

        Parameters
        ----------
        nodes : ndarray of float, size(num_nodes,3)
            node coordinates, in (rho,theta,zeta)
        derivatives : ndarray of int, shape(3,)
            order of derivatives to compute in (rho,theta,zeta)
        modes : ndarray of in, shape(num_modes,3), optional
            basis modes to evaluate (if None, full basis is used)

        Returns
        -------
        y : ndarray, shape(num_nodes,num_modes)
            basis functions evaluated at nodes

        """

    @abstractmethod
    def change_resolution(self) -> None:
        """Change resolution of the basis to the given resolutions"""

    @property
    def L(self) -> int:
        """ int: maximum radial resolution"""
        return self._L

    @property
    def M(self) -> int:
        """ int:  maximum poloidal resolution"""
        return self._M

    @property
    def N(self) -> int:
        """ int: maximum toroidal resolution"""
        return self._N

    @property
    def NFP(self) -> int:
        """ int: number of field periods"""
        return self._NFP

    @property
    def sym(self) -> str:
        """str: {'cos', 'sin', None} type of symmetry"""
        return self._sym

    @property
    def modes(self):
        """ndarray: mode numbers [l,m,n]"""
        return self._modes

    @modes.setter
    def modes(self, modes) -> None:
        self._modes = modes

    @property
    def num_modes(self) -> int:
        """int: number of modes in the spectral basis"""
        return self._modes.shape[0]


class PowerSeries(Basis):
    """1D basis set for flux surface quantities.

    Power series in the radial coordinate.


    Parameters
    ---------
    L : int
        maximum radial resolution

    """

    def __init__(
        self, L: int = 0, load_from=None, file_format=None, obj_lib=None
    ) -> None:

        self._file_format_ = file_format

        if load_from is None:
            self._L = L
            self._M = 0
            self._N = 0
            self._NFP = 1
            self._sym = None

            self._modes = self._get_modes(L=self._L)

            self._enforce_symmetry()
            self._sort_modes()

        else:
            self._init_from_file_(
                load_from=load_from, file_format=file_format, obj_lib=obj_lib
            )

    def _get_modes(self, L: int = 0):
        """Gets mode numbers for power series

        Parameters
        ----------
        L : int
            maximum radial resolution

        Returns
        -------
        modes : ndarray of int, shape(num_modes,3)
            array of mode numbers [l,m,n]
            each row is one basis function with modes (l,m,n)

        """
        l = np.arange(L + 1).reshape((-1, 1))
        z = np.zeros((L + 1, 2))
        return np.hstack([l, z])

    def evaluate(self, nodes, derivatives=np.array([0, 0, 0]), modes=None):
        """Evaluates basis functions at specified nodes

        Parameters
        ----------
        nodes : ndarray of float, size(num_nodes,3)
            node coordinates, in (rho,theta,zeta)
        derivatives : ndarray of int, shape(num_derivatives,3)
            order of derivatives to compute in (rho,theta,zeta)
        modes : ndarray of in, shape(num_modes,3), optional
            basis modes to evaluate (if None, full basis is used)

        Returns
        -------
        y : ndarray, shape(num_nodes,num_modes)
            basis functions evaluated at nodes

        """
        if modes is None:
            modes = self._modes

        return powers(nodes[:, 0], modes[:, 0], dr=derivatives[0])

    def change_resolution(self, L: int) -> None:
        """Change resolution of the basis to the given resolution.

        Parameters
        ----------
        L : int
            maximum radial resolution

        """
        if L != self._L:
            self._L = L
            self._modes = self._get_modes(self._L)
            self._sort_modes()


class FourierSeries(Basis):
    """1D basis set for use with the magnetic axis.
    Fourier series in the toroidal coordinate.

    Parameters
    ----------
    N : int
        maximum toroidal resolution
    NFP : int
        number of field periods
    sym : {'cos', 'sin', None}
        * 'cos' for cos(m*t-n*z) symmetry
        * 'sin' for sin(m*t-n*z) symmetry
        * None for no symmetry (Default)

    """

    def __init__(
        self,
        N: int = 0,
        NFP: int = 1,
        sym: str = None,
        load_from=None,
        file_format=None,
        obj_lib=None,
    ) -> None:

        self._file_format_ = file_format

        if load_from is None:
            self._L = 0
            self._M = 0
            self._N = N
            self._NFP = NFP
            self._sym = sym

            self._modes = self._get_modes(N=self._N)

            self._enforce_symmetry()
            self._sort_modes()

        else:
            self._init_from_file_(
                load_from=load_from, file_format=file_format, obj_lib=obj_lib
            )

    def _get_modes(self, N: int = 0) -> None:
        """Gets mode numbers for double fourier series

        Parameters
        ----------
        N : int
            maximum toroidal resolution

        Returns
        -------
        modes : ndarray of int, shape(num_modes,3)
            array of mode numbers [l,m,n]
            each row is one basis function with modes (l,m,n)

        """
        dim_tor = 2 * N + 1
        n = np.arange(dim_tor).reshape((-1, 1)) - N
        z = np.zeros((dim_tor, 2))
        return np.hstack([z, n])

    def evaluate(self, nodes, derivatives=np.array([0, 0, 0]), modes=None):
        """Evaluates basis functions at specified nodes

        Parameters
        ----------
        nodes : ndarray of float, size(num_nodes,3)
            node coordinates, in (rho,theta,zeta)
        derivatives : ndarray of int, shape(num_derivatives,3)
            order of derivatives to compute in (rho,theta,zeta)
        modes : ndarray of in, shape(num_modes,3), optional
            basis modes to evaluate (if None, full basis is used)

        Returns
        -------
        y : ndarray, shape(num_nodes,num_modes)
            basis functions evaluated at nodes

        """
        if modes is None:
            modes = self._modes

        return fourier(nodes[:, 2], modes[:, 2], NFP=self._NFP, dt=derivatives[2])

    def change_resolution(self, N: int) -> None:
        """Change resolution of the basis to the given resolutions.

        Parameters
        ----------
        N : int
            maximum toroidal resolution

        """
        if N != self._N:
            self._N = N
            self._modes = self._get_modes(self._N)
            self._sort_modes()


class DoubleFourierSeries(Basis):
    """2D basis set for use on a single flux surface.
    Fourier series in both the poloidal and toroidal coordinates.

    Parameters
    ----------
    M : int
        maximum poloidal resolution
    N : int
        maximum toroidal resolution
    NFP : int
        number of field periods
    sym : {'cos', 'sin', None}
        * 'cos' for cos(m*t-n*z) symmetry
        * 'sin' for sin(m*t-n*z) symmetry
        * None for no symmetry (Default)

    """

    def __init__(
        self,
        M: int = 0,
        N: int = 0,
        NFP: int = 1,
        sym: str = None,
        load_from=None,
        file_format=None,
        obj_lib=None,
    ) -> None:

        self._file_format_ = file_format

        if load_from is None:
            self._L = 0
            self._M = M
            self._N = N
            self._NFP = NFP
            self._sym = sym

            self._modes = self._get_modes(M=self._M, N=self._N)

            self._enforce_symmetry()
            self._sort_modes()

        else:
            self._init_from_file_(
                load_from=load_from, file_format=file_format, obj_lib=obj_lib
            )

    def _get_modes(self, M: int = 0, N: int = 0) -> None:
        """Gets mode numbers for double fourier series

        Parameters
        ----------
        M : int
            maximum poloidal resolution
        N : int
            maximum toroidal resolution

        Returns
        -------
        modes : ndarray of int, shape(num_modes,3)
            array of mode numbers [l,m,n]
            each row is one basis function with modes (l,m,n)

        """
        dim_pol = 2 * M + 1
        dim_tor = 2 * N + 1
        m = np.arange(dim_pol) - M
        n = np.arange(dim_tor) - N
        mm, nn = np.meshgrid(m, n)
        mm = mm.reshape((-1, 1), order="F")
        nn = nn.reshape((-1, 1), order="F")
        z = np.zeros_like(mm)
        y = np.hstack([z, mm, nn])
        return y

    def evaluate(self, nodes, derivatives=np.array([0, 0, 0]), modes=None):
        """Evaluates basis functions at specified nodes

        Parameters
        ----------
        nodes : ndarray of float, size(num_nodes,3)
            node coordinates, in (rho,theta,zeta)
        derivatives : ndarray of int, shape(num_derivatives,3)
            order of derivatives to compute in (rho,theta,zeta)
        modes : ndarray of in, shape(num_modes,3), optional
            basis modes to evaluate (if None, full basis is used)

        Returns
        -------
        y : ndarray, shape(num_nodes,num_modes)
            basis functions evaluated at nodes

        """
        if modes is None:
            modes = self._modes

        poloidal = fourier(nodes[:, 1], modes[:, 1], dt=derivatives[1])
        toroidal = fourier(nodes[:, 2], modes[:, 2], NFP=self._NFP, dt=derivatives[2])
        return poloidal * toroidal

    def change_resolution(self, M: int, N: int) -> None:
        """Change resolution of the basis to the given resolutions.

        Parameters
        ----------
        M : int
            maximum poloidal resolution
        N : int
            maximum toroidal resolution

        Returns
        -------
        None

        """
        if M != self._M or N != self._N:
            self._M = M
            self._N = N
            self._modes = self._get_modes(self._M, self._N)
            self._sort_modes()


class FourierZernikeBasis(Basis):
    """3D basis set for analytic functions in a toroidal volume.
    Zernike polynomials in the radial & poloidal coordinates, and a Fourier
    series in the toroidal coordinate.

    Initializes a FourierZernikeBasis

    Parameters
    ----------
    L : int
        maximum radial resolution
    M : int
        maximum poloidal resolution
    N : int
        maximum toroidal resolution
    NFP : int
        number of field periods
    sym : {'cos', 'sin', None}
        * 'cos' for cos(m*t-n*z) symmetry
        * 'sin' for sin(m*t-n*z) symmetry
        * None for no symmetry (Default)
    index : {'ansi', 'frige', 'chevron', 'house'}
        Indexing method, default value = 'ansi'

        For L=0, all methods are equivalent and give a "chevron" shaped
        basis (only the outer edge of the zernike pyramid of width M).
        For L>0, the indexing scheme defines order of the basis functions:

        ``'ansi'``: ANSI indexing fills in the pyramid with triangles of
        decreasing size, ending in a triagle shape. The maximum L is M,
        at which point the traditional ANSI indexing is recovered.
        Gives a single mode at m=M, and multiple modes at l=L, from m=0 to m=l.
        Total number of modes = (M-(L//2)+1)*((L//2)+1)

        ``'fringe'``: Fringe indexing fills in the pyramid with chevrons of
        decreasing size, ending in a diamond shape. The maximum L is 2*M,
        for which the traditional fringe/U of Arizona indexing is recovered.
        Gives a single mode at m=M and a single mode at l=L and m=0.
        Total number of modes = (M+1)*(M+2)/2 - (M-L//2+1)*(M-L//2)/2

        ``'chevron'``: Beginning from the initial chevron of width M,
        increasing L adds additional chevrons of the same width.
        Similar to "house" but with fewer modes with high l and low m.
        Total number of modes = (M+1)*(2*(L//2)+1)

        ``'house'``: Fills in the pyramid row by row, with a maximum
        horizontal width of M and a maximum radial resolution of L.
        For L=M, it is equivalent to ANSI, while for L>M it takes on a
        "house" like shape. Gives multiple modes at m=M and l=L.


    """

    def __init__(
        self,
        L: int = -1,
        M: int = 0,
        N: int = 0,
        NFP: int = 1,
        sym: str = None,
        index: str = "ansi",
        load_from=None,
        file_format=None,
        obj_lib=None,
    ) -> None:

        self._file_format_ = file_format

        if load_from is None:
            self._L = L
            self._M = M
            self._N = N
            self._NFP = NFP
            self._sym = sym
            self._index = index

            self._modes = self._get_modes(
                L=self._L, M=self._M, N=self._N, index=self._index
            )

            self._enforce_symmetry()
            self._sort_modes()

        else:
            self._init_from_file_(
                load_from=load_from, file_format=file_format, obj_lib=obj_lib
            )

    def _get_modes(self, L: int = -1, M: int = 0, N: int = 0, index: str = "ansi"):
        """Gets mode numbers for Fourier-Zernike basis functions

        Parameters
        ----------
        L : int
            maximum radial resolution
        M : int
            maximum poloidal resolution
        N : int
            maximum toroidal resolution
        index : {'ansi', 'frige', 'chevron', 'house'}
            Indexing method, default value = 'ansi'

            For L=0, all methods are equivalent and give a "chevron" shaped
            basis (only the outer edge of the zernike pyramid of width M).
            For L>0, the indexing scheme defines order of the basis functions:

            ``'ansi'``: ANSI indexing fills in the pyramid with triangles of
            decreasing size, ending in a triagle shape. The maximum L is M,
            at which point the traditional ANSI indexing is recovered.
            Gives a single mode at m=M, and multiple modes at l=L, from m=0 to m=l.
            Total number of modes = (M-(L//2)+1)*((L//2)+1)

            ``'fringe'``: Fringe indexing fills in the pyramid with chevrons of
            decreasing size, ending in a diamond shape. The maximum L is 2*M,
            for which the traditional fringe/U of Arizona indexing is recovered.
            Gives a single mode at m=M and a single mode at l=L and m=0.
            Total number of modes = (M+1)*(M+2)/2 - (M-L//2+1)*(M-L//2)/2

            ``'chevron'``: Beginning from the initial chevron of width M,
            increasing L adds additional chevrons of the same width.
            Similar to "house" but with fewer modes with high l and low m.
            Total number of modes = (M+1)*(2*(L//2)+1)

            ``'house'``: Fills in the pyramid row by row, with a maximum
            horizontal width of M and a maximum radial resolution of L.
            For L=M, it is equivalent to ANSI, while for L>M it takes on a
            "house" like shape. Gives multiple modes at m=M and l=L.

        Returns
        -------
        modes : ndarray of int, shape(num_modes,3)
            array of mode numbers [l,m,n]
            each row is one basis function with modes (l,m,n)

        """
        default_L = {"ansi": M, "fringe": 2 * M, "chevron": M, "house": 2 * M}
        L = L if L >= 0 else default_L[index]

        if index == "ansi":
            pol_posm = [
                [(m + d, m) for m in range(0, M + 1) if m + d < M + 1]
                for d in range(0, L + 1, 2)
            ]

        elif index == "fringe":
            pol_posm = [
                [(m + d // 2, m - d // 2) for m in range(0, M + 1) if m - d // 2 >= 0]
                for d in range(0, L + 1, 2)
            ]

        elif index == "chevron":
            pol_posm = [(m + d, m) for m in range(0, M + 1) for d in range(0, L + 1, 2)]

        elif index == "house":
            pol_posm = [
                [(l, m) for m in range(0, M + 1) if l >= m and (l - m) % 2 == 0]
                for l in range(0, L + 1)
            ] + [(m, m) for m in range(M + 1)]
            pol_posm = list(dict.fromkeys(flatten_list(pol_posm)))

        pol = [
            [(l, m), (l, -m)] if m != 0 else [(l, m)] for l, m in flatten_list(pol_posm)
        ]
        pol = np.array(flatten_list(pol))
        num_pol = len(pol)

        pol = np.tile(pol, (2 * N + 1, 1))
        tor = np.atleast_2d(
            np.tile(np.arange(-N, N + 1), (num_pol, 1)).flatten(order="f")
        ).T
        return np.hstack([pol, tor])

    def evaluate(self, nodes, derivatives=np.array([0, 0, 0]), modes=None):
        """Evaluates basis functions at specified nodes

        Parameters
        ----------
        nodes : ndarray of float, size(num_nodes,3)
            node coordinates, in (rho,theta,zeta)
        derivatives : ndarray of int, shape(num_derivatives,3)
            order of derivatives to compute in (rho,theta,zeta)
        modes : ndarray of int, shape(num_modes,3), optional
            basis modes to evaluate (if None, full basis is used)

        Returns
        -------
        y : ndarray, shape(num_nodes,num_modes)
            basis functions evaluated at nodes

        """
        if modes is None:
            modes = self._modes

        radial = jacobi(nodes[:, 0], modes[:, 0], modes[:, 1], dr=derivatives[0])
        poloidal = fourier(nodes[:, 1], modes[:, 1], dt=derivatives[1])
        toroidal = fourier(nodes[:, 2], modes[:, 2], NFP=self._NFP, dt=derivatives[2])
        return radial * poloidal * toroidal

    def change_resolution(self, L: int, M: int, N: int) -> None:
        """Change resolution of the basis to the given resolutions.

        Parameters
        ----------
        L : int
            maximum radial resolution
        M : int
            maximum poloidal resolution
        N : int
            maximum toroidal resolution

        """
        if M != self._M or N != self._N or L != self._L:
            self._M = M
            self._N = N
            self._L = L
            self._modes = self._get_modes(self._L, self._M, self._N, index=self._index)
            self._sort_modes()


def polyder_vec(p, m):
    """Vectorized version of polyder

    For differentiating multiple polynomials of the same degree

    Parameters
    ----------
    p : ndarray, shape(N,M)
        polynomial coefficients. Each row is 1 polynomial, in descending powers of x,
        each column is a power of x
    m : int >=0
        order of derivative

    Returns
    -------
    der : ndarray, shape(N,M)
        polynomial coefficients for derivative in descending order

    """
    m = np.asarray(m, dtype=int)  # order of derivative
    p = np.atleast_2d(p)
    n = p.shape[1] - 1  # order of polynomials

    D = np.arange(n, -1, -1)
    D = factorial(D) / factorial(D - m)

    p = np.roll(D * p, m, axis=1)
    idx = np.arange(p.shape[1])
    p = np.where(idx < m, 0, p)

    return p


def polyval_vec(p, x):
    """Evaluate a polynomial at specific values

    Vectorized for evaluating multiple polynomials of the same degree.

    Parameters
    ----------
    p : ndarray, shape(N,M)
        Array of coefficient for N polynomials of order M.
        Each row is one polynomial, given in descending powers of x.
    x : ndarray, shape(K,)
        A number, or 1d array of numbers at
        which to evaluate p. If greater than 1d it is flattened.

    Returns
    -------
    y : ndarray, shape(N,K)
        polynomials evaluated at x.
        Each row corresponds to a polynomial, each column to a value of x

    Notes:
        Horner's scheme is used to evaluate the polynomial. Even so,
        for polynomials of high degree the values may be inaccurate due to
        rounding errors. Use carefully.

    """
    p = np.atleast_2d(p)
    x = np.atleast_1d(x).flatten()
    npoly = p.shape[0]  # number of polynomials
    order = p.shape[1]  # order of polynomials
    nx = len(x)  # number of coordinates
    y = np.zeros((npoly, nx))

    for k in range(order):
        y = y * x + np.atleast_2d(p[:, k]).T

    return y


def power_coeffs(l):
    """Power series

    Parameters
    ----------
    l : ndarray of int, shape(K,)
        radial mode number(s)

    Returns
    -------
    coeffs : ndarray, shape(l+1,)

    """
    l = np.atleast_1d(l).astype(int)
    npoly = len(l)  # number of polynomials
    order = np.max(l)  # order of polynomials
    coeffs = np.zeros((npoly, order + 1))
    coeffs[range(npoly), l] = 1
    return coeffs


def powers(rho, l, dr=0):
    """Power series

    Parameters
    ----------
    rho : ndarray, shape(N,)
        radial coordiantes to evaluate basis
    l : ndarray of int, shape(K,)
        radial mode number(s)
    dr : int
        order of derivative (Default = 0)

    Returns
    -------
    y : ndarray, shape(N,K)
        basis function(s) evaluated at specified points

    """
    coeffs = power_coeffs(l)
    coeffs = polyder_vec(np.fliplr(coeffs), dr)
    return polyval_vec(coeffs, rho).T


def jacobi_coeffs(l, m):
    """Jacobi polynomials

    Parameters
    ----------
    l : ndarray of int, shape(K,)
        radial mode number(s)
    m : ndarray of int, shape(K,)
        azimuthal mode number(s)

    Returns
    -------
    coeffs : ndarray

    """
    factorial = np.math.factorial
    l = np.atleast_1d(l).astype(int)
    m = np.atleast_1d(np.abs(m)).astype(int)
    npoly = len(l)
    lmax = np.max(l)
    coeffs = np.zeros((npoly, lmax + 1))
    lm_even = ((l - m) % 2 == 0)[:, np.newaxis]
    for ii in range(npoly):
        ll = l[ii]
        mm = m[ii]
        for s in range(mm, ll + 1, 2):
            coeffs[ii, s] = (
                (-1) ** ((ll - s) / 2)
                * factorial((ll + s) / 2)
                / (
                    factorial((ll - s) / 2)
                    * factorial((s + mm) / 2)
                    * factorial((s - mm) / 2)
                )
            )
    return np.fliplr(np.where(lm_even, coeffs, 0))


def jacobi(rho, l, m, dr=0):
    """Jacobi polynomials

    Parameters
    ----------
    rho : ndarray, shape(N,)
        radial coordiantes to evaluate basis
    l : ndarray of int, shape(K,)
        radial mode number(s)
    m : ndarray of int, shape(K,)
        azimuthal mode number(s)
    dr : int
        order of derivative (Default = 0)

    Returns
    -------
    y : ndarray, shape(N,K)
        basis function(s) evaluated at specified points

    """
    coeffs = jacobi_coeffs(l, m)
    coeffs = polyder_vec(coeffs, dr)
    return polyval_vec(coeffs, rho).T


def fourier(theta, m, NFP=1, dt=0):
    """Fourier series

    Parameters
    ----------
    theta : ndarray, shape(N,)
        poloidal/toroidal coordinates to evaluate basis
    m : ndarray of int, shape(K,)
        poloidal/toroidal mode number(s)
    NFP : int
        number of field periods (Default = 1)
    dt : int
        order of derivative (Default = 0)

    Returns
    -------
    y : ndarray, shape(N,K)
        basis function(s) evaluated at specified points

    """
    theta_2d = np.atleast_2d(theta).T
    m_2d = np.atleast_2d(m)
    m_pos = (m_2d >= 0).astype(int)
    m_neg = (m_2d < 0).astype(int)
    m_abs = np.abs(m_2d) * NFP
    if dt == 0:
        return m_pos * np.cos(m_abs * theta_2d) + m_neg * np.sin(m_abs * theta_2d)
    else:
        return m_abs * (m_neg - m_pos) * fourier(theta, -m, NFP=NFP, dt=dt - 1)


def zernike_norm(l, m):
    """Norm of a Zernike polynomial with l, m indexing.
    Returns the integral (Z^m_l)^2 r dr dt, r=[0,1], t=[0,2*pi]

    Parameters
    ----------
    l,m : int
        radial and azimuthal mode numbers.

    Returns
    -------
    norm : float
        norm of Zernike polynomial over unit disk.

    """
    return np.sqrt((2 * (l + 1)) / (np.pi * (1 + int(m == 0))))

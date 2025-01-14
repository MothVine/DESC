import pytest
import unittest
import numpy as np
from desc.plotting import (
    plot_1d,
    plot_2d,
    plot_3d,
    plot_surfaces,
    plot_section,
    plot_comparison,
    plot_logo,
    plot_grid,
    plot_basis,
    plot_coefficients,
    _find_idx,
    plot_field_lines_sfl,
    plot_boozer_modes,
    plot_boozer_surface,
    plot_qs_error,
    plot_coils,
)
from desc.grid import LinearGrid, ConcentricGrid, QuadratureGrid
from desc.basis import (
    PowerSeries,
    FourierSeries,
    DoubleFourierSeries,
    FourierZernikeBasis,
)
from desc.equilibrium import EquilibriaFamily
from desc.coils import FourierXYZCoil, CoilSet


@pytest.mark.mpl_image_compare(tolerance=50)
def test_1d_p(plot_eq):
    fig, ax = plot_1d(plot_eq, "p")
    return fig


@pytest.mark.mpl_image_compare(tolerance=50)
def test_1d_dpdr(plot_eq):
    fig, ax = plot_1d(plot_eq, "p_r")
    return fig


@pytest.mark.mpl_image_compare(tolerance=50)
def test_1d_iota(plot_eq):
    grid = LinearGrid(rho=0.5, theta=np.linspace(0, 2 * np.pi, 100), zeta=0, axis=True)
    fig, ax = plot_1d(plot_eq, "iota", grid=grid)
    return fig


@pytest.mark.mpl_image_compare(tolerance=50)
def test_1d_logpsi(plot_eq):
    fig, ax = plot_1d(plot_eq, "psi", log=True)
    return fig


@pytest.mark.mpl_image_compare(tolerance=50)
def test_2d_logF(plot_eq):
    grid = LinearGrid(
        rho=np.linspace(0, 1, 100),
        theta=np.linspace(0, 2 * np.pi, 100),
        zeta=0,
        axis=True,
    )
    fig, ax = plot_2d(plot_eq, "|F|", log=True, grid=grid)
    return fig


@pytest.mark.mpl_image_compare(tolerance=50)
def test_2d_g_tz(plot_eq):
    grid = LinearGrid(
        rho=0.5,
        theta=np.linspace(0, 2 * np.pi, 100),
        zeta=np.linspace(0, 2 * np.pi, 100),
        axis=True,
    )
    fig, ax = plot_2d(plot_eq, "sqrt(g)", grid=grid)
    return fig


@pytest.mark.mpl_image_compare(tolerance=50)
def test_2d_g_rz(plot_eq):
    grid = LinearGrid(
        rho=np.linspace(0, 1, 100),
        theta=0,
        zeta=np.linspace(0, 2 * np.pi, 100),
        axis=True,
    )
    fig, ax = plot_2d(plot_eq, "sqrt(g)", grid=grid)
    return fig


@pytest.mark.mpl_image_compare(tolerance=50)
def test_2d_lambda(plot_eq):
    fig, ax = plot_2d(plot_eq, "lambda")
    return fig


@pytest.mark.mpl_image_compare(tolerance=50)
def test_3d_B(plot_eq):
    fig, ax = plot_3d(plot_eq, "B^zeta")
    return fig


@pytest.mark.mpl_image_compare(tolerance=50)
def test_3d_J(plot_eq):
    grid = LinearGrid(
        rho=1,
        theta=np.linspace(0, 2 * np.pi, 100),
        zeta=np.linspace(0, 2 * np.pi, 100),
        axis=True,
    )
    fig, ax = plot_3d(plot_eq, "J^theta", grid=grid)
    return fig


@pytest.mark.mpl_image_compare(tolerance=50)
def test_3d_tz(plot_eq):
    grid = LinearGrid(
        rho=0.5,
        theta=np.linspace(0, 2 * np.pi, 100),
        zeta=np.linspace(0, 2 * np.pi, 100),
        axis=True,
    )
    fig, ax = plot_3d(plot_eq, "|F|", log=True, grid=grid)
    return fig


@pytest.mark.mpl_image_compare(tolerance=50)
def test_3d_rz(plot_eq):
    grid = LinearGrid(
        rho=np.linspace(0, 1, 100),
        theta=0,
        zeta=np.linspace(0, 2 * np.pi, 100),
        axis=True,
    )
    fig, ax = plot_3d(plot_eq, "p", grid=grid)
    return fig


@pytest.mark.mpl_image_compare(tolerance=50)
def test_3d_rt(plot_eq):
    grid = LinearGrid(
        rho=np.linspace(0, 1, 100), theta=np.linspace(0, 2 * np.pi, 100), zeta=0
    )
    fig, ax = plot_3d(plot_eq, "psi", grid=grid)
    return fig


@pytest.mark.mpl_image_compare(tolerance=50)
def test_section_J(plot_eq):
    fig, ax = plot_section(plot_eq, "J^rho")
    return fig


@pytest.mark.mpl_image_compare(tolerance=50)
def test_section_Z(plot_eq):
    fig, ax = plot_section(plot_eq, "Z")
    return fig


@pytest.mark.mpl_image_compare(tolerance=50)
def test_section_R(plot_eq):
    fig, ax = plot_section(plot_eq, "R")
    return fig


@pytest.mark.mpl_image_compare(tolerance=50)
def test_section_F(plot_eq):
    fig, ax = plot_section(plot_eq, "F_rho")
    return fig


@pytest.mark.mpl_image_compare(tolerance=50)
def test_section_logF(plot_eq):
    fig, ax = plot_section(plot_eq, "|F|", log=True)
    return fig


@pytest.mark.slow
@pytest.mark.mpl_image_compare(tolerance=50)
def test_plot_surfaces(plot_eq):
    fig, ax = plot_surfaces(plot_eq)
    return fig


@pytest.mark.slow
@pytest.mark.mpl_image_compare(tolerance=50)
def test_plot_comparison(DSHAPE):
    eqf = EquilibriaFamily.load(load_from=str(DSHAPE["desc_h5_path"]))
    fig, ax = plot_comparison(eqf)
    return fig


@pytest.mark.mpl_image_compare(tolerance=50)
def test_plot_con_basis(plot_eq):
    fig, ax = plot_2d(plot_eq, "e^rho", component="R")
    return fig


@pytest.mark.mpl_image_compare(tolerance=50)
def test_plot_cov_basis(plot_eq):
    fig, ax = plot_2d(plot_eq, "e_rho")
    return fig


@pytest.mark.mpl_image_compare(tolerance=50)
def test_plot_magnetic_tension(plot_eq):
    fig, ax = plot_2d(plot_eq, "|(B*grad)B|")
    return fig


@pytest.mark.mpl_image_compare(tolerance=50)
def test_plot_magnetic_pressure(plot_eq):
    fig, ax = plot_2d(plot_eq, "|grad(|B|^2)|")
    return fig


@pytest.mark.mpl_image_compare(tolerance=50)
def test_plot_gradpsi(plot_eq):
    fig, ax = plot_2d(plot_eq, "|grad(rho)|")
    return fig


@pytest.mark.mpl_image_compare(tolerance=50)
def test_plot_normF_2d(plot_eq):
    fig, ax = plot_2d(plot_eq, "|F|", norm_F=True)
    return fig


@pytest.mark.mpl_image_compare(tolerance=50)
def test_plot_normF_section(plot_eq):
    fig, ax = plot_section(plot_eq, "|F|", norm_F=True, log=True)
    return fig


@pytest.mark.mpl_image_compare(tolerance=50)
def test_plot_coefficients(plot_eq):
    fig, ax = plot_coefficients(plot_eq)
    return fig


@pytest.mark.mpl_image_compare(tolerance=50)
def test_plot_logo():
    fig, ax = plot_logo()
    return fig


class TestPlotGrid(unittest.TestCase):
    @pytest.mark.mpl_image_compare(tolerance=50)
    def test_plot_grid_linear(self):
        grid = LinearGrid(L=10, M=10, N=1)
        fig, ax = plot_grid(grid)
        return fig

    @pytest.mark.mpl_image_compare(tolerance=50)
    def test_plot_grid_quad(self):
        grid = QuadratureGrid(L=10, M=10, N=1)
        fig, ax = plot_grid(grid)
        return fig

    @pytest.mark.mpl_image_compare(tolerance=50)
    def test_plot_grid_jacobi(self):
        grid = ConcentricGrid(L=20, M=10, N=1, node_pattern="jacobi")
        fig, ax = plot_grid(grid)
        return fig

    @pytest.mark.mpl_image_compare(tolerance=50)
    def test_plot_grid_cheb1(self):
        grid = ConcentricGrid(L=20, M=10, N=1, node_pattern="cheb1")
        fig, ax = plot_grid(grid)
        return fig

    @pytest.mark.mpl_image_compare(tolerance=50)
    def test_plot_grid_cheb2(self):
        grid = ConcentricGrid(L=20, M=10, N=1, node_pattern="cheb2")
        fig, ax = plot_grid(grid)
        return fig

    @pytest.mark.mpl_image_compare(tolerance=50)
    def test_plot_grid_ocs(self):
        grid = ConcentricGrid(L=20, M=10, N=1, node_pattern="ocs")
        fig, ax = plot_grid(grid)
        return fig


class TestPlotBasis(unittest.TestCase):
    @pytest.mark.mpl_image_compare(tolerance=50)
    def test_plot_basis_powerseries(self):
        basis = PowerSeries(L=6)
        fig, ax = plot_basis(basis)
        return fig

    @pytest.mark.mpl_image_compare(tolerance=50)
    def test_plot_basis_fourierseries(self):
        basis = FourierSeries(N=3)
        fig, ax = plot_basis(basis)
        return fig

    @pytest.mark.slow
    @pytest.mark.mpl_image_compare(tolerance=50)
    def test_plot_basis_doublefourierseries(self):
        basis = DoubleFourierSeries(M=3, N=2)
        fig, ax = plot_basis(basis)
        return fig

    @pytest.mark.slow
    @pytest.mark.mpl_image_compare(tolerance=50)
    def test_plot_basis_fourierzernike(self):
        basis = FourierZernikeBasis(L=8, M=3, N=2)
        fig, ax = plot_basis(basis)
        return fig


class TestPlotFieldLines(unittest.TestCase):
    def test_find_idx(self):
        # pick the first grid node point, add epsilon to it, check it returns idx of 0
        grid = LinearGrid(L=2, M=2, N=2, axis=False)
        epsilon = np.finfo(float).eps
        test_point = grid.nodes[0, :] + epsilon
        idx = _find_idx(*test_point, grid=grid)
        self.assertEqual(idx, 0)

    def test_field_line_Rbf(self):
        pass


@pytest.mark.slow
@pytest.mark.mpl_image_compare(tolerance=50)
def test_plot_field_line(plot_eq):
    fig, ax, _ = plot_field_lines_sfl(plot_eq, rho=1, seed_thetas=0, phi_end=2 * np.pi)
    return fig


@pytest.mark.slow
@pytest.mark.mpl_image_compare(tolerance=50)
def test_plot_field_lines(plot_eq):
    fig, ax, _ = plot_field_lines_sfl(
        plot_eq, rho=1, seed_thetas=np.linspace(0, 2 * np.pi, 4), phi_end=2 * np.pi
    )
    return fig


@pytest.mark.mpl_image_compare(tolerance=50)
def test_plot_boozer_modes(plot_eq):
    fig, ax = plot_boozer_modes(plot_eq)
    return fig


@pytest.mark.mpl_image_compare(tolerance=50)
def test_plot_boozer_surface(plot_eq):
    fig, ax = plot_boozer_surface(plot_eq)
    return fig


@pytest.mark.mpl_image_compare(tolerance=50)
def test_plot_qs_error(plot_eq):
    fig, ax = plot_qs_error(plot_eq, helicity=(0, 0), log=False)
    return fig


@pytest.mark.mpl_image_compare(tolerance=50)
def test_plot_coils():
    R = 10
    N = 48
    NFP = 4
    I = 1
    coil = FourierXYZCoil()
    coil.rotate(angle=np.pi / N)
    coils = CoilSet.linspaced_angular(coil, I, [0, 0, 1], np.pi / NFP, N // NFP // 2)
    coils.grid = 100
    coils2 = CoilSet.from_symmetry(coils, NFP, True)
    fig, ax = plot_coils(coils2)

    return fig

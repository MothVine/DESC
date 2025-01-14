import unittest
import numpy as np

from desc.backend import jnp
from desc.utils import unpack_state
from desc.grid import LinearGrid
from desc.transform import Transform
from desc.compute import compute_toroidal_coords
from desc.equilibrium import Equilibrium
from desc.objective_funs import ObjectiveFunction
from desc.boundary_conditions import LCFSConstraint


class DummyFunLinear(ObjectiveFunction):
    """A dummy linear objective function."""

    @property
    def name(self):
        return "BC"

    @property
    def scalar(self):
        return False

    @property
    def derivatives(self):
        derivatives = np.array([[0, 0, 0]])
        return derivatives

    def compute(self, y, Rb_lmn, Zb_lmn, p_l, i_l, Psi):

        if self.BC_constraint is not None:
            x = self.BC_constraint.recover_from_constraints(y, Rb_lmn, Zb_lmn)

        R_lmn, Z_lmn, L_lmn = unpack_state(
            x, self.R_transform.basis.num_modes, self.Z_transform.basis.num_modes
        )

        toroidal_coords = compute_toroidal_coords(
            R_lmn,
            Z_lmn,
            self.R_transform,
            self.Z_transform,
        )

        axis = self.R_transform.grid.axis
        R0_mn = jnp.where(
            (self.Rb_transform.basis.modes == [0, 0, 0]).all(axis=1), Rb_lmn, 0
        ).sum()

        # f = R0_x / Psi - R0_b
        residual = toroidal_coords["R"][axis] / Psi - R0_mn
        return residual * jnp.ones_like(y)

    def compute_scalar(self, x, Rb_lmn, Zb_lmn, p_l, i_l, Psi):
        pass

    def callback(self, x, Rb_lmn, Zb_lmn, p_l, i_l, Psi) -> bool:
        pass


class TestPerturbations(unittest.TestCase):
    """Tests for pertubations."""

    def test_perturb_1D(self):
        """Linear test function where perturb order=1 is exact."""

        inputs = {
            "sym": True,
            "NFP": 1,
            "Psi": 1.0,
            "L": 2,
            "M": 2,
            "N": 1,
            "pressure": np.array([[0, 0]]),
            "iota": np.array([[0, 0]]),
            "surface": np.array([[0, -1, 0, 0, 2], [0, 0, 0, 3, 0], [0, 1, 0, 1, 0]]),
        }
        eq_old = Equilibrium(**inputs)
        grid = LinearGrid(NFP=eq_old.NFP, rho=0)
        R_transform = Transform(grid, eq_old.R_basis)
        Z_transform = Transform(grid, eq_old.Z_basis)
        L_transform = Transform(grid, eq_old.L_basis)
        pres = eq_old.pressure.copy()
        pres.grid = grid
        iota = eq_old.iota.copy()
        iota.grid = grid

        obj_fun = DummyFunLinear(
            R_transform=R_transform,
            Z_transform=Z_transform,
            L_transform=L_transform,
            p_profile=pres,
            i_profile=iota,
            BC_constraint=eq_old.surface.get_constraint(
                eq_old.R_basis, eq_old.Z_basis, eq_old.L_basis
            ),
        )
        eq_old.objective = obj_fun
        y = eq_old.objective.BC_constraint.project(eq_old.x)
        args = (y, eq_old.Rb_lmn, eq_old.Zb_lmn, eq_old.p_l, eq_old.i_l, eq_old.Psi)

        eq_old.objective.Rb_transform = eq_old.surface._R_transform
        eq_old.objective.compile(y, args[1:])
        res_old = eq_old.objective.compute(*args)

        deltas = {
            "dRb": np.zeros((eq_old.surface.R_basis.num_modes,)),
            "dZb": np.zeros((eq_old.surface.Z_basis.num_modes,)),
            "dPsi": 0.2,
        }
        idx_R = np.where((eq_old.surface.R_basis.modes == [0, 2, 1]).all(axis=1))[0]
        idx_Z = np.where((eq_old.surface.Z_basis.modes == [0, -2, 1]).all(axis=1))[0]
        deltas["dRb"][idx_R] = 0.5
        deltas["dZb"][idx_Z] = -0.3

        eq_new = eq_old.perturb(**deltas, order=1, tr_ratio=100, weight=None)
        y = eq_new.objective.BC_constraint.project(eq_new.x)
        args = (y, eq_new.Rb_lmn, eq_new.Zb_lmn, eq_new.p_l, eq_new.i_l, eq_new.Psi)
        eq_new.objective.Rb_transform = eq_new.surface._R_transform
        eq_new.objective.compile(y, args[1:])
        res_new = eq_new.objective.compute(*args)

        # tolerance could be lower if only testing with JAX
        np.testing.assert_allclose(res_old, 0, atol=1e-6)
        np.testing.assert_allclose(res_new, 0, atol=1e-6)

    def test_perturb_2D(self):
        """Nonlinear test function to check perturb convergence rates."""
        pass

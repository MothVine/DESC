"""data_index contains all of the quantities calculated by the compute functions.

label = (str) Title of the quantity in LaTeX format.
units = (str) Units of the quantity in LaTeX format.
units_long (str) Full units without abbreviations.
description (str) Description of the quantity.
fun = (str) Function name in compute_funs.py that computes the quantity.
dim = (int) Dimension of the quantity: 0-D, 1-D, or 3-D.
"""

data_index = {}
# flux coordinates
data_index["rho"] = {
    "label": "\\rho",
    "units": "~",
    "units_long": "None",
    "description": "Radial coordinate, proportional to the square root of the toroidal flux",
    "fun": "compute_flux_coords",
    "dim": 1,
}
data_index["theta"] = {
    "label": "\\theta",
    "units": "rad",
    "units_long": "radians",
    "description": "Poloidal angular coordinate (geometric, not magnetic)",
    "fun": "compute_flux_coords",
    "dim": 1,
}
data_index["zeta"] = {
    "label": "\\zeta",
    "units": "rad",
    "units_long": "radians",
    "description": "Toroidal angular coordinate, equal to the geometric toroidal angle",
    "fun": "compute_flux_coords",
    "dim": 1,
}
# toroidal flux
data_index["psi"] = {
    "label": "\\psi = \\Psi / (2 \\pi)",
    "units": "Wb",
    "units_long": "Webers",
    "description": "Toroidal flux",
    "fun": "compute_toroidal_flux",
    "dim": 1,
}
data_index["psi_r"] = {
    "label": "\\psi' = \\partial_{\\rho} \\Psi / (2 \\pi)",
    "units": "Wb",
    "units_long": "Webers",
    "description": "Toroidal flux, first radial derivative",
    "fun": "compute_toroidal_flux",
    "dim": 1,
}
data_index["psi_rr"] = {
    "label": "\\psi'' = \\partial_{\\rho\\rho} \\Psi / (2 \\pi)",
    "units": "Wb",
    "units_long": "Webers",
    "description": "Toroidal flux, second radial derivative",
    "fun": "compute_toroidal_flux",
    "dim": 1,
}
# R
data_index["R"] = {
    "label": "R",
    "units": "m",
    "units_long": "meters",
    "description": "Major radius in lab frame",
    "fun": "compute_toroidal_coords",
    "dim": 1,
    "R_derivs": [[0, 0, 0]],
}

data_index["R_r"] = {
    "label": "\\partial_{\\rho} R",
    "units": "m",
    "units_long": "meters",
    "description": "Major radius in lab frame, first radial derivative",
    "fun": "compute_toroidal_coords",
    "dim": 1,
    "R_derivs": [[1, 0, 0]],
}
data_index["R_t"] = {
    "label": "\\partial_{\\theta} R",
    "units": "m",
    "units_long": "meters",
    "description": "Major radius in lab frame, first poloidal derivative",
    "fun": "compute_toroidal_coords",
    "dim": 1,
    "R_derivs": [[0, 1, 0]],
}
data_index["R_z"] = {
    "label": "\\partial_{\\zeta} R",
    "units": "m",
    "units_long": "meters",
    "description": "Major radius in lab frame, first toroidal derivative",
    "fun": "compute_toroidal_coords",
    "dim": 1,
    "R_derivs": [[0, 0, 1]],
}
data_index["R_rr"] = {
    "label": "\\partial_{\\rho\\rho} R",
    "units": "m",
    "units_long": "meters",
    "description": "Major radius in lab frame, second radial derivative",
    "fun": "compute_toroidal_coords",
    "dim": 1,
    "R_derivs": [[2, 0, 0]],
}
data_index["R_tt"] = {
    "label": "\\partial_{\\theta\\theta} R",
    "units": "m",
    "units_long": "meters",
    "description": "Major radius in lab frame, second poloidal derivative",
    "fun": "compute_toroidal_coords",
    "dim": 1,
    "R_derivs": [[0, 2, 0]],
}
data_index["R_zz"] = {
    "label": "\\partial_{\\zeta\\zeta} R",
    "units": "m",
    "units_long": "meters",
    "description": "Major radius in lab frame, second toroidal derivative",
    "fun": "compute_toroidal_coords",
    "dim": 1,
    "R_derivs": [[0, 0, 2]],
}
data_index["R_rt"] = {
    "label": "\\partial_{\\rho\\theta} R",
    "units": "m",
    "units_long": "meters",
    "description": "Major radius in lab frame, second derivative wrt to radius and poloidal angle",
    "fun": "compute_toroidal_coords",
    "dim": 1,
    "R_derivs": [[1, 1, 0]],
}
data_index["R_rz"] = {
    "label": "\\partial_{\\rho\\zeta} R",
    "units": "m",
    "units_long": "meters",
    "description": "Major radius in lab frame, second derivative wrt to radius and toroidal angle",
    "fun": "compute_toroidal_coords",
    "dim": 1,
    "R_derivs": [[1, 0, 1]],
}

data_index["R_tz"] = {
    "label": "\\partial_{\\theta\\zeta} R",
    "units": "m",
    "units_long": "meters",
    "description": "Major radius in lab frame, second derivative wrt to poloidal and toroidal angles",
    "fun": "compute_toroidal_coords",
    "dim": 1,
    "R_derivs": [[0, 1, 1]],
}
data_index["R_rrr"] = {
    "label": "\\partial_{\\rho\\rho\\rho} R",
    "units": "m",
    "units_long": "meters",
    "description": "Major radius in lab frame, third radial derivative",
    "fun": "compute_toroidal_coords",
    "dim": 1,
    "R_derivs": [[3, 0, 0]],
}
data_index["R_ttt"] = {
    "label": "\\partial_{\\theta\\theta\\theta} R",
    "units": "m",
    "units_long": "meters",
    "description": "Major radius in lab frame, third poloidal derivative",
    "fun": "compute_toroidal_coords",
    "dim": 1,
    "R_derivs": [[0, 3, 0]],
}
data_index["R_zzz"] = {
    "label": "\\partial_{\\zeta\\zeta\\zeta} R",
    "units": "m",
    "units_long": "meters",
    "description": "Major radius in lab frame, third toroidal derivative",
    "fun": "compute_toroidal_coords",
    "dim": 1,
    "R_derivs": [[0, 0, 3]],
}
data_index["R_rrt"] = {
    "label": "\\partial_{\\rho\\rho\\theta} R",
    "units": "m",
    "units_long": "meters",
    "description": "Major radius in lab frame, third derivative, wrt to radius twice and poloidal angle",
    "fun": "compute_toroidal_coords",
    "dim": 1,
    "R_derivs": [[2, 1, 0]],
}
data_index["R_rtt"] = {
    "label": "\\partial_{\\rho\\theta\\theta} R",
    "units": "m",
    "units_long": "meters",
    "description": "Major radius in lab frame, third derivative wrt to radius and poloidal angle twice",
    "fun": "compute_toroidal_coords",
    "dim": 1,
    "R_derivs": [[1, 2, 0]],
}
data_index["R_rrz"] = {
    "label": "\\partial_{\\rho\\rho\\zeta} R",
    "units": "m",
    "units_long": "meters",
    "description": "Major radius in lab frame, third derivative wrt to radius twice and toroidal angle",
    "fun": "compute_toroidal_coords",
    "dim": 1,
    "R_derivs": [[2, 0, 1]],
}
data_index["R_rzz"] = {
    "label": "\\partial_{\\rho\\zeta\\zeta} R",
    "units": "m",
    "units_long": "meters",
    "description": "Major radius in lab frame, third derivative wrt to radius and toroidal angle twice",
    "fun": "compute_toroidal_coords",
    "dim": 1,
    "R_derivs": [[1, 0, 2]],
}
data_index["R_ttz"] = {
    "label": "\\partial_{\\theta\\theta\\zeta} R",
    "units": "m",
    "units_long": "meters",
    "description": "Major radius in lab frame, third derivative wrt to poloidal angle twice and toroidal angle",
    "fun": "compute_toroidal_coords",
    "dim": 1,
    "R_derivs": [[0, 2, 1]],
}
data_index["R_tzz"] = {
    "label": "\\partial_{\\theta\\zeta\\zeta} R",
    "units": "m",
    "units_long": "meters",
    "description": "Major radius in lab frame, third derivative wrt to poloidal angle  and toroidal angle twice",
    "fun": "compute_toroidal_coords",
    "dim": 1,
    "R_derivs": [[0, 1, 2]],
}
data_index["R_rtz"] = {
    "label": "\\partial_{\\rho\\theta\\zeta} R",
    "units": "m",
    "units_long": "meters",
    "description": "Major radius in lab frame, third derivative wrt to radius, poloidal angle, and toroidal angle",
    "fun": "compute_toroidal_coords",
    "dim": 1,
    "R_derivs": [[1, 1, 1]],
}
# Z
data_index["Z"] = {
    "label": "Z",
    "units": "m",
    "units_long": "meters",
    "description": "Vertical coordinate in lab frame",
    "fun": "compute_toroidal_coords",
    "dim": 1,
    "R_derivs": [[0, 0, 0]],
}
data_index["Z_r"] = {
    "label": "\\partial_{\\rho} Z",
    "units": "m",
    "units_long": "meters",
    "description": "Vertical coordinate in lab frame, first radial derivative",
    "fun": "compute_toroidal_coords",
    "dim": 1,
    "R_derivs": [[1, 0, 0]],
}
data_index["Z_t"] = {
    "label": "\\partial_{\\theta} Z",
    "units": "m",
    "units_long": "meters",
    "description": "Vertical coordinate in lab frame, first poloidal derivative",
    "fun": "compute_toroidal_coords",
    "dim": 1,
    "R_derivs": [[0, 1, 0]],
}
data_index["Z_z"] = {
    "label": "\\partial_{\\zeta} Z",
    "units": "m",
    "units_long": "meters",
    "description": "Vertical coordinate in lab frame, first toroidal derivative",
    "fun": "compute_toroidal_coords",
    "dim": 1,
    "R_derivs": [[0, 0, 1]],
}
data_index["Z_rr"] = {
    "label": "\\partial_{\\rho\\rho} Z",
    "units": "m",
    "units_long": "meters",
    "description": "Vertical coordinate in lab frame, second radial derivative",
    "fun": "compute_toroidal_coords",
    "dim": 1,
    "R_derivs": [[2, 0, 0]],
}
data_index["Z_tt"] = {
    "label": "\\partial_{\\theta\\theta} Z",
    "units": "m",
    "units_long": "meters",
    "description": "Vertical coordinate in lab frame, second poloidal derivative",
    "fun": "compute_toroidal_coords",
    "dim": 1,
    "R_derivs": [[0, 2, 0]],
}
data_index["Z_zz"] = {
    "label": "\\partial_{\\zeta\\zeta} Z",
    "units": "m",
    "units_long": "meters",
    "description": "Vertical coordinate in lab frame, second toroidal derivative",
    "fun": "compute_toroidal_coords",
    "dim": 1,
    "R_derivs": [[0, 0, 2]],
}
data_index["Z_rt"] = {
    "label": "\\partial_{\\rho\\theta} Z",
    "units": "m",
    "units_long": "meters",
    "description": "Vertical coordinate in lab frame, second derivative wrt to radius and poloidal angle",
    "fun": "compute_toroidal_coords",
    "dim": 1,
    "R_derivs": [[1, 1, 0]],
}
data_index["Z_rz"] = {
    "label": "\\partial_{\\rho\\zeta} Z",
    "units": "m",
    "units_long": "meters",
    "description": "Vertical coordinate in lab frame, second derivative wrt to radius and toroidal angle",
    "fun": "compute_toroidal_coords",
    "dim": 1,
    "R_derivs": [[1, 0, 1]],
}
data_index["Z_tz"] = {
    "label": "\\partial_{\\theta\\zeta} Z",
    "units": "m",
    "units_long": "meters",
    "description": "Vertical coordinate in lab frame, second derivative wrt to poloidal and toroidal angles",
    "fun": "compute_toroidal_coords",
    "dim": 1,
    "R_derivs": [[0, 1, 1]],
}
data_index["Z_rrr"] = {
    "label": "\\partial_{\\rho\\rho\\rho} Z",
    "units": "m",
    "units_long": "meters",
    "description": "Vertical coordinate in lab frame, third radial derivative",
    "fun": "compute_toroidal_coords",
    "dim": 1,
    "R_derivs": [[3, 0, 0]],
}
data_index["Z_ttt"] = {
    "label": "\\partial_{\\theta\\theta\\theta} Z",
    "units": "m",
    "units_long": "meters",
    "description": "Vertical coordinate in lab frame, third poloidal derivative",
    "fun": "compute_toroidal_coords",
    "dim": 1,
    "R_derivs": [[0, 3, 0]],
}
data_index["Z_zzz"] = {
    "label": "\\partial_{\\zeta\\zeta\\zeta} Z",
    "units": "m",
    "units_long": "meters",
    "description": "Vertical coordinate in lab frame, third toroidal derivative",
    "fun": "compute_toroidal_coords",
    "dim": 1,
    "R_derivs": [[0, 0, 3]],
}
data_index["Z_rrt"] = {
    "label": "\\partial_{\\rho\\rho\\theta} Z",
    "units": "m",
    "units_long": "meters",
    "description": "Vertical coordinate in lab frame, third derivative, wrt to radius twice and poloidal angle",
    "fun": "compute_toroidal_coords",
    "dim": 1,
    "R_derivs": [[2, 1, 0]],
}
data_index["Z_rtt"] = {
    "label": "\\partial_{\\rho\\theta\\theta} Z",
    "units": "m",
    "units_long": "meters",
    "description": "Vertical coordinate in lab frame, third derivative wrt to radius and poloidal angle twice",
    "fun": "compute_toroidal_coords",
    "dim": 1,
    "R_derivs": [[1, 2, 0]],
}
data_index["Z_rrz"] = {
    "label": "\\partial_{\\rho\\rho\\zeta} Z",
    "units": "m",
    "units_long": "meters",
    "description": "Vertical coordinate in lab frame, third derivative wrt to radius twice and toroidal angle",
    "fun": "compute_toroidal_coords",
    "dim": 1,
    "R_derivs": [[2, 0, 1]],
}
data_index["Z_rzz"] = {
    "label": "\\partial_{\\rho\\zeta\\zeta} Z",
    "units": "m",
    "units_long": "meters",
    "description": "Vertical coordinate in lab frame, third derivative wrt to radius and toroidal angle twice",
    "fun": "compute_toroidal_coords",
    "dim": 1,
    "R_derivs": [[1, 0, 2]],
}
data_index["Z_ttz"] = {
    "label": "\\partial_{\\theta\\theta\\zeta} Z",
    "units": "m",
    "units_long": "meters",
    "description": "Vertical coordinate in lab frame, third derivative wrt to poloidal angle twice and toroidal angle",
    "fun": "compute_toroidal_coords",
    "dim": 1,
    "R_derivs": [[0, 2, 1]],
}
data_index["Z_tzz"] = {
    "label": "\\partial_{\\theta\\zeta\\zeta} Z",
    "units": "m",
    "units_long": "meters",
    "description": "Vertical coordinate in lab frame, third derivative wrt to poloidal angle  and toroidal angle twice",
    "fun": "compute_toroidal_coords",
    "dim": 1,
    "R_derivs": [[0, 1, 2]],
}
data_index["Z_rtz"] = {
    "label": "\\partial_{\\rho\\theta\\zeta} Z",
    "units": "m",
    "units_long": "meters",
    "description": "Vertical coordinate in lab frame, third derivative wrt to radius, poloidal angle, and toroidal angle",
    "fun": "compute_toroidal_coords",
    "dim": 1,
    "R_derivs": [[1, 1, 1]],
}
# cartesian coordinates
data_index["phi"] = {
    "label": "\\phi = \\zeta",
    "units": "rad",
    "units_long": "radians",
    "description": "Toroidal angle in lab frame",
    "fun": "compute_cartesian_coords",
    "dim": 1,
    "R_derivs": [[0, 0, 0]],
}
data_index["X"] = {
    "label": "X = R \\cos{\\phi}",
    "units": "m",
    "units_long": "meters",
    "description": "Cartesian X coordinate",
    "fun": "compute_cartesian_coords",
    "dim": 1,
    "R_derivs": [[0, 0, 0]],
}
data_index["Y"] = {
    "label": "Y = R \\sin{\\phi}",
    "units": "m",
    "units_long": "meters",
    "description": "Cartesian Y coordinate",
    "fun": "compute_cartesian_coords",
    "dim": 1,
    "R_derivs": [[0, 0, 0]],
}
# lambda
data_index["lambda"] = {
    "label": "\\lambda",
    "units": "rad",
    "units_long": "radians",
    "description": "Poloidal stream function",
    "fun": "compute_lambda",
    "dim": 1,
    "L_derivs": [[0, 0, 0]],
}
data_index["lambda_r"] = {
    "label": "\\partial_{\\rho} \\lambda",
    "units": "rad",
    "units_long": "radians",
    "description": "Poloidal stream function, first radial derivative",
    "fun": "compute_lambda",
    "dim": 1,
    "L_derivs": [[1, 0, 0]],
}
data_index["lambda_t"] = {
    "label": "\\partial_{\\theta} \\lambda",
    "units": "rad",
    "units_long": "radians",
    "description": "Poloidal stream function, first poloidal derivative",
    "fun": "compute_lambda",
    "dim": 1,
    "L_derivs": [[0, 1, 0]],
}
data_index["lambda_z"] = {
    "label": "\\partial_{\\zeta} \\lambda",
    "units": "rad",
    "units_long": "radians",
    "description": "Poloidal stream function, first toroidal derivative",
    "fun": "compute_lambda",
    "dim": 1,
    "L_derivs": [[0, 0, 1]],
}
data_index["lambda_rr"] = {
    "label": "\\partial_{\\rho\\rho} \\lambda",
    "units": "rad",
    "units_long": "radians",
    "description": "Poloidal stream function, second radial derivative",
    "fun": "compute_lambda",
    "dim": 1,
    "L_derivs": [[2, 0, 0]],
}
data_index["lambda_tt"] = {
    "label": "\\partial_{\\theta\\theta} \\lambda",
    "units": "rad",
    "units_long": "radians",
    "description": "Poloidal stream function, second poloidal derivative",
    "fun": "compute_lambda",
    "dim": 1,
    "L_derivs": [[0, 2, 0]],
}
data_index["lambda_zz"] = {
    "label": "\\partial_{\\zeta\\zeta} \\lambda",
    "units": "rad",
    "units_long": "radians",
    "description": "Poloidal stream function, second toroidal derivative",
    "fun": "compute_lambda",
    "dim": 1,
    "L_derivs": [[0, 0, 2]],
}
data_index["lambda_rt"] = {
    "label": "\\partial_{\\rho\\theta} \\lambda",
    "units": "rad",
    "units_long": "radians",
    "description": "Poloidal stream function, second derivative wrt to radius and poloidal angle",
    "fun": "compute_lambda",
    "dim": 1,
    "L_derivs": [[1, 1, 0]],
}
data_index["lambda_rz"] = {
    "label": "\\partial_{\\rho\\zeta} \\lambda",
    "units": "rad",
    "units_long": "radians",
    "description": "Poloidal stream function, second derivative wrt to radius and toroidal angle",
    "fun": "compute_lambda",
    "dim": 1,
    "L_derivs": [[1, 0, 1]],
}
data_index["lambda_tz"] = {
    "label": "\\partial_{\\theta\\zeta} \\lambda",
    "units": "rad",
    "units_long": "radians",
    "description": "Poloidal stream function, second derivative wrt to poloidal and toroidal angles",
    "fun": "compute_lambda",
    "dim": 1,
    "L_derivs": [[0, 1, 1]],
}
data_index["lambda_rrr"] = {
    "label": "\\partial_{\\rho\\rho\\rho} \\lambda",
    "units": "rad",
    "units_long": "radians",
    "description": "Poloidal stream function, third radial derivative",
    "fun": "compute_lambda",
    "dim": 1,
    "L_derivs": [[3, 0, 0]],
}
data_index["lambda_ttt"] = {
    "label": "\\partial_{\\theta\\theta\\theta} \\lambda",
    "units": "rad",
    "units_long": "radians",
    "description": "Poloidal stream function, third poloidal derivative",
    "fun": "compute_lambda",
    "dim": 1,
    "L_derivs": [[0, 3, 0]],
}
data_index["lambda_zzz"] = {
    "label": "\\partial_{\\zeta\\zeta\\zeta} \\lambda",
    "units": "rad",
    "units_long": "radians",
    "description": "Poloidal stream function, third toroidal derivative",
    "fun": "compute_lambda",
    "dim": 1,
    "L_derivs": [[0, 0, 3]],
}
data_index["lambda_rrt"] = {
    "label": "\\partial_{\\rho\\rho\\theta} \\lambda",
    "units": "rad",
    "units_long": "radians",
    "description": "Poloidal stream function, third derivative, wrt to radius twice and poloidal angle",
    "fun": "compute_lambda",
    "dim": 1,
    "L_derivs": [[2, 1, 0]],
}
data_index["lambda_rtt"] = {
    "label": "\\partial_{\\rho\\theta\\theta} \\lambda",
    "units": "rad",
    "units_long": "radians",
    "description": "Poloidal stream function, third derivative wrt to radius and poloidal angle twice",
    "fun": "compute_lambda",
    "dim": 1,
    "L_derivs": [[1, 2, 0]],
}
data_index["lambda_rrz"] = {
    "label": "\\partial_{\\rho\\rho\\zeta} \\lambda",
    "units": "rad",
    "units_long": "radians",
    "description": "Poloidal stream function, third derivative wrt to radius twice and toroidal angle",
    "fun": "compute_lambda",
    "dim": 1,
    "L_derivs": [[2, 0, 1]],
}
data_index["lambda_rzz"] = {
    "label": "\\partial_{\\rho\\zeta\\zeta} \\lambda",
    "units": "rad",
    "units_long": "radians",
    "description": "Poloidal stream function, third derivative wrt to radius and toroidal angle twice",
    "fun": "compute_lambda",
    "dim": 1,
    "L_derivs": [[1, 0, 2]],
}
data_index["lambda_ttz"] = {
    "label": "\\partial_{\\theta\\theta\\zeta} \\lambda",
    "units": "rad",
    "units_long": "radians",
    "description": "Poloidal stream function, third derivative wrt to poloidal angle twice and toroidal angle",
    "fun": "compute_lambda",
    "dim": 1,
    "L_derivs": [[0, 2, 1]],
}
data_index["lambda_tzz"] = {
    "label": "\\partial_{\\theta\\zeta\\zeta} \\lambda",
    "units": "rad",
    "units_long": "radians",
    "description": "Poloidal stream function, third derivative wrt to poloidal angle  and toroidal angle twice",
    "fun": "compute_lambda",
    "dim": 1,
    "L_derivs": [[0, 1, 2]],
}
data_index["lambda_rtz"] = {
    "label": "\\partial_{\\rho\\theta\\zeta} \\lambda",
    "units": "rad",
    "units_long": "radians",
    "description": "Poloidal stream function, third derivative wrt to radius, poloidal angle, and toroidal angle",
    "fun": "compute_lambda",
    "dim": 1,
    "L_derivs": [[1, 1, 1]],
}
# pressure
data_index["p"] = {
    "label": "p",
    "units": "Pa",
    "units_long": "Pascal",
    "description": "Pressure",
    "fun": "compute_pressure",
    "dim": 1,
}
data_index["p_r"] = {
    "label": "\\partial_{\\rho} p",
    "units": "Pa",
    "units_long": "Pascal",
    "description": "Pressure, first radial derivative",
    "fun": "compute_pressure",
    "dim": 1,
}
# rotational transform
data_index["iota"] = {
    "label": "\\iota",
    "units": "~",
    "units_long": "None",
    "description": "Rotational transform",
    "fun": "compute_rotational_transform",
    "dim": 1,
}
data_index["iota_r"] = {
    "label": "\\partial_{\\rho} \\iota",
    "units": "~",
    "units_long": "None",
    "description": "Rotational transform, first radial derivative",
    "fun": "compute_rotational_transform",
    "dim": 1,
}
data_index["iota_rr"] = {
    "label": "\\partial_{\\rho\\rho} \\iota",
    "units": "~",
    "units_long": "None",
    "description": "Rotational transform, second radial derivative",
    "fun": "compute_rotational_transform",
    "dim": 1,
}
# covariant basis
data_index["e_rho"] = {
    "label": "\\mathbf{e}_{\\rho}",
    "units": "m",
    "units_long": "meters",
    "description": "Covariant radial basis vector",
    "fun": "compute_covariant_basis",
    "dim": 3,
    "R_derivs": [[1, 0, 0]],
}

data_index["e_theta"] = {
    "label": "\\mathbf{e}_{\\theta}",
    "units": "m",
    "units_long": "meters",
    "description": "Covariant poloidal basis vector",
    "fun": "compute_covariant_basis",
    "dim": 3,
    "R_derivs": [[0, 1, 0]],
}

data_index["e_zeta"] = {
    "label": "\\mathbf{e}_{\\zeta}",
    "units": "m",
    "units_long": "meters",
    "description": "Covariant toroidal basis vector",
    "fun": "compute_covariant_basis",
    "dim": 3,
    "R_derivs": [[0, 0, 0], [0, 0, 1]],
}

data_index["e_rho_r"] = {
    "label": "\\partial_{\\rho} \\mathbf{e}_{\\rho}",
    "units": "m",
    "units_long": "meters",
    "description": "Covariant radial basis vector, derivative wrt radial coordinate",
    "fun": "compute_covariant_basis",
    "dim": 3,
    "R_derivs": [[2, 0, 0]],
}

data_index["e_rho_t"] = {
    "label": "\\partial_{\\theta} \\mathbf{e}_{\\rho}",
    "units": "m",
    "units_long": "meters",
    "description": "Covariant radial basis vector, derivative wrt poloidal angle",
    "fun": "compute_covariant_basis",
    "dim": 3,
    "R_derivs": [[1, 1, 0]],
}

data_index["e_rho_z"] = {
    "label": "\\partial_{\\zeta} \\mathbf{e}_{\\rho}",
    "units": "m",
    "units_long": "meters",
    "description": "Covariant radial basis vector, derivative wrt toroidal angle",
    "fun": "compute_covariant_basis",
    "dim": 3,
    "R_derivs": [[1, 0, 1]],
}

data_index["e_theta_r"] = {
    "label": "\\partial_{\\rho} \\mathbf{e}_{\\theta}",
    "units": "m",
    "units_long": "meters",
    "description": "Covariant poloidal basis vector, derivative wrt radial coordinate",
    "fun": "compute_covariant_basis",
    "dim": 3,
    "R_derivs": [[1, 1, 0]],
}

data_index["e_theta_t"] = {
    "label": "\\partial_{\\theta} \\mathbf{e}_{\\theta}",
    "units": "m",
    "units_long": "meters",
    "description": "Covariant poloidal basis vector, derivative wrt poloidal angle",
    "fun": "compute_covariant_basis",
    "dim": 3,
    "R_derivs": [[0, 2, 0]],
}

data_index["e_theta_z"] = {
    "label": "\\partial_{\\zeta} \\mathbf{e}_{\\theta}",
    "units": "m",
    "units_long": "meters",
    "description": "Covariant poloidal basis vector, derivative wrt toroidal angle",
    "fun": "compute_covariant_basis",
    "dim": 3,
    "R_derivs": [[0, 1, 1]],
}

data_index["e_zeta_r"] = {
    "label": "\\partial_{\\rho} \\mathbf{e}_{\\zeta}",
    "units": "m",
    "units_long": "meters",
    "description": "Covariant toroidal basis vector, derivative wrt radial coordinate",
    "fun": "compute_covariant_basis",
    "dim": 3,
    "R_derivs": [[1, 0, 0], [1, 0, 1]],
}

data_index["e_zeta_t"] = {
    "label": "\\partial_{\\theta} \\mathbf{e}_{\\zeta}",
    "units": "m",
    "units_long": "meters",
    "description": "Covariant toroidal basis vector, derivative wrt poloidal angle",
    "fun": "compute_covariant_basis",
    "dim": 3,
    "R_derivs": [[0, 1, 0], [0, 1, 1]],
}

data_index["e_zeta_z"] = {
    "label": "\\partial_{\\zeta} \\mathbf{e}_{\\zeta}",
    "units": "m",
    "units_long": "meters",
    "description": "Covariant toroidal basis vector, derivative wrt toroidal angle",
    "fun": "compute_covariant_basis",
    "dim": 3,
    "R_derivs": [[0, 0, 1], [0, 0, 2]],
}

data_index["e_rho_rr"] = {
    "label": "\\partial_{\\rho\\rho} \\mathbf{e}_{\\rho}",
    "units": "m",
    "units_long": "meters",
    "description": "Covariant radial basis vector, second derivative wrt radial coordinate",
    "fun": "compute_covariant_basis",
    "dim": 3,
    "R_derivs": [[3, 0, 0]],
}

data_index["e_rho_tt"] = {
    "label": "\\partial_{\\theta\\theta} \\mathbf{e}_{\\rho}",
    "units": "m",
    "units_long": "meters",
    "description": "Covariant radial basis vector, second derivative wrt poloidal angle",
    "fun": "compute_covariant_basis",
    "dim": 3,
    "R_derivs": [[1, 2, 0]],
}

data_index["e_rho_zz"] = {
    "label": "\\partial_{\\zeta\\zeta} \\mathbf{e}_{\\rho}",
    "units": "m",
    "units_long": "meters",
    "description": "Covariant radial basis vector, second derivative wrt toroidal angle",
    "fun": "compute_covariant_basis",
    "dim": 3,
    "R_derivs": [[1, 0, 2]],
}

data_index["e_rho_rt"] = {
    "label": "\\partial_{\\rho\\theta} \\mathbf{e}_{\\rho}",
    "units": "m",
    "units_long": "meters",
    "description": "Covariant radial basis vector, second derivative wrt radial coordinate and poloidal angle",
    "fun": "compute_covariant_basis",
    "dim": 3,
    "R_derivs": [[2, 1, 0]],
}

data_index["e_rho_rz"] = {
    "label": "\\partial_{\\rho\\zeta} \\mathbf{e}_{\\rho}",
    "units": "m",
    "units_long": "meters",
    "description": "Covariant radial basis vector, second derivative wrt radial coordinate and toroidal angle",
    "fun": "compute_covariant_basis",
    "dim": 3,
    "R_derivs": [[2, 1, 0]],
}

data_index["e_rho_tz"] = {
    "label": "\\partial_{\\theta\\zeta} \\mathbf{e}_{\\rho}",
    "units": "m",
    "units_long": "meters",
    "description": "Covariant radial basis vector, second derivative wrt poloidal and toroidal angles",
    "fun": "compute_covariant_basis",
    "dim": 3,
    "R_derivs": [[1, 1, 1]],
}

data_index["e_theta_rr"] = {
    "label": "\\partial_{\\rho\\rho} \\mathbf{e}_{\\theta}",
    "units": "m",
    "units_long": "meters",
    "description": "Covariant poloidal basis vector, second derivative wrt radial coordinate",
    "fun": "compute_covariant_basis",
    "dim": 3,
    "R_derivs": [[2, 1, 0]],
}

data_index["e_theta_tt"] = {
    "label": "\\partial_{\\theta\\theta} \\mathbf{e}_{\\theta}",
    "units": "m",
    "units_long": "meters",
    "description": "Covariant poloidal basis vector, second derivative wrt poloidal angle",
    "fun": "compute_covariant_basis",
    "dim": 3,
    "R_derivs": [[0, 3, 0]],
}

data_index["e_theta_zz"] = {
    "label": "\\partial_{\\zeta\\zeta} \\mathbf{e}_{\\theta}",
    "units": "m",
    "units_long": "meters",
    "description": "Covariant poloidal basis vector, second derivative wrt toroidal angle",
    "fun": "compute_covariant_basis",
    "dim": 3,
    "R_derivs": [[0, 1, 2]],
}

data_index["e_theta_rt"] = {
    "label": "\\partial_{\\rho\\theta} \\mathbf{e}_{\\theta}",
    "units": "m",
    "units_long": "meters",
    "description": "Covariant poloidal basis vector, second derivative wrt radial coordinate and poloidal angle",
    "fun": "compute_covariant_basis",
    "dim": 3,
    "R_derivs": [[1, 2, 0]],
}

data_index["e_theta_rz"] = {
    "label": "\\partial_{\\rho\\zeta} \\mathbf{e}_{\\theta}",
    "units": "m",
    "units_long": "meters",
    "description": "Covariant poloidal basis vector, second derivative wrt radial coordinate and toroidal angle",
    "fun": "compute_covariant_basis",
    "dim": 3,
    "R_derivs": [[1, 1, 1]],
}

data_index["e_theta_tz"] = {
    "label": "\\partial_{\\theta\\zeta} \\mathbf{e}_{\\theta}",
    "units": "m",
    "units_long": "meters",
    "description": "Covariant poloidal basis vector, second derivative wrt poloidal and toroidal angles",
    "fun": "compute_covariant_basis",
    "dim": 3,
    "R_derivs": [[0, 2, 1]],
}

data_index["e_zeta_rr"] = {
    "label": "\\partial_{\\rho\\rho} \\mathbf{e}_{\\zeta}",
    "units": "m",
    "units_long": "meters",
    "description": "Covariant toroidal basis vector, second derivative wrt radial coordinate",
    "fun": "compute_covariant_basis",
    "dim": 3,
    "R_derivs": [[2, 0, 0], [2, 0, 1]],
}

data_index["e_zeta_tt"] = {
    "label": "\\partial_{\\theta\\theta} \\mathbf{e}_{\\zeta}",
    "units": "m",
    "units_long": "meters",
    "description": "Covariant toroidal basis vector, second derivative wrt poloidal angle",
    "fun": "compute_covariant_basis",
    "dim": 3,
    "R_derivs": [[0, 2, 0], [0, 2, 1]],
}

data_index["e_zeta_zz"] = {
    "label": "\\partial_{\\zeta\\zeta} \\mathbf{e}_{\\zeta}",
    "units": "m",
    "units_long": "meters",
    "description": "Covariant toroidal basis vector, second derivative wrt toroidal angle",
    "fun": "compute_covariant_basis",
    "dim": 3,
    "R_derivs": [[0, 0, 2], [0, 0, 3]],
}

data_index["e_zeta_rt"] = {
    "label": "\\partial_{\\rho\\theta} \\mathbf{e}_{\\zeta}",
    "units": "m",
    "units_long": "meters",
    "description": "Covariant toroidal basis vector, second derivative wrt radial coordinate and poloidal angle",
    "fun": "compute_covariant_basis",
    "dim": 3,
    "R_derivs": [[1, 1, 0], [1, 1, 1]],
}

data_index["e_zeta_rz"] = {
    "label": "\\partial_{\\rho\\zeta} \\mathbf{e}_{\\zeta}",
    "units": "m",
    "units_long": "meters",
    "description": "Covariant toroidal basis vector, second derivative wrt radial coordinate and toroidal angle",
    "fun": "compute_covariant_basis",
    "dim": 3,
    "R_derivs": [[1, 0, 1], [1, 0, 2]],
}

data_index["e_zeta_tz"] = {
    "label": "\\partial_{\\theta\\zeta} \\mathbf{e}_{\\zeta}",
    "units": "m",
    "units_long": "meters",
    "description": "Covariant toroidal basis vector, second derivative wrt poloidal and toroidal angles",
    "fun": "compute_covariant_basis",
    "dim": 3,
    "R_derivs": [[0, 1, 1], [0, 1, 2]],
}

# contravariant basis
data_index["e^rho"] = {
    "label": "\\mathbf{e}^{\\rho}",
    "units": "m^{-1}",
    "units_long": "inverse meters",
    "description": "Contravariant radial basis vector",
    "fun": "compute_contravariant_basis",
    "dim": 3,
    "R_derivs": [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]],
}

data_index["e^theta"] = {
    "label": "\\mathbf{e}^{\\theta}",
    "units": "m^{-1}",
    "units_long": "inverse meters",
    "description": "Contravariant poloidal basis vector",
    "fun": "compute_contravariant_basis",
    "dim": 3,
    "R_derivs": [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]],
}

data_index["e^zeta"] = {
    "label": "\\mathbf{e}^{\\zeta}",
    "units": "m^{-1}",
    "units_long": "inverse meters",
    "description": "Contravariant toroidal basis vector",
    "fun": "compute_contravariant_basis",
    "dim": 3,
    "R_derivs": [[0, 0, 0]],
}

# Jacobian
data_index["sqrt(g)"] = {
    "label": "\\sqrt{g}",
    "units": "m^{3}",
    "units_long": "cubic meters",
    "description": "Jacobian determinant",
    "fun": "compute_jacobian",
    "dim": 1,
    "R_derivs": [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]],
}

data_index["sqrt(g)_r"] = {
    "label": "\\partial_{\\rho} \\sqrt{g}",
    "units": "m^{3}",
    "units_long": "cubic meters",
    "description": "Jacobian determinant, derivative wrt radial coordinate",
    "fun": "compute_jacobian",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [2, 0, 0],
        [1, 1, 0],
        [1, 0, 1],
    ],
}

data_index["sqrt(g)_t"] = {
    "label": "\\partial_{\\theta} \\sqrt{g}",
    "units": "m^{3}",
    "units_long": "cubic meters",
    "description": "Jacobian determinant, derivative wrt poloidal angle",
    "fun": "compute_jacobian",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [1, 1, 0],
        [0, 1, 1],
    ],
}

data_index["sqrt(g)_z"] = {
    "label": "\\partial_{\\zeta} \\sqrt{g}",
    "units": "m^{3}",
    "units_long": "cubic meters",
    "description": "Jacobian determinant, derivative wrt toroidal angle",
    "fun": "compute_jacobian",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 0, 2],
        [1, 0, 1],
        [0, 1, 1],
    ],
}

data_index["sqrt(g)_rr"] = {
    "label": "\\partial_{\\rho\\rho} \\sqrt{g}",
    "units": "m^{3}",
    "units_long": "cubic meters",
    "description": "Jacobian determinant, second derivative wrt radial coordinate",
    "fun": "compute_jacobian",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [2, 0, 0],
        [1, 1, 0],
        [1, 0, 1],
        [3, 0, 0],
        [2, 1, 0],
        [2, 0, 1],
    ],
}

data_index["sqrt(g)_tt"] = {
    "label": "\\partial_{\\theta\\theta} \\sqrt{g}",
    "units": "m^{3}",
    "units_long": "cubic meters",
    "description": "Jacobian determinant, second derivative wrt poloidal angle",
    "fun": "compute_jacobian",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [1, 1, 0],
        [0, 1, 1],
        [0, 3, 0],
        [1, 2, 0],
        [0, 2, 1],
    ],
}

data_index["sqrt(g)_zz"] = {
    "label": "\\partial_{\\zeta\\zeta} \\sqrt{g}",
    "units": "m^{3}",
    "units_long": "cubic meters",
    "description": "Jacobian determinant, second derivative wrt toroidal angle",
    "fun": "compute_jacobian",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 0, 2],
        [1, 0, 1],
        [0, 1, 1],
        [0, 0, 3],
        [1, 0, 2],
        [0, 1, 2],
    ],
}

data_index["sqrt(g)_tz"] = {
    "label": "\\partial_{\\theta\\zeta} \\sqrt{g}",
    "units": "m^{3}",
    "units_long": "cubic meters",
    "description": "Jacobian determinant, second derivative wrt poloidal and toroidal angles",
    "fun": "compute_jacobian",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
        [0, 2, 1],
        [0, 1, 2],
        [1, 1, 1],
    ],
}

# covariant metric coefficients
data_index["g_rr"] = {
    "label": "g_{\\rho\\rho}",
    "units": "m^{2}",
    "units_long": "square meters",
    "description": "Radial/Radial element of covariant metric tensor",
    "fun": "compute_covariant_metric_coefficients",
    "dim": 1,
    "R_derivs": [[1, 0, 0]],
}

data_index["g_tt"] = {
    "label": "g_{\\theta\\theta}",
    "units": "m^{2}",
    "units_long": "square meters",
    "description": "Poloidal/Poloidal element of covariant metric tensor",
    "fun": "compute_covariant_metric_coefficients",
    "dim": 1,
    "R_derivs": [[0, 1, 0]],
}

data_index["g_zz"] = {
    "label": "g_{\\zeta\\zeta}",
    "units": "m^{2}",
    "units_long": "square meters",
    "description": "Toroidal/Toroidal element of covariant metric tensor",
    "fun": "compute_covariant_metric_coefficients",
    "dim": 1,
    "R_derivs": [[0, 0, 0], [0, 0, 1]],
}

data_index["g_rt"] = {
    "label": "g_{\\rho\\theta}",
    "units": "m^{2}",
    "units_long": "square meters",
    "description": "Radial/Poloidal element of covariant metric tensor",
    "fun": "compute_covariant_metric_coefficients",
    "dim": 1,
    "R_derivs": [[1, 0, 0], [0, 1, 0]],
}

data_index["g_rz"] = {
    "label": "g_{\\rho\\zeta}",
    "units": "m^{2}",
    "units_long": "square meters",
    "description": "Radial/Toroidal element of covariant metric tensor",
    "fun": "compute_covariant_metric_coefficients",
    "dim": 1,
    "R_derivs": [[1, 0, 0], [0, 0, 1]],
}

data_index["g_tz"] = {
    "label": "g_{\\theta\\zeta}",
    "units": "m^{2}",
    "units_long": "square meters",
    "description": "Poloidal/Toroidal element of covariant metric tensor",
    "fun": "compute_covariant_metric_coefficients",
    "dim": 1,
    "R_derivs": [[0, 0, 0], [0, 1, 0], [0, 0, 1]],
}

# contravariant metric coefficients
data_index["g^rr"] = {
    "label": "g^{\\rho\\rho}",
    "units": "m^{-2}",
    "units_long": "inverse square meters",
    "description": "Radial/Radial element of contravariant metric tensor",
    "fun": "compute_contravariant_metric_coefficients",
    "dim": 1,
    "R_derivs": [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]],
}

data_index["g^tt"] = {
    "label": "g^{\\theta\\theta}",
    "units": "m^{-2}",
    "units_long": "inverse square meters",
    "description": "Poloidal/Poloidal element of contravariant metric tensor",
    "fun": "compute_contravariant_metric_coefficients",
    "dim": 1,
    "R_derivs": [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]],
}

data_index["g^zz"] = {
    "label": "g^{\\zeta\\zeta}",
    "units": "m^{-2}",
    "units_long": "inverse square meters",
    "description": "Toroidal/Toroidal element of contravariant metric tensor",
    "fun": "compute_contravariant_metric_coefficients",
    "dim": 1,
    "R_derivs": [[0, 0, 0]],
}

data_index["g^rt"] = {
    "label": "g^{\\rho\\theta}",
    "units": "m^{-2}",
    "units_long": "inverse square meters",
    "description": "Radial/Poloidal element of contravariant metric tensor",
    "fun": "compute_contravariant_metric_coefficients",
    "dim": 1,
    "R_derivs": [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]],
}

data_index["g^rz"] = {
    "label": "g^{\\rho\\zeta}",
    "units": "m^{-2}",
    "units_long": "inverse square meters",
    "description": "Radial/Toroidal element of contravariant metric tensor",
    "fun": "compute_contravariant_metric_coefficients",
    "dim": 1,
    "R_derivs": [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]],
}

data_index["g^tz"] = {
    "label": "g^{\\theta\\zeta}",
    "units": "m^{-2}",
    "units_long": "inverse square meters",
    "description": "Poloidal/Toroidal element of contravariant metric tensor",
    "fun": "compute_contravariant_metric_coefficients",
    "dim": 1,
    "R_derivs": [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]],
}

data_index["|grad(rho)|"] = {
    "label": "|\\nabla \\rho|",
    "units": "m^{-1}",
    "units_long": "inverse meters",
    "description": "Magnitude of contravariant radial basis vector",
    "fun": "compute_contravariant_metric_coefficients",
    "dim": 1,
    "R_derivs": [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]],
}

data_index["|grad(theta)|"] = {
    "label": "|\\nabla \\theta|",
    "units": "m^{-1}",
    "units_long": "inverse meters",
    "description": "Magnitude of contravariant poloidal basis vector",
    "fun": "compute_contravariant_metric_coefficients",
    "dim": 1,
    "R_derivs": [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]],
}

data_index["|grad(zeta)|"] = {
    "label": "|\\nabla \\zeta|",
    "units": "m^{-1}",
    "units_long": "inverse meters",
    "description": "Magnitude of contravariant toroidal basis vector",
    "fun": "compute_contravariant_metric_coefficients",
    "dim": 1,
    "R_derivs": [[0, 0, 0]],
}

# contravariant magnetic field
data_index["B0"] = {
    "label": "\\psi' / \\sqrt{g}",
    "units": "T m^{-1}",
    "units_long": "Tesla / meters",
    "description": "",
    "fun": "compute_contravariant_magnetic_field",
    "dim": 1,
    "R_derivs": [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]],
    "L_derivs": [[0, 0, 0]],
}

data_index["B^rho"] = {
    "label": "B^{\\rho}",
    "units": "T m^{-1}",
    "units_long": "Tesla / meters",
    "description": "Contravariant radial component of magnetic field",
    "fun": "compute_contravariant_magnetic_field",
    "dim": 1,
    "R_derivs": [[0, 0, 0]],
    "L_derivs": [[0, 0, 0]],
}

data_index["B^theta"] = {
    "label": "B^{\\theta}",
    "units": "T m^{-1}",
    "units_long": "Tesla / meters",
    "description": "Contravariant poloidal component of magnetic field",
    "fun": "compute_contravariant_magnetic_field",
    "dim": 1,
    "R_derivs": [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]],
    "L_derivs": [[0, 0, 0], [0, 0, 1]],
}

data_index["B^zeta"] = {
    "label": "B^{\\zeta}",
    "units": "T m^{-1}",
    "units_long": "Tesla / meters",
    "description": "Contravariant toroidal component of magnetic field",
    "fun": "compute_contravariant_magnetic_field",
    "dim": 1,
    "R_derivs": [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]],
    "L_derivs": [[0, 0, 0], [0, 1, 0]],
}

data_index["B"] = {
    "label": "\\mathbf{B}",
    "units": "T",
    "units_long": "Tesla",
    "description": "Magnetic field",
    "fun": "compute_contravariant_magnetic_field",
    "dim": 3,
    "R_derivs": [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 0, 1]],
}

data_index["B_R"] = {
    "label": "B_{R}",
    "units": "T",
    "units_long": "Tesla",
    "description": "Radial component of magnetic field in lab frame",
    "fun": "compute_contravariant_magnetic_field",
    "dim": 1,
    "R_derivs": [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 0, 1]],
}

data_index["B_phi"] = {
    "label": "B_{\\phi}",
    "units": "T",
    "units_long": "Tesla",
    "description": "Toroidal component of magnetic field in lab frame",
    "fun": "compute_contravariant_magnetic_field",
    "dim": 1,
    "R_derivs": [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 0, 1]],
}

data_index["B_Z"] = {
    "label": "B_{Z}",
    "units": "T",
    "units_long": "Tesla",
    "description": "Vertical component of magnetic field in lab frame",
    "fun": "compute_contravariant_magnetic_field",
    "dim": 1,
    "R_derivs": [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 0, 1]],
}

data_index["B0_r"] = {
    "label": "\\psi'' / \\sqrt{g} - \\psi' \\partial_{\\rho} \\sqrt{g} / g",
    "units": "T \\cdot m^{-1}",
    "units_long": "Tesla / meters",
    "description": "",
    "fun": "compute_contravariant_magnetic_field",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [2, 0, 0],
        [1, 1, 0],
        [1, 0, 1],
    ],
    "L_derivs": [[0, 0, 0]],
}

data_index["B^theta_r"] = {
    "label": "\\partial_{\\rho} B^{\\theta}",
    "units": "T \\cdot m^{-1}",
    "units_long": "Tesla / meters",
    "description": "Contravariant poloidal component of magnetic field, derivative wrt radial coordinate",
    "fun": "compute_contravariant_magnetic_field",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [2, 0, 0],
        [1, 1, 0],
        [1, 0, 1],
    ],
    "L_derivs": [[0, 0, 0], [0, 0, 1], [1, 0, 1]],
}

data_index["B^zeta_r"] = {
    "label": "\\partial_{\\rho} B^{\\zeta}",
    "units": "T \\cdot m^{-1}",
    "units_long": "Tesla / meters",
    "description": "Contravariant toroidal component of magnetic field, derivative wrt radial coordinate",
    "fun": "compute_contravariant_magnetic_field",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [2, 0, 0],
        [1, 1, 0],
        [1, 0, 1],
    ],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [1, 1, 0]],
}

data_index["B_r"] = {
    "label": "\\partial_{\\rho} \\mathbf{B}",
    "units": "T",
    "units_long": "Tesla",
    "description": "Magnetic field, derivative wrt radial coordinate",
    "fun": "compute_contravariant_magnetic_field",
    "dim": 3,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [2, 0, 0],
        [1, 1, 0],
        [1, 0, 1],
    ],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 0, 1], [1, 0, 1], [1, 1, 0]],
}

data_index["B0_t"] = {
    "label": "-\\psi' \\partial_{\\theta} \\sqrt{g} / g",
    "units": "T \\cdot m^{-1}",
    "units_long": "Tesla / meters",
    "description": "",
    "fun": "compute_contravariant_magnetic_field",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [1, 1, 0],
        [0, 1, 1],
    ],
    "L_derivs": [[0, 0, 0]],
}

data_index["B^theta_t"] = {
    "label": "\\partial_{\\theta} B^{\\theta}",
    "units": "T \\cdot m^{-1}",
    "units_long": "Tesla / meters",
    "description": "Contravariant poloidal component of magnetic field, derivative wrt poloidal angle",
    "fun": "compute_contravariant_magnetic_field",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [1, 1, 0],
        [0, 1, 1],
    ],
    "L_derivs": [[0, 0, 0], [0, 0, 1], [0, 1, 1]],
}

data_index["B^zeta_t"] = {
    "label": "\\partial_{\\theta} B^{\\zeta}",
    "units": "T \\cdot m^{-1}",
    "units_long": "Tesla / meters",
    "description": "Contravariant toroidal component of magnetic field, derivative wrt poloidal angle",
    "fun": "compute_contravariant_magnetic_field",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [1, 1, 0],
        [0, 1, 1],
    ],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 2, 0]],
}

data_index["B_t"] = {
    "label": "\\partial_{\\theta} \\mathbf{B}",
    "units": "T",
    "units_long": "Tesla",
    "description": "Magnetic field, derivative wrt poloidal angle",
    "fun": "compute_contravariant_magnetic_field",
    "dim": 3,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [1, 1, 0],
        [0, 1, 1],
    ],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 0, 1], [0, 1, 1]],
}

data_index["B0_z"] = {
    "label": "-\\psi' \\partial_{\\zeta} \\sqrt{g} / g",
    "units": "T \\cdot m^{-1}",
    "units_long": "Tesla / meters",
    "description": "",
    "fun": "compute_contravariant_magnetic_field",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 0, 2],
        [1, 0, 1],
        [0, 1, 1],
    ],
    "L_derivs": [[0, 0, 0]],
}

data_index["B^theta_z"] = {
    "label": "\\partial_{\\zeta} B^{\\theta}",
    "units": "T \\cdot m^{-1}",
    "units_long": "Tesla / meters",
    "description": "Contravariant poloidal component of magnetic field, derivative wrt toroidal angle",
    "fun": "compute_contravariant_magnetic_field",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 0, 2],
        [1, 0, 1],
        [0, 1, 1],
    ],
    "L_derivs": [[0, 0, 0], [0, 0, 1], [0, 0, 2]],
}

data_index["B^zeta_z"] = {
    "label": "\\partial_{\\zeta} B^{\\zeta}",
    "units": "T \\cdot m^{-1}",
    "units_long": "Tesla / meters",
    "description": "Contravariant toroidal component of magnetic field, derivative wrt toroidal angle",
    "fun": "compute_contravariant_magnetic_field",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 0, 2],
        [1, 0, 1],
        [0, 1, 1],
    ],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 1, 1]],
}

data_index["B_z"] = {
    "label": "\\partial_{\\zeta} \\mathbf{B}",
    "units": "T",
    "units_long": "Tesla",
    "description": "Magnetic field, derivative wrt toroidal angle",
    "fun": "compute_contravariant_magnetic_field",
    "dim": 3,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 0, 2],
        [1, 0, 1],
        [0, 1, 1],
    ],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 2], [0, 1, 1]],
}

data_index["B0_tt"] = {
    "label": "-\\psi' \\partial_{\\theta\\theta} \\sqrt{g} / g + "
    + "2 \\psi' (\\partial_{\\theta} \\sqrt{g})^2 / (\\sqrt{g})^{3}",
    "units": "T \\cdot m^{-1}",
    "units_long": "Tesla / meters",
    "description": "",
    "fun": "compute_contravariant_magnetic_field",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [1, 1, 0],
        [0, 1, 1],
        [0, 3, 0],
        [1, 2, 0],
        [0, 2, 1],
    ],
    "L_derivs": [[0, 0, 0]],
}
data_index["B^theta_tt"] = {
    "label": "\\partial_{\\theta\\theta} B^{\\theta}",
    "units": "T \\cdot m^{-1}",
    "units_long": "Tesla / meters",
    "description": "Contravariant poloidal component of magnetic field, second derivative wrt poloidal angle",
    "fun": "compute_contravariant_magnetic_field",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [1, 1, 0],
        [0, 1, 1],
        [0, 3, 0],
        [1, 2, 0],
        [0, 2, 1],
    ],
    "L_derivs": [[0, 0, 0], [0, 0, 1], [0, 1, 1], [0, 2, 1]],
}

data_index["B^zeta_tt"] = {
    "label": "\\partial_{\\theta\\theta} B^{\\zeta}",
    "units": "T \\cdot m^{-1}",
    "units_long": "Tesla / meters",
    "description": "Contravariant toroidal component of magnetic field, second derivative wrt poloidal angle",
    "fun": "compute_contravariant_magnetic_field",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [1, 1, 0],
        [0, 1, 1],
        [0, 3, 0],
        [1, 2, 0],
        [0, 2, 1],
    ],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 2, 0], [0, 3, 0]],
}
data_index["B0_zz"] = {
    "label": "-\\psi' \\partial_{\\zeta\\zeta} \\sqrt{g} / g + "
    + "2 \\psi' (\\partial_{\\zeta} \\sqrt{g})^2 / (\\sqrt{g})^{3}",
    "units": "T \\cdot m^{-1}",
    "units_long": "Tesla / meters",
    "description": "",
    "fun": "compute_contravariant_magnetic_field",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 0, 2],
        [1, 0, 1],
        [0, 1, 1],
        [0, 0, 3],
        [1, 0, 2],
        [0, 1, 2],
    ],
    "L_derivs": [[0, 0, 0]],
}
data_index["B^theta_zz"] = {
    "label": "\\partial_{\\zeta\\zeta} B^{\\theta}",
    "units": "T \\cdot m^{-1}",
    "units_long": "Tesla / meters",
    "description": "Contravariant poloidal component of magnetic field, second derivative wrt toroidal angle",
    "fun": "compute_contravariant_magnetic_field",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 0, 2],
        [1, 0, 1],
        [0, 1, 1],
        [0, 0, 3],
        [1, 0, 2],
        [0, 1, 2],
    ],
    "L_derivs": [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 0, 3]],
}
data_index["B^zeta_zz"] = {
    "label": "\\partial_{\\zeta\\zeta} B^{\\zeta}",
    "units": "T \\cdot m^{-1}",
    "units_long": "Tesla / meters",
    "description": "Contravariant toroidal component of magnetic field, second derivative wrt toroidal angle",
    "fun": "compute_contravariant_magnetic_field",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 0, 2],
        [1, 0, 1],
        [0, 1, 1],
        [0, 0, 3],
        [1, 0, 2],
        [0, 1, 2],
    ],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 1, 1], [0, 1, 2]],
}
data_index["B0_tz"] = {
    "label": "-\\psi' \\partial_{\\theta\\zeta} \\sqrt{g} / g + "
    + "2 \\psi' \\partial_{\\theta} \\sqrt{g} \\partial_{\\zeta} \\sqrt{g} / "
    + "(\\sqrt{g})^{3}",
    "units": "T \\cdot m^{-1}",
    "units_long": "Tesla / meters",
    "description": "",
    "fun": "compute_contravariant_magnetic_field",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
        [0, 2, 1],
        [0, 1, 2],
        [1, 1, 1],
    ],
    "L_derivs": [[0, 0, 0]],
}
data_index["B^theta_tz"] = {
    "label": "\\partial_{\\theta\\zeta} B^{\\theta}",
    "units": "T \\cdot m^{-1}",
    "units_long": "Tesla / meters",
    "description": "Contravariant poloidal component of magnetic field, second derivative wrt poloidal and toroidal angles",
    "fun": "compute_contravariant_magnetic_field",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
        [0, 2, 1],
        [0, 1, 2],
        [1, 1, 1],
    ],
    "L_derivs": [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 1], [0, 1, 2]],
}
data_index["B^zeta_tz"] = {
    "label": "\\partial_{\\theta\\zeta} B^{\\zeta}",
    "units": "T \\cdot m^{-1}",
    "units_long": "Tesla / meters",
    "description": "Contravariant toroidal component of magnetic field, second derivative wrt poloidal and toroidal angles",
    "fun": "compute_contravariant_magnetic_field",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
        [0, 2, 1],
        [0, 1, 2],
        [1, 1, 1],
    ],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 2, 0], [0, 1, 1], [0, 2, 1]],
}
# covariant magnetic field
data_index["B_rho"] = {
    "label": "B_{\\rho}",
    "units": "T \\cdot m",
    "units_long": "Tesla * meters",
    "description": "Covariant radial component of magnetic field",
    "fun": "compute_covariant_magnetic_field",
    "dim": 1,
    "R_derivs": [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 0, 1]],
}
data_index["B_theta"] = {
    "label": "B_{\\theta}",
    "units": "T \\cdot m",
    "units_long": "Tesla * meters",
    "description": "Covariant poloidal component of magnetic field",
    "fun": "compute_covariant_magnetic_field",
    "dim": 1,
    "R_derivs": [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 0, 1]],
}
data_index["B_zeta"] = {
    "label": "B_{\\zeta}",
    "units": "T \\cdot m",
    "units_long": "Tesla * meters",
    "description": "Covariant toroidal component of magnetic field",
    "fun": "compute_covariant_magnetic_field",
    "dim": 1,
    "R_derivs": [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 0, 1]],
}
data_index["B_rho_r"] = {
    "label": "\\partial_{\\rho} B_{\\rho}",
    "units": "T \\cdot m",
    "units_long": "Tesla * meters",
    "description": "Covariant radial component of magnetic field, derivative wrt radial coordinate",
    "fun": "compute_covariant_magnetic_field",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [2, 0, 0],
        [1, 1, 0],
        [1, 0, 1],
    ],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 0], [1, 0, 1]],
}
data_index["B_theta_r"] = {
    "label": "\\partial_{\\rho} B_{\\theta}",
    "units": "T \\cdot m",
    "units_long": "Tesla * meters",
    "description": "Covariant poloidal component of magnetic field, derivative wrt radial coordinate",
    "fun": "compute_covariant_magnetic_field",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [2, 0, 0],
        [1, 1, 0],
        [1, 0, 1],
    ],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 0], [1, 0, 1]],
}
data_index["B_zeta_r"] = {
    "label": "\\partial_{\\rho} B_{\\zeta}",
    "units": "T \\cdot m",
    "units_long": "Tesla * meters",
    "description": "Covariant toroidal component of magnetic field, derivative wrt radial coordinate",
    "fun": "compute_covariant_magnetic_field",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [2, 0, 0],
        [1, 1, 0],
        [1, 0, 1],
    ],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 0], [1, 0, 1]],
}
data_index["B_rho_t"] = {
    "label": "\\partial_{\\theta} B_{\\rho}",
    "units": "T \\cdot m",
    "units_long": "Tesla * meters",
    "description": "Covariant radial component of magnetic field, derivative wrt poloidal angle",
    "fun": "compute_covariant_magnetic_field",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [1, 1, 0],
        [0, 1, 1],
    ],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 0, 1], [0, 2, 0], [0, 1, 1]],
}
data_index["B_theta_t"] = {
    "label": "\\partial_{\\theta} B_{\\theta}",
    "units": "T \\cdot m",
    "units_long": "Tesla * meters",
    "description": "Covariant poloidal component of magnetic field, derivative wrt poloidal angle",
    "fun": "compute_covariant_magnetic_field",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [1, 1, 0],
        [0, 1, 1],
    ],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 0, 1], [0, 2, 0], [0, 1, 1]],
}
data_index["B_zeta_t"] = {
    "label": "\\partial_{\\theta} B_{\\zeta}",
    "units": "T \\cdot m",
    "units_long": "Tesla * meters",
    "description": "Covariant toroidal component of magnetic field, derivative wrt poloidal angle",
    "fun": "compute_covariant_magnetic_field",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [1, 1, 0],
        [0, 1, 1],
    ],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 0, 1], [0, 2, 0], [0, 1, 1]],
}
data_index["B_rho_z"] = {
    "label": "\\partial_{\\zeta} B_{\\rho}",
    "units": "T \\cdot m",
    "units_long": "Tesla * meters",
    "description": "Covariant radial component of magnetic field, derivative wrt toroidal angle",
    "fun": "compute_covariant_magnetic_field",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 0, 2],
        [1, 0, 1],
        [0, 1, 1],
    ],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 2], [0, 1, 1]],
}
data_index["B_theta_z"] = {
    "label": "\\partial_{\\zeta} B_{\\theta}",
    "units": "T \\cdot m",
    "units_long": "Tesla * meters",
    "description": "Covariant poloidal component of magnetic field, derivative wrt toroidal angle",
    "fun": "compute_covariant_magnetic_field",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 0, 2],
        [1, 0, 1],
        [0, 1, 1],
    ],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 2], [0, 1, 1]],
}
data_index["B_zeta_z"] = {
    "label": "\\partial_{\\zeta} B_{\\zeta}",
    "units": "T \\cdot m",
    "units_long": "Tesla * meters",
    "description": "Covariant toroidal component of magnetic field, derivative wrt toroidal angle",
    "fun": "compute_covariant_magnetic_field",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 0, 2],
        [1, 0, 1],
        [0, 1, 1],
    ],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 2], [0, 1, 1]],
}
# magnetic field magnitude
data_index["|B|"] = {
    "label": "|\\mathbf{B}|",
    "units": "T",
    "units_long": "Tesla",
    "description": "Magnitude of magnetic field",
    "fun": "compute_magnetic_field_magnitude",
    "dim": 1,
    "R_derivs": [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 0, 1]],
}
data_index["|B|_t"] = {
    "label": "\\partial_{\\theta} |\\mathbf{B}|",
    "units": "T",
    "units_long": "Tesla",
    "description": "Magnitude of magnetic field, derivative wrt poloidal angle",
    "fun": "compute_magnetic_field_magnitude",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [1, 1, 0],
        [0, 1, 1],
    ],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 0, 1], [0, 2, 0], [0, 1, 1]],
}
data_index["|B|_z"] = {
    "label": "\\partial_{\\zeta} |\\mathbf{B}|",
    "units": "T",
    "units_long": "Tesla",
    "description": "Magnitude of magnetic field, derivative wrt toroidal angle",
    "fun": "compute_magnetic_field_magnitude",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 0, 2],
        [1, 0, 1],
        [0, 1, 1],
    ],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 2], [0, 1, 1]],
}
data_index["|B|_tt"] = {
    "label": "\\partial_{\\theta\\theta} |\\mathbf{B}|",
    "units": "T",
    "units_long": "Tesla",
    "description": "Magnitude of magnetic field, second derivative wrt poloidal angle",
    "fun": "compute_magnetic_field_magnitude",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [1, 1, 0],
        [0, 1, 1],
        [0, 3, 0],
        [1, 2, 0],
        [0, 2, 1],
    ],
    "L_derivs": [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [0, 1, 1],
        [0, 3, 0],
        [0, 2, 1],
    ],
}
data_index["|B|_zz"] = {
    "label": "\\partial_{\\zeta\\zeta} |\\mathbf{B}|",
    "units": "T",
    "units_long": "Tesla",
    "description": "Magnitude of magnetic field, second derivative wrt toroidal angle",
    "fun": "compute_magnetic_field_magnitude",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 0, 2],
        [1, 0, 1],
        [0, 1, 1],
        [0, 0, 3],
        [1, 0, 2],
        [0, 1, 2],
    ],
    "L_derivs": [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 0, 2],
        [0, 1, 1],
        [0, 0, 3],
        [0, 1, 2],
    ],
}
data_index["|B|_tz"] = {
    "label": "\\partial_{\\theta\\zeta} |\\mathbf{B}|",
    "units": "T",
    "units_long": "Tesla",
    "description": "Magnitude of magnetic field, derivative wrt poloidal and toroidal angles",
    "fun": "compute_magnetic_field_magnitude",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
        [0, 2, 1],
        [0, 1, 2],
        [1, 1, 1],
    ],
    "L_derivs": [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [0, 0, 2],
        [0, 1, 1],
        [0, 2, 1],
        [0, 1, 2],
    ],
}
# magnetic pressure gradient
data_index["grad(|B|^2)_rho"] = {
    "label": "(\\nabla B^{2})_{\\rho}",
    "units": "T^{2}",
    "units_long": "Tesla squared",
    "description": "Covariant radial component of magnetic pressure gradient",
    "fun": "compute_magnetic_pressure_gradient",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [2, 0, 0],
        [1, 1, 0],
        [1, 0, 1],
    ],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 0], [1, 0, 1]],
}
data_index["grad(|B|^2)_theta"] = {
    "label": "(\\nabla B^{2})_{\\theta}",
    "units": "T^{2}",
    "units_long": "Tesla squared",
    "description": "Covariant poloidal component of magnetic pressure gradient",
    "fun": "compute_magnetic_pressure_gradient",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [1, 1, 0],
        [0, 1, 1],
    ],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 0, 1], [0, 2, 0], [0, 1, 1]],
}
data_index["grad(|B|^2)_zeta"] = {
    "label": "(\\nabla B^{2})_{\\zeta}",
    "units": "T^{2}",
    "units_long": "Tesla squared",
    "description": "Covariant toroidal component of magnetic pressure gradient",
    "fun": "compute_magnetic_pressure_gradient",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 0, 2],
        [1, 0, 1],
        [0, 1, 1],
    ],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 2], [0, 1, 1]],
}
data_index["grad(|B|^2)"] = {
    "label": "\\nabla B^{2}",
    "units": "T^{2} \\cdot m^{-1}",
    "units_long": "Tesla squared / meters",
    "description": "Magnetic pressure gradient",
    "fun": "compute_magnetic_pressure_gradient",
    "dim": 3,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [2, 0, 0],
        [0, 2, 0],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
    ],
    "L_derivs": [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
    ],
}
data_index["|grad(|B|^2)|"] = {
    "label": "|\\nabla B^{2}|",
    "units": "T^{2} \\cdot m^{-1}",
    "units_long": "Tesla squared / meters",
    "description": "Magnitude of magnetic pressure gradient",
    "fun": "compute_magnetic_pressure_gradient",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [2, 0, 0],
        [0, 2, 0],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
    ],
    "L_derivs": [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
    ],
}
# magnetic tension
data_index["(curl(B)xB)_rho"] = {
    "label": "((\\nabla \\times \\mathbf{B}) \\times \\mathbf{B})_{\\rho}",
    "units": "T^{2}",
    "units_long": "Tesla squared",
    "description": "Covariant radial component of Lorentz force",
    "fun": "compute_magnetic_tension",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [2, 0, 0],
        [0, 2, 0],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
    ],
    "L_derivs": [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
    ],
}
data_index["(curl(B)xB)_theta"] = {
    "label": "((\\nabla \\times \\mathbf{B}) \\times \\mathbf{B})_{\\theta}",
    "units": "T^{2}",
    "units_long": "Tesla squared",
    "description": "Covariant poloidal component of Lorentz force",
    "fun": "compute_magnetic_tension",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
    ],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 0, 1], [0, 2, 0], [0, 0, 2], [0, 1, 1]],
}
data_index["(curl(B)xB)_zeta"] = {
    "label": "((\\nabla \\times \\mathbf{B}) \\times \\mathbf{B})_{\\zeta}",
    "units": "T^{2}",
    "units_long": "Tesla squared",
    "description": "Covariant toroidal component of Lorentz force",
    "fun": "compute_magnetic_tension",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
    ],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 0, 1], [0, 2, 0], [0, 0, 2], [0, 1, 1]],
}
data_index["curl(B)xB"] = {
    "label": "(\\nabla \\times \\mathbf{B}) \\times \\mathbf{B}",
    "units": "T^{2} \\cdot m^{-1}",
    "units_long": "Tesla squared / meters",
    "description": "Lorentz force",
    "fun": "compute_magnetic_tension",
    "dim": 3,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [2, 0, 0],
        [0, 2, 0],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
    ],
    "L_derivs": [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
    ],
}
data_index["(B*grad)B"] = {
    "label": "(\\mathbf{B} \\cdot \\nabla) \\mathbf{B}",
    "units": "T^{2} \\cdot m^{-1}",
    "units_long": "Tesla squared / meters",
    "description": "Magnetic tension",
    "fun": "compute_magnetic_tension",
    "dim": 3,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [2, 0, 0],
        [0, 2, 0],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
    ],
    "L_derivs": [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
    ],
}
data_index["((B*grad)B)_rho"] = {
    "label": "((\\mathbf{B} \\cdot \\nabla) \\mathbf{B})_{\\rho}",
    "units": "T^{2}",
    "units_long": "Tesla squared",
    "description": "Covariant radial component of magnetic tension",
    "fun": "compute_magnetic_tension",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [2, 0, 0],
        [0, 2, 0],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
    ],
    "L_derivs": [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
    ],
}
data_index["((B*grad)B)_theta"] = {
    "label": "((\\mathbf{B} \\cdot \\nabla) \\mathbf{B})_{\\theta}",
    "units": "T^{2}",
    "units_long": "Tesla squared",
    "description": "Covariant poloidal component of magnetic tension",
    "fun": "compute_magnetic_tension",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [2, 0, 0],
        [0, 2, 0],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
    ],
    "L_derivs": [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
    ],
}
data_index["((B*grad)B)_zeta"] = {
    "label": "((\\mathbf{B} \\cdot \\nabla) \\mathbf{B})_{\\zeta}",
    "units": "T^{2}",
    "units_long": "Tesla squared",
    "description": "Covariant toroidal component of magnetic tension",
    "fun": "compute_magnetic_tension",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [2, 0, 0],
        [0, 2, 0],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
    ],
    "L_derivs": [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
    ],
}
data_index["|(B*grad)B|"] = {
    "label": "|(\\mathbf{B} \\cdot \\nabla) \\mathbf{B}|",
    "units": "T^2 \\cdot m^{-1}",
    "units_long": "Tesla squared / meters",
    "description": "Magnitude of magnetic tension",
    "fun": "compute_magnetic_tension",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [2, 0, 0],
        [0, 2, 0],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
    ],
    "L_derivs": [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
    ],
}
# B dot grad(B)
data_index["B*grad(|B|)"] = {
    "label": "\\mathbf{B} \\cdot \\nabla B",
    "units": "T^2 \\cdot m^{-1}",
    "units_long": "Tesla squared / meters",
    "description": "",
    "fun": "compute_B_dot_gradB",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
    ],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 0, 1], [0, 2, 0], [0, 0, 2], [0, 1, 1]],
}
data_index["(B*grad(|B|))_t"] = {
    "label": "\\partial_{\\theta} (\\mathbf{B} \\cdot \\nabla B)",
    "units": "T^2 \\cdot m^{-1}",
    "units_long": "Tesla squared / meters",
    "description": "",
    "fun": "compute_B_dot_gradB",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
        [0, 3, 0],
        [1, 2, 0],
        [0, 2, 1],
        [0, 1, 2],
        [1, 1, 1],
    ],
    "L_derivs": [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [0, 0, 2],
        [0, 1, 1],
        [0, 3, 0],
        [0, 2, 1],
        [0, 1, 2],
    ],
}
data_index["(B*grad(|B|))_z"] = {
    "label": "\\partial_{\\zeta} (\\mathbf{B} \\cdot \\nabla B)",
    "units": "T^2 \\cdot m^{-1}",
    "units_long": "Tesla squared / meters",
    "description": "",
    "fun": "compute_B_dot_gradB",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
        [0, 0, 3],
        [1, 2, 0],
        [1, 0, 2],
        [0, 2, 1],
        [0, 1, 2],
        [1, 1, 1],
    ],
    "L_derivs": [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [0, 0, 2],
        [0, 1, 1],
        [0, 0, 3],
        [0, 2, 1],
        [0, 1, 2],
    ],
}
# contravarian current density
data_index["J^rho"] = {
    "label": "J^{\\rho}",
    "units": "A \\cdot m^{-3}",
    "units_long": "Amperes / cubic meter",
    "description": "Contravariant radial component of plasma current",
    "fun": "compute_contravariant_current_density",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
    ],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 0, 1], [0, 2, 0], [0, 0, 2], [0, 1, 1]],
}
data_index["J^theta"] = {
    "label": "J^{\\theta}",
    "units": "A \\cdot m^{-3}",
    "units_long": "Amperes / cubic meter",
    "description": "Contravariant poloidal component of plasma current",
    "fun": "compute_contravariant_current_density",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [2, 0, 0],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
    ],
    "L_derivs": [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
    ],
}
data_index["J^zeta"] = {
    "label": "J^{\\zeta}",
    "units": "A \\cdot m^{-3}",
    "units_long": "Amperes / cubic meter",
    "description": "Contravariant toroidal component of plasma current",
    "fun": "compute_contravariant_current_density",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [2, 0, 0],
        [0, 2, 0],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
    ],
    "L_derivs": [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
    ],
}
data_index["J"] = {
    "label": "\\mathbf{J}",
    "units": "A \\cdot m^{-2}",
    "units_long": "Amperes / square meter",
    "description": "Plasma current",
    "fun": "compute_contravariant_current_density",
    "dim": 3,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [2, 0, 0],
        [0, 2, 0],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
    ],
    "L_derivs": [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
    ],
}
data_index["J_parallel"] = {
    "label": "\\mathbf{J}_{\parallel}",
    "units": "A \\cdot m^{-2}",
    "units_long": "Amperes / square meter",
    "description": "Plasma current parallel to magnetic field",
    "fun": "compute_contravariant_current_density",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [2, 0, 0],
        [0, 2, 0],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
    ],
    "L_derivs": [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
    ],
}
data_index["div_J_perp"] = {
    "label": "\\nabla \\cdot \\mathbf{J}_{\perp}",
    "units": "A \\cdot m^{-3}",
    "units_long": "Amperes / cubic meter",
    "description": "Divergence of Plasma current perpendicular to magnetic field",
    "fun": "compute_force_error",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [2, 0, 0],
        [0, 2, 0],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
    ],
    "L_derivs": [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
    ],
}
# force error
data_index["F_rho"] = {
    "label": "F_{\\rho}",
    "units": "N \\cdot m^{-2}",
    "units_long": "Newtons / square meter",
    "description": "Covariant radial component of force balance error",
    "fun": "compute_force_error",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [2, 0, 0],
        [0, 2, 0],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
    ],
    "L_derivs": [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
    ],
}
data_index["F_theta"] = {
    "label": "F_{\\theta}",
    "units": "N \\cdot m^{-2}",
    "units_long": "Newtons / square meter",
    "description": "Covariant poloidal component of force balance error",
    "fun": "compute_force_error",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
    ],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 0, 1], [0, 2, 0], [0, 0, 2], [0, 1, 1]],
}
data_index["F_zeta"] = {
    "label": "F_{\\zeta}",
    "units": "N \\cdot m^{-2}",
    "units_long": "Newtons / square meter",
    "description": "Covariant toroidal component of force balance error",
    "fun": "compute_force_error",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
    ],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 0, 1], [0, 2, 0], [0, 0, 2], [0, 1, 1]],
}
data_index["F_beta"] = {
    "label": "F_{\\beta}",
    "units": "A",
    "units_long": "Amperes",
    "description": "Covariant helical component of force balance error",
    "fun": "compute_force_error",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
    ],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 0, 1], [0, 2, 0], [0, 0, 2], [0, 1, 1]],
}
data_index["F"] = {
    "label": "\\mathbf{J} \\times \\mathbf{B} - \\nabla p",
    "units": "N \\cdot m^{-3}",
    "units_long": "Newtons / cubic meter",
    "description": "Force balance error",
    "fun": "compute_force_error",
    "dim": 3,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [2, 0, 0],
        [0, 2, 0],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
    ],
    "L_derivs": [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
    ],
}
data_index["|F|"] = {
    "label": "|\\mathbf{J} \\times \\mathbf{B} - \\nabla p|",
    "units": "N \\cdot m^{-3}",
    "units_long": "Newtons / cubic meter",
    "description": "Magnitude of force balance error",
    "fun": "compute_force_error",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [2, 0, 0],
        [0, 2, 0],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
    ],
    "L_derivs": [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
    ],
}
data_index["|grad(p)|"] = {
    "label": "|\\nabla p|",
    "units": "N \\cdot m^{-3}",
    "units_long": "Newtons / cubic meter",
    "description": "Magnitude of pressure gradient",
    "fun": "compute_force_error",
    "dim": 1,
    "R_derivs": [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]],
    "L_derivs": [[0, 0, 0]],
}
data_index["|beta|"] = {
    "label": "|B^{\\theta} \\nabla \\zeta - B^{\\zeta} \\nabla \\theta|",
    "units": "T \\cdot m^{-2}",
    "units_long": "Tesla / square meter",
    "description": "Magnitude of helical basis vector",
    "fun": "compute_force_error",
    "dim": 1,
    "R_derivs": [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 0, 1]],
}
# quasi-symmetry
data_index["I"] = {
    "label": "I",
    "units": "T \\cdot m",
    "units_long": "Tesla * meters",
    "description": "Boozer toroidal current",
    "fun": "compute_quasisymmetry_error",
    "dim": 1,
    "R_derivs": [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 0, 1]],
}
data_index["G"] = {
    "label": "G",
    "units": "T \\cdot m",
    "units_long": "Tesla * meters",
    "description": "Boozer poloidal current",
    "fun": "compute_quasisymmetry_error",
    "dim": 1,
    "R_derivs": [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 0, 1]],
}
data_index["nu"] = {
    "label": "\\nu = \\zeta_{B} - \\zeta",
    "units": "rad",
    "units_long": "radians",
    "description": "Boozer toroidal stream function",
    "fun": "compute_boozer_coords",
    "dim": 1,
    "R_derivs": [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 0, 1]],
}
data_index["nu_t"] = {
    "label": "\\partial_{\\theta} \\nu",
    "units": "rad",
    "units_long": "radians",
    "description": "Boozer toroidal stream function, first poloidal derivative",
    "fun": "compute_boozer_coords",
    "dim": 1,
    "R_derivs": [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 0, 1]],
}
data_index["nu_z"] = {
    "label": "\\partial_{\\zeta} \\nu",
    "units": "rad",
    "units_long": "radians",
    "description": "Boozer toroidal stream function, first toroidal derivative",
    "fun": "compute_boozer_coords",
    "dim": 1,
    "R_derivs": [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 0, 1]],
}
data_index["theta_B"] = {
    "label": "\\theta_{B}",
    "units": "rad",
    "units_long": "radians",
    "description": "Boozer poloidal angular coordinate",
    "fun": "compute_boozer_coords",
    "dim": 1,
    "R_derivs": [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 0, 1]],
}
data_index["zeta_B"] = {
    "label": "\\zeta_{B}",
    "units": "rad",
    "units_long": "radians",
    "description": "Boozer toroidal angular coordinate",
    "fun": "compute_boozer_coords",
    "dim": 1,
    "R_derivs": [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 0, 1]],
}
data_index["sqrt(g)_B"] = {
    "label": "\\sqrt{g}_{B}",
    "units": "~",
    "units_long": "None",
    "description": "Jacobian determinant of Boozer coordinates",
    "fun": "compute_boozer_coords",
    "dim": 1,
    "R_derivs": [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 0, 1]],
}
data_index["|B|_mn"] = {
    "label": "B_{mn}^{Boozer}",
    "units": "T",
    "units_long": "Tesla",
    "description": "Boozer harmonics of magnetic field",
    "fun": "compute_boozer_coords",
    "dim": 1,
    "R_derivs": [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 0, 1]],
}
data_index["B modes"] = {
    "label": "Boozer modes",
    "units": "",
    "units_long": "None",
    "description": "Boozer harmonics",
    "fun": "compute_boozer_coords",
    "dim": 1,
}
data_index["f_C"] = {
    "label": "(\\mathbf{B} \\times \\nabla \\psi) \\cdot \\nabla B - "
    + "(M G + N I) / (M \\iota - N) \\mathbf{B} \\cdot \\nabla B",
    "units": "T^{3}",
    "units_long": "Tesla cubed",
    "description": "Two-term quasisymmetry metric",
    "fun": "compute_quasisymmetry_error",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
    ],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 0, 1], [0, 2, 0], [0, 0, 2], [0, 1, 1]],
}
data_index["f_T"] = {
    "label": "\\nabla \\psi \\times \\nabla B \\cdot \\nabla "
    + "(\\mathbf{B} \\cdot \\nabla B)",
    "units": "T^{4} \\cdot m^{-2}",
    "units_long": "Tesla quarted / square meters",
    "description": "Triple product quasisymmetry metric",
    "fun": "compute_quasisymmetry_error",
    "dim": 1,
    "R_derivs": [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [0, 0, 2],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
        [0, 3, 0],
        [0, 0, 3],
        [1, 2, 0],
        [1, 0, 2],
        [0, 2, 1],
        [0, 1, 2],
        [1, 1, 1],
    ],
    "L_derivs": [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 2, 0],
        [0, 0, 2],
        [0, 1, 1],
        [0, 3, 0],
        [0, 0, 3],
        [0, 2, 1],
        [0, 1, 2],
    ],
}
# energy
data_index["W"] = {
    "label": "W",
    "units": "J",
    "units_long": "Joules",
    "description": "Plasma total energy",
    "fun": "compute_energy",
    "dim": 0,
    "R_derivs": [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 0, 1]],
}
data_index["W_B"] = {
    "label": "W_B",
    "units": "J",
    "units_long": "Joules",
    "description": "Plasma magnetic energy",
    "fun": "compute_energy",
    "dim": 0,
    "R_derivs": [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]],
    "L_derivs": [[0, 0, 0], [0, 1, 0], [0, 0, 1]],
}
data_index["W_p"] = {
    "label": "W_p",
    "units": "J",
    "units_long": "Joules",
    "description": "Plasma thermodynamic energy",
    "fun": "compute_energy",
    "dim": 0,
    "R_derivs": [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]],
    "L_derivs": [[0, 0, 0]],
}
# geometry
data_index["V"] = {
    "label": "V",
    "units": "m^{3}",
    "units_long": "cubic meters",
    "description": "Volume",
    "fun": "compute_geometry",
    "dim": 0,
    "R_derivs": [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]],
}
data_index["A"] = {
    "label": "A",
    "units": "m^{2}",
    "units_long": "square meters",
    "description": "Cross-sectional area",
    "fun": "compute_geometry",
    "dim": 0,
    "R_derivs": [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]],
}
data_index["R0"] = {
    "label": "R_{0}",
    "units": "m",
    "units_long": "meters",
    "description": "Major radius",
    "fun": "compute_geometry",
    "dim": 0,
    "R_derivs": [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]],
}
data_index["a"] = {
    "label": "a",
    "units": "m",
    "units_long": "meters",
    "description": "Minor radius",
    "fun": "compute_geometry",
    "dim": 0,
    "R_derivs": [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]],
}
data_index["R0/a"] = {
    "label": "R_{0} / a",
    "units": "~",
    "units_long": "None",
    "description": "Aspect ratio",
    "fun": "compute_geometry",
    "dim": 0,
    "R_derivs": [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]],
}

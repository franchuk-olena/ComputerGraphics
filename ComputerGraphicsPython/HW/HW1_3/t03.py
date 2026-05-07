from HW1_3.main import *

cube = cube_points()

R_xyz = compose(
    rot_x(45),
    rot_y(30),
    rot_z(60)
)

R_zyx = compose(
    rot_z(60),
    rot_y(30),
    rot_x(45)
)

print("XYZ matrix:\n", R_xyz)
print("ZYX matrix:\n", R_zyx)

print_points("XYZ result", apply(cube, R_xyz))
print_points("ZYX result", apply(cube, R_zyx))
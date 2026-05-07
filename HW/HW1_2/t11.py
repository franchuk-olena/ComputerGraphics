from HW1_2.main import *

from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.model.Cube import Cube
from src.math.Vec4 import Vec4
from src.math.utils_matrix import decompose_affine_2

SHAPE_NAME = "object"

obj = Cube(alpha=0.2)
cube = cube_points()

R_ext = rot_z(60) @ rot_y(45) @ rot_x(30)
R_int = rot_x(60) @ rot_y(45) @ rot_z(30)

print("External matrix:\n", R_ext)
print("Internal matrix:\n", R_int)

ext_result = apply(cube, R_ext)
int_result = apply(cube, R_int)

print_points("External result (X30→Y45→Z60)", ext_result)
print_points("Internal result (X60→Y45→Z30)", int_result)

T1, R1, S1, axis, theta = decompose_affine_2(R_int)

rotation = RotationAnimation(
    end=theta,
    axis=axis,
    channel=SHAPE_NAME,
)

rotation_x = RotationAnimation(
    end=np.radians(30),
    axis=Vec4(1, 0, 0),
    channel=SHAPE_NAME,
)

rotation_y = RotationAnimation(
    end=np.radians(45),
    axis=Vec4(0, 1, 0),
    channel=SHAPE_NAME,
)

rotation_z = RotationAnimation(
    end=np.radians(60),
    axis=Vec4(0, 0, 1),
    channel=SHAPE_NAME,
)

animations = [
    rotation
    # x,
    # y,
    # z
]

run_animations(animations, "Animation Task 11", obj)
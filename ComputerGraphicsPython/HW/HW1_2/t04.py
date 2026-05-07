from HW1_2.main import *

from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.math.Vec4 import Vec4

SHAPE_NAME = "object"

obj = Cube(alpha=0.2)
cube = cube_points()

angle_z, angle_y, angle_x = 20, 35, 50

OX = Vec4(1, 0, 0)
OY = Vec4(0, 1, 0)
OZ = Vec4(0, 0, 1)

R = euler_zyx(angle_z, angle_y, angle_x)
T = translate(1, 3, -2)

rotated = apply(cube, R)
print_points("Rotate", rotated)

final_cube = apply(cube, compose(R, T))
print_points("Final", final_cube)

rotation_z = RotationAnimation(end=np.radians(angle_z), axis=OZ, channel=SHAPE_NAME)
rotation_y = RotationAnimation(end=np.radians(angle_y), axis=OY, channel=SHAPE_NAME)
rotation_x = RotationAnimation(end=np.radians(angle_x), axis=OX, channel=SHAPE_NAME)

translation = TranslationAnimation(end=Vec4(1, 3, -2), channel=SHAPE_NAME)

animations = [
    rotation_z,
    rotation_y,
    rotation_x,
    translation
]

run_animations(animations, "Animation Task 04", obj)
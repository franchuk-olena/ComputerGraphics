from HW1_2.main import *

from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.math.Vec4 import Vec4

SHAPE_NAME = "object"

obj = Cube(alpha=0.2)
cube = cube_points()

R1 = rot_axis(60, (0, 0, 1))
R2 = rot_axis(45, (1, 1, 1))
T = translate(4, -2, 1)

rot_z = apply(cube, R1)
print_points("Rotation Z", rot_z)

rot_12 = apply(cube, compose(R1, R2))
print_points("Rotation (1, 1, 1)", rot_12)

final_cube = apply(cube, compose(R1, R2, T))
print_points("Final", final_cube)

rotation_1 = RotationAnimation(end=np.radians(60), axis=Vec4(0, 0, 1), channel=SHAPE_NAME)
rotation_2 = RotationAnimation(end=np.radians(45), axis=Vec4(1, 1, 1), channel=SHAPE_NAME)

translation = TranslationAnimation(end=Vec4(4, -2, 1), channel=SHAPE_NAME)

animations = [
    rotation_1,
    rotation_2,
    translation
]

run_animations(animations, "Animation Task 03", obj)
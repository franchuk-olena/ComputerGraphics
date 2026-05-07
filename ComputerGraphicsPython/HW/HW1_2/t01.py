from HW1_2.main import *

from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.math.Vec4 import Vec4

SHAPE_NAME = "object"

obj = Cube(alpha=0.2)
cube = cube_points()

# Трансформації
R = rot_axis(45, (1, 1, 0))
T = translate(2, -1, 3)

rotated_cube = apply(cube, R)
print_points("After rotation", rotated_cube)

final_cube = apply(cube, compose(R, T))
print_points("Final", final_cube)

rotation_anim = RotationAnimation(end=np.radians(45), axis=Vec4(1, 1, 0), channel=SHAPE_NAME)
translation_anim = TranslationAnimation(end=Vec4(2, -1, 3), channel=SHAPE_NAME)

run_animations(
    [rotation_anim, translation_anim],"Animation Task 01", obj)
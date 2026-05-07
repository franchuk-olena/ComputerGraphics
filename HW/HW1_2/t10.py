from HW1_2.main import *

from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.engine.model.Cube import Cube
from src.math.Vec4 import Vec4

SHAPE_NAME = "object"

obj = Cube(alpha=0.2)
obj.pivot(1, 1, 1)
obj.show_pivot()

cube = cube_points()
pivot = (1, 1, 1)

S = around_point(scale(2, 1, 1), pivot)
R = around_point(rot_axis(45, (0, 1, 0)), pivot)
T = translate(-3, 4, 2)

scaled = apply(cube, S)
print_points("Scale", scaled)

scaled_rotated = apply(cube, compose(S, R))
print_points("Scale + Rotate", scaled_rotated)

final_cube = apply(cube, compose(S, R, T))
print_points("Final", final_cube)

scale_anim = ScaleAnimation(end=Vec4(2, 1, 1), channel=SHAPE_NAME)

rotation = RotationAnimation(
    end=np.radians(45),
    axis=Vec4(0, 1, 0),
    channel=SHAPE_NAME,
)

translation = TranslationAnimation(
    end=Vec4(-3, 4, 2),
    channel=SHAPE_NAME,
)

animations = [
    scale_anim,
    rotation,
    translation
]

run_animations(animations, "Animation Task 10", obj)
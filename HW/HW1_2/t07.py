from HW1_2.main import *

from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation
from src.engine.model.Cube import Cube
from src.math.Vec4 import Vec4

SHAPE_NAME = "object"

obj = Cube(alpha=0.2)
obj.pivot(1, 2, 3)
obj.show_pivot()

cube = cube_points()

pivot = (1, 2, 3)

S = around_point(scale(1, 1, 3), pivot)
R = around_point(rot_axis(30, (1, 0, 0)), pivot)

scaled = apply(cube, S)
print_points("Scale", scaled)

final_cube = apply(cube, compose(S, R))
print_points("Final", final_cube)

scaling = ScaleAnimation(end=Vec4(1, 1, 3), channel=SHAPE_NAME)

rotation = RotationAnimation(
    end=np.radians(30),
    axis=Vec4(1, 0, 0),
    channel=SHAPE_NAME,
)

animations = [
    scaling,
    rotation,
]

run_animations(animations, "Animation Task 07", obj)
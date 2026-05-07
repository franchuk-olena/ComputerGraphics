from HW1_2.main import *

from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.model.SimplePolygon import SimplePolygon
from src.math.Vec4 import Vec4

SHAPE_NAME = "object"

obj = SimplePolygon(
    1, 2, 0,
    4, 2, 0,
    4, 5, 0,
    1, 5, 0,
)

points = np.array([
    [1, 2, 0, 1],
    [4, 2, 0, 1],
    [4, 5, 0, 1],
    [1, 5, 0, 1]
])

obj.pivot(3, 3, 0)
obj.show_pivot()

pivot = (3, 3, 0)

R1 = around_point(rot_axis(60, (0, 1, 0)), pivot)
R2 = around_point(rot_axis(30, (1, 0, 0)), pivot)

rot_y = apply(points, R1)
print_points("Rotation Y", rot_y)

final_points = apply(points, compose(R1, R2))
print_points("Final", final_points)

rotation1 = RotationAnimation(
    end=np.radians(60),
    axis=Vec4(0, 1, 0),
    channel=SHAPE_NAME,
)

rotation2 = RotationAnimation(
    end=np.radians(30),
    axis=Vec4(1, 0, 0),
    channel=SHAPE_NAME,
)

animations = [
    rotation1,
    rotation2
]

run_animations(animations, "Animation Task 09", obj)
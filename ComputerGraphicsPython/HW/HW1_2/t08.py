from HW1_2.main import *

from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.engine.model.SimplePolygon import SimplePolygon
from src.math.Vec4 import Vec4

SHAPE_NAME = "object"

obj = SimplePolygon(
    1, 2, 3,
    4, 5, 6,
    7, 8, 9,
)

triangle_points = np.array([
    [1, 2, 3, 1],
    [4, 5, 6, 1],
    [7, 8, 9, 1],
])

obj.pivot(2, 3, 4)
obj.show_pivot()

pivot = (2, 3, 4)

R = around_point(rot_axis(90, (1, 1, 1)), pivot)
T = translate(0, -1, 2)

rotated = apply(triangle_points, R)
print_points("Rotation", rotated)

final_points = apply(triangle_points, compose(R, T))
print_points("Final", final_points)

rotation = RotationAnimation(
    end=np.radians(90),
    axis=Vec4(1, 1, 1),
    channel=SHAPE_NAME,
)

translation = TranslationAnimation(
    end=Vec4(0, -1, 2),
    channel=SHAPE_NAME,
)

animations = [
    rotation,
    translation
]

run_animations(animations, "Animation Task 8", obj)
from HW1_1.main import *

from src.engine.animation.ScaleAnimation import ScaleAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.math.Vec3 import vertex

SHAPE_NAME = "rect"

base_square = square()
pivot_point = [1, 1]

scaled_first = apply(base_square, scale_around(2, 1, pivot=pivot_point))
result_1 = apply(scaled_first, translate(3, -2))
print_points("Розтяг + переміщення", result_1)

translated_first = apply(base_square, translate(3, -2))
result_2 = apply(translated_first, scale_around(2, 1, pivot=pivot_point))
print_points("Переміщення + розтяг", result_2)

run_task([
    ScaleAnimation(end=(2, 1), frames=20, channel=SHAPE_NAME),
    TranslationAnimation(vertex(3, -2), frames=20, channel=SHAPE_NAME)
], "Animation Task", pivot=pivot_point)
from HW1_1.main import *

from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation

SHAPE_NAME = "rect"

base_square = square()
pivot_point = [0.5, 0.5]

rotated_square = apply(base_square, rotate_around(60, pivot=pivot_point))
print_points(f"Поворот на 60 навколо {pivot_point}", rotated_square)

run_task([
    RotationAnimation(end=60, frames=20, channel=SHAPE_NAME)
], "Animation Task", pivot=pivot_point)
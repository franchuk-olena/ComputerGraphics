from HW1_1.main import *

from src.engine.animation.ScaleAnimation import ScaleAnimation

SHAPE_NAME = "rect"

base_square = square()
pivot_point = [0.5, 0.5]

scaled_square = apply(base_square, scale_around(2, 3, pivot=pivot_point))
print_points(f"Розтяг x2 по X та x3 по Y відносно {pivot_point}", scaled_square)

run_task([
    ScaleAnimation(end=(2, 3), frames=20, channel=SHAPE_NAME)
], "Animation Task", pivot=pivot_point)
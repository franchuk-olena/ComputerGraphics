from HW1_1.main import *

from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation

SHAPE_NAME = "rect"

base_square = square()

scaled_square = apply(base_square, scale(2, 2))
print_points("Після розтягу", scaled_square)

rotated_square = apply(scaled_square, rotate(45))
print_points("Після повороту", rotated_square)

run_task([
    ScaleAnimation(end=(2, 2), frames=20, channel=SHAPE_NAME),
    RotationAnimation(end=30, frames=20, channel=SHAPE_NAME)
], "Animation Task")
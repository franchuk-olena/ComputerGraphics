from HW1_1.main import *

from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation

SHAPE_NAME = "rect"

base_square = square()

scaled_square = apply(base_square, scale(3, 3))
print_points("Після розтягу х3", scaled_square)

rotated_square = apply(scaled_square, rotate(60))
print_points("Після повороту на 60", rotated_square)

run_task([
    ScaleAnimation(end=(3, 3), frames=20, channel=SHAPE_NAME),
    RotationAnimation(end=60, frames=20, channel=SHAPE_NAME)
], "Animation Task")
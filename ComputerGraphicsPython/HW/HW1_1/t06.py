from HW1_1.main import *

from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation
from src.math.Vec3 import vertex

SHAPE_NAME = "rect"

base_square = square()

scaled_square = apply(base_square, scale(1, 3))
rotated_square = apply(scaled_square, rotate(60))
moved_square = apply(rotated_square, translate(2, 3))
print_points("Розтяг + поворот + перенесення", moved_square)

moved_square_2 = apply(base_square, translate(2, 3))
scaled_square_2 = apply(moved_square_2, scale(1, 3))
rotated_square_2 = apply(scaled_square_2, rotate(60))
print_points("Перенесення + розтяг + поворот", rotated_square_2)

run_task([
    ScaleAnimation(end=(1, 3), frames=20, channel=SHAPE_NAME),
    RotationAnimation(end=60, frames=20, channel=SHAPE_NAME),
    TranslationAnimation(end=vertex(2, 3), frames=20, channel=SHAPE_NAME)
], "Animation Task")
from HW1_1.main import *

from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.math.Vec3 import vertex

SHAPE_NAME = "rect"

base_square = square()

rotated_square = apply(base_square, rotate(90))
print_points("Після повороту", rotated_square)

moved_square = apply(rotated_square, translate(2, 3))
print_points("Після перенесення", moved_square)

run_task([
    RotationAnimation(end=90, frames=20, channel=SHAPE_NAME),
    TranslationAnimation(end=vertex(2, 3), frames=20, channel=SHAPE_NAME)
], "Animation Task")
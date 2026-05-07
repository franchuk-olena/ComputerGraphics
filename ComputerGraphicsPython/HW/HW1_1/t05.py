from HW1_1.main import *

from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation
from src.math.Vec3 import vertex

SHAPE_NAME = "rect"

base_square = square()

moved_square = apply(base_square, translate(1, -1))
print_points("Після переміщення (1, -1)", moved_square)

scaled_square = apply(moved_square, scale(2, 2))
print_points("Після розтягу х2", scaled_square)

run_task([
    TranslationAnimation(end=vertex(1, -1), frames=20, channel=SHAPE_NAME),
    ScaleAnimation(end=(2, 2), frames=20, channel=SHAPE_NAME)
], "Animation Task")
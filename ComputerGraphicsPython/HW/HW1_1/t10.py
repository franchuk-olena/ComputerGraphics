from HW1_1.main import *

from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation
from src.math.Vec3 import vertex

SHAPE_NAME = "rect"

base_square = square()
pivot = [0.5, 0.5]

# Варіант 1: розтяг -> поворот -> переміщення
scaled_1 = apply(base_square, scale_around(2, 2, pivot))
rotated_1 = apply(scaled_1, rotate_around(30, pivot=pivot))
translated_1 = apply(rotated_1, translate(1, -1))
print_points("Розтяг + поворот + переміщення", translated_1)

# Варіант 2: переміщення -> розтяг -> поворот
translated_2 = apply(base_square, translate(1, -1))
scaled_2 = apply(translated_2, scale_around(2, 2, pivot))
rotated_2 = apply(scaled_2, rotate_around(30, pivot=pivot))
print_points("Переміщення + розтяг + поворот", rotated_2)

# Варіант 3: розтяг -> переміщення -> поворот
scaled_3 = apply(base_square, scale_around(2, 2, pivot))
translated_3 = apply(scaled_3, translate(1, -1))
rotated_3 = apply(translated_3, rotate_around(30, pivot=pivot))
print_points("Розтяг + переміщення + поворот", rotated_3)

run_task([
    ScaleAnimation(end=(2, 2), frames=20, channel=SHAPE_NAME),
    RotationAnimation(end=30, frames=20, channel=SHAPE_NAME),
    TranslationAnimation(end=vertex(1, -1), frames=20, channel=SHAPE_NAME),
], "Animation Task")
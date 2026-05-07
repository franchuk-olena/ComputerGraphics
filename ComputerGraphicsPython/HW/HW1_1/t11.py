from HW1_1.main import *

from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation
from src.math.Vec3 import vertex

SHAPE_NAME = "rect"

TRS = np.array([
    [2.934, -0.416, 2.000],
    [0.624, 1.956, 3.400],
    [0.0, 0.0, 1.0]
])

transformed_vertices = np.array([
    [2, 3.4, 1],
    [4.9, 4, 1],
    [4.5, 6, 1],
    [1.6, 5.4, 1]
])

T_inv = inverse_matrix(TRS)
print("Матриця зворотної трансформації: \n", T_inv)

original_vertices = apply(transformed_vertices, T_inv)
print_points("Відновлені вершини (локальна система координат)", original_vertices)

translation, rotation, scale = decompose_trs(TRS)

run_task([
    TranslationAnimation(end=translation, frames=20, channel=SHAPE_NAME),
    RotationAnimation(end=rotation, frames=20, channel=SHAPE_NAME),
    ScaleAnimation(end=scale, frames=20, channel=SHAPE_NAME),
], "Animation Task")
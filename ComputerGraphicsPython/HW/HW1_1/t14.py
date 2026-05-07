from HW1_1.main import *

from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation
from src.math.Vec3 import vertex

SHAPE_NAME = "rect"

TRS = np.array([
    [1.732, -1, 5],
    [1, 1.732, -3],
    [0, 0, 1]
])

pivot = [1, 1]

translation, rotation, scale = decompose_trs_with_pivot(TRS, pivot)

run_task([
    TranslationAnimation(end=translation, frames=20, channel=SHAPE_NAME),
    RotationAnimation(end=rotation, frames=20, channel=SHAPE_NAME),
    ScaleAnimation(end=scale, frames=20, channel=SHAPE_NAME),
], "task 14", pivot=pivot)
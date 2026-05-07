from HW1_1.main import *

from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation
from src.math.Vec3 import vertex

SHAPE_NAME = "rect"

TRS = np.array([
    [0.866, 0.5, 4.000],
    [0.5, 0.866, 3.000],
    [0.0, 0.0, 1.0]
])

translation, rotation, scale = decompose_trs(TRS)

run_task([
    TranslationAnimation(end=translation, frames=20, channel=SHAPE_NAME),
    RotationAnimation(end=rotation, frames=20, channel=SHAPE_NAME),
    ScaleAnimation(end=scale, frames=20, channel=SHAPE_NAME),
], "Animation Task")
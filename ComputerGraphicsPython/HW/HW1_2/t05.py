from HW1_2.main import *
from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.engine.model.Tetrahedron import Tetrahedron
from src.math.Vec4 import Vec4
import numpy as np

obj = Tetrahedron(alpha=0.2)

tetra = tetra_points()

angle = np.random.uniform(10, 90)
axis = np.random.uniform(-1, 1, 3)
shift = np.random.uniform(-5, 5, 3)

R = rot_axis(angle, axis)
T = translate(*shift)

tr1 = apply(tetra, R)
print_points("Rotate", tr1)

tr2 = apply(tetra, compose(R, T))
print_points("Final", tr2)

rotation = RotationAnimation(
    end=np.radians(angle),
    axis=Vec4(*axis),
    channel="object",
)

translation = TranslationAnimation(
    end=Vec4(*shift),
    channel="object",
)

animations = [
    rotation,
    translation
]

run_animations(animations, "Animation Task 05", obj)
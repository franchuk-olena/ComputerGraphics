from HW1_2.main import *

from src.engine.model.Cube import Cube
from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.math.Vec4 import Vec4

SHAPE_NAME = "object"

obj = Cube(alpha=0.2)
obj.pivot(1, 1, 1)
obj.show_pivot()

cube = cube_points()
pivot = (1, 1, 1)

S = around_point(scale(2, 2, 2), pivot)
scaled = apply(cube, S)
print_points("Scale", scaled)

old_origin = np.array([[1, 1, 1, 1]])
new_origin = apply(old_origin, S)[0]
new_pivot = (new_origin[0], new_origin[1], new_origin[2])

R = around_point(rot_y(90), new_pivot)
rotated = apply(cube, compose(S, R))
print_points("Rotation", rotated)

T = translate(-3, 4, 2)
M = compose(S, R, T)

final = apply(cube, M)
print_points("Final", final)

def decompose(M):
    t = M[:3, 3]

    sx = np.linalg.norm(M[:3, 0])
    sy = np.linalg.norm(M[:3, 1])
    sz = np.linalg.norm(M[:3, 2])

    R = M[:3, :3] / np.array([sx, sy, sz])

    angle = np.arccos((np.trace(R) - 1) / 2)

    axis = np.array([
        R[2, 1] - R[1, 2],
        R[0, 2] - R[2, 0],
        R[1, 0] - R[0, 1]
    ]) / (2 * np.sin(angle))

    return t, (sx, sy, sz), axis, np.degrees(angle)

print(decompose(M))

scale_anim = ScaleAnimation(end=Vec4(2, 2, 2), channel=SHAPE_NAME)

rotation = RotationAnimation(
    end=np.radians(90),
    axis=Vec4(0, 1, 0),
    channel=SHAPE_NAME,
)

translation = TranslationAnimation(
    end=Vec4(-3, 4, 2),
    channel=SHAPE_NAME,
)

animations = [
    scale_anim,
    rotation,
    translation
]

run_animations(animations, "Animation Task 14", obj)
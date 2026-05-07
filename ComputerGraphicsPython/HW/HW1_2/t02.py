from HW1_2.main import *

from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.math.Vec4 import Vec4

SHAPE_NAME = "object"

obj = Cube(alpha=0.2)
cube = cube_points()

# Параметри кутів
angle_x, angle_y, angle_z = 30, 45, 60

# Оси
OX = Vec4(1, 0, 0)
OY = Vec4(0, 1, 0)
OZ = Vec4(0, 0, 1)

# Трансформації
S = scale(2, 0.5, 1)
R = euler_xyz(angle_x, angle_y, angle_z)
T = translate(-3, 2, 5)

# Перевірка трансформацій
scaled_cube = apply(cube, S)
print_points("Scale", scaled_cube)

scaled_rotated_cube = apply(cube, compose(S, R))
print_points("Scale + Rotate", scaled_rotated_cube)

final_cube = apply(cube, compose(S, R, T))
print_points("Final", final_cube)

# Анімації (компактно)
scaling = ScaleAnimation(end=Vec4(2, 0.5, 1), channel=SHAPE_NAME)

rotation_x = RotationAnimation(end=np.radians(angle_x), axis=OX, channel=SHAPE_NAME)
rotation_y = RotationAnimation(end=np.radians(angle_y), axis=OY, channel=SHAPE_NAME)
rotation_z = RotationAnimation(end=np.radians(angle_z), axis=OZ, channel=SHAPE_NAME)

translation = TranslationAnimation(end=Vec4(2, -1, 3), channel=SHAPE_NAME)

animations = [
    scaling,
    rotation_x,
    rotation_y,
    rotation_z,
    translation
]

run_animations(animations, "Animation Task 02", obj)
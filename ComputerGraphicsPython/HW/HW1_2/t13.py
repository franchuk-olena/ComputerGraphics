from HW1_2.main import *

import numpy as np
from src.math.utils_matrix import decompose_affine_2
from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.engine.model.Tetrahedron import Tetrahedron
from src.math.Vec4 import Vec4

SHAPE_NAME = "object"

obj = Tetrahedron(alpha=0.2)
tetra = tetra_points()

M = np.eye(4)

M = M @ rot_x(45)
step1 = apply(tetra, M)
print_points("Step 1 (rotate X local)", step1)

rotation_x = RotationAnimation(
    end=np.radians(45),
    axis=Vec4(1, 0, 0),
    channel=SHAPE_NAME,
)

local_y = M[:3, 1]
T_local = translate(local_y[0] * 2, local_y[1] * 2, local_y[2] * 2)

M = M @ T_local
step2 = apply(tetra, M)
print_points("Step 2 (move along local Y)", step2)

translation_vector = M[:3, 3]

translation = TranslationAnimation(
    end=Vec4(*translation_vector, 0),
    channel=SHAPE_NAME,
)

local_z = M[:3, 2]
R_local_z = rot_axis(30, local_z)

M = M @ R_local_z
step3 = apply(tetra, M)
print_points("Step 3 (rotate around local Z)", step3)

_, R_final, _, axis_final, angle_final = decompose_affine_2(R_local_z)

rotation_z = RotationAnimation(
    end=np.radians(30),
    axis=Vec4(*local_z, 0),
    channel=SHAPE_NAME,
)

animations = [
    rotation_x,
    translation,
    rotation_z
]

run_animations(animations, "Animation Task 13", obj)
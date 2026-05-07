from HW1_3.main import *

from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.engine.model.Cube import Cube
from src.math.Vec4 import Vec4

OBJ_NAME = "object"

cube_obj = Cube(alpha=0.2)

base_cube = cube_points()
print_points("Base cube", base_cube)

run_animations([
    RotationAnimation(end=np.radians(50), frames=20,
                      axis=Vec4(0, 0, 1), channel=OBJ_NAME),

    RotationAnimation(end=np.radians(35), frames=20,
                      axis=Vec4(0, 1, 0), channel=OBJ_NAME),

    RotationAnimation(end=np.radians(20), frames=20,
                      axis=Vec4(1, 0, 0), channel=OBJ_NAME),

    TranslationAnimation(end=Vec4(1, 3, -2), frames=20,
                         channel=OBJ_NAME)
], "Animation Task 02", cube_obj)
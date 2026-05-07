from HW1_3.main import *

from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.engine.model.Cube import Cube
from src.math.Vec4 import Vec4

OBJ_NAME = "object"

cube_obj = Cube(alpha=0.2)

base_cube = cube_points()
print_points("Base cube", base_cube)

run_animations([
    ScaleAnimation(end=Vec4(2, 0.5, 1), frames=20, channel=OBJ_NAME),

    RotationAnimation(end=np.radians(30), frames=20,
                      axis=Vec4(1, 0, 0), channel=OBJ_NAME),

    RotationAnimation(end=np.radians(45), frames=20,
                      axis=Vec4(0, 1, 0), channel=OBJ_NAME),

    RotationAnimation(end=np.radians(60), frames=20,
                      axis=Vec4(0, 0, 1), channel=OBJ_NAME),

    TranslationAnimation(end=Vec4(-3, 2, 5), frames=20, channel=OBJ_NAME)
], "Animation Task 01", cube_obj)
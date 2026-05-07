import numpy as np
from HW1_3.main import *


def extract_euler(R):
    if abs(R[2, 0]) != 1:
        y = -np.arcsin(R[2, 0])
        x = np.arctan2(R[2, 1], R[2, 2])
        z = np.arctan2(R[1, 0], R[0, 0])

    # gimbal lock case
    else:
        z = 0
        if R[2, 0] == -1:
            y = np.pi / 2
            x = z + np.arctan2(R[0, 1], R[0, 2])
        else:
            y = -np.pi / 2
            x = -z + np.arctan2(-R[0, 1], -R[0, 2])

    return np.degrees([x, y, z])


R = rot_y(90)[:3, :3]

angles = extract_euler(R)

print("Euler angles (deg):", angles)
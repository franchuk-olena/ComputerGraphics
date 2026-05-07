import numpy as np
import math

def run():
    R = np.array([
        [0, -1, 0],
        [1,  0, 0],
        [0,  0, 1]
    ])

    trace = np.trace(R)
    w = math.sqrt(1 + trace) / 2
    x = (R[2,1] - R[1,2]) / (4*w)
    y = (R[0,2] - R[2,0]) / (4*w)
    z = (R[1,0] - R[0,1]) / (4*w)

    q = [w, x, y, z]

    print("Quaternion:", q)
    return q
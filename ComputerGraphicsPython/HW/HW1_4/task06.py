import numpy as np
import math

def run():
    M = np.array([
        [0, -2, 0, 1],
        [0,  0, 1, 5],
        [0,  0, 1.5, 3],
        [0,  0, 0, 1]
    ])

    T = M[:3, 3]

    A = M[:3, :3]

    sx = np.linalg.norm(A[:,0])
    sy = np.linalg.norm(A[:,1])
    sz = np.linalg.norm(A[:,2])

    R = A.copy()
    R[:,0] /= sx
    R[:,1] /= sy
    R[:,2] /= sz

    trace = np.trace(R)
    w = math.sqrt(1 + trace) / 2
    x = (R[2,1] - R[1,2]) / (4*w)
    y = (R[0,2] - R[2,0]) / (4*w)
    z = (R[1,0] - R[0,1]) / (4*w)

    q = [w, x, y, z]

    print("T:", T)
    print("Scale:", sx, sy, sz)
    print("Quaternion:", q)

    return T, q
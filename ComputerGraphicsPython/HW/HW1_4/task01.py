from quaternion import *

def run():
    axis = [1, 1, 1]
    q = quaternion_from_axis_angle(axis, 60)

    print("Q:", q)
    print("Norm:", quaternion_norm(q))
    print("Matrix:\n", quaternion_to_matrix(q))

    return q
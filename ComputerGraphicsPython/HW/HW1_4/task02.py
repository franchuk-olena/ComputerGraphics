from quaternion import *

def run():
    p = [1, 0, 0]
    q = quaternion_from_axis_angle([0, 0, 1], 90)

    res = rotate_vector(q, p)

    print("Result:", res)
    return res
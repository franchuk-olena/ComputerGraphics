from quaternion import *

def run():
    qz = quaternion_from_axis_angle([0,0,1], 20)
    qy = quaternion_from_axis_angle([0,1,0], 90)
    qx = quaternion_from_axis_angle([1,0,0], 50)

    q = quaternion_mul(qz, quaternion_mul(qy, qx))

    print("Euler quaternion:", q)
    print("Norm:", quaternion_norm(q))

    return q
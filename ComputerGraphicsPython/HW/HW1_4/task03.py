from quaternion import *

def run():
    q1 = quaternion_from_axis_angle([1, 0, 0], 45)
    q2 = quaternion_from_axis_angle([0, 1, 0], 30)

    q_total = quaternion_mul(q2, q1)

    tetra = [
        [0,0,0],
        [1,0,0],
        [0,1,0],
        [0,0,1]
    ]

    rotated = [rotate_vector(q_total, v) for v in tetra]

    print("Rotated tetrahedron:")
    for v in rotated:
        print(v)

    return q_total
import math
import numpy as np


def normalize(v):
    n = math.sqrt(sum(x*x for x in v))
    return [x / n for x in v]


def quaternion_from_axis_angle(axis, theta_deg):
    theta = math.radians(theta_deg)
    half = theta / 2

    axis = normalize(axis)

    return [
        math.cos(half),
        axis[0] * math.sin(half),
        axis[1] * math.sin(half),
        axis[2] * math.sin(half)
    ]


def quaternion_mul(q1, q2):
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2

    return [
        w1*w2 - x1*x2 - y1*y2 - z1*z2,
        w1*x2 + x1*w2 + y1*z2 - z1*y2,
        w1*y2 - x1*z2 + y1*w2 + z1*x2,
        w1*z2 + x1*y2 - y1*x2 + z1*w2
    ]


def quaternion_inverse(q):
    w, x, y, z = q
    n = w*w + x*x + y*y + z*z
    return [w/n, -x/n, -y/n, -z/n]


def quaternion_norm(q):
    return math.sqrt(sum(x*x for x in q))


def quaternion_to_matrix(q):
    w, x, y, z = q

    return np.array([
        [1 - 2*(y*y + z*z), 2*(x*y - w*z),     2*(x*z + w*y)],
        [2*(x*y + w*z),     1 - 2*(x*x + z*z), 2*(y*z - w*x)],
        [2*(x*z - w*y),     2*(y*z + w*x),     1 - 2*(x*x + y*y)]
    ])


def rotate_vector(q, v):
    vq = [0] + v
    q_inv = quaternion_inverse(q)

    tmp = quaternion_mul(q, vq)
    res = quaternion_mul(tmp, q_inv)

    return res[1:]
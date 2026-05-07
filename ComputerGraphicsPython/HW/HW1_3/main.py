import numpy as np

from src.engine.scene.AnimatedScene import AnimatedScene
from src.engine.model.Cube import Cube


def create_scene(title, model, key="object",
                 image_size=(8, 8),
                 coordinate_rect=(-2, -2, -2, 3, 3, 3)):

    scene = AnimatedScene(
        title=title,
        image_size=image_size,
        coordinate_rect=coordinate_rect,
    )

    scene[key] = model
    return scene


def run_animations(animations, title, model, key="object"):
    scene = create_scene(title, model, key)
    scene.add_animations(*animations)
    scene.show()


def cube_points():
    return np.array([
        [0, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 1, 0, 1],
        [0, 1, 0, 1],
        [0, 0, 1, 1],
        [1, 0, 1, 1],
        [1, 1, 1, 1],
        [0, 1, 1, 1]
    ])


def tetra_points():
    return np.array([
        [0,0,0,1],
        [1,0,0,1],
        [0,1,0,1],
        [0,0,1,1]
    ])


def rot_x(deg):
    a = np.radians(deg)
    return np.array([
        [1,0,0,0],
        [0,np.cos(a),-np.sin(a),0],
        [0,np.sin(a), np.cos(a),0],
        [0,0,0,1]
    ])


def rot_y(deg):
    a = np.radians(deg)
    return np.array([
        [np.cos(a),0,np.sin(a),0],
        [0,1,0,0],
        [-np.sin(a),0,np.cos(a),0],
        [0,0,0,1]
    ])


def rot_z(deg):
    a = np.radians(deg)
    return np.array([
        [np.cos(a),-np.sin(a),0,0],
        [np.sin(a), np.cos(a),0,0],
        [0,0,1,0],
        [0,0,0,1]
    ])


def rot_axis(deg, axis):
    a = np.radians(deg)
    x, y, z = np.array(axis) / np.linalg.norm(axis)

    c, s = np.cos(a), np.sin(a)

    R = np.array([
        [c+(1-c)*x*x, (1-c)*x*y - s*z, (1-c)*x*z + s*y],
        [(1-c)*y*x + s*z, c+(1-c)*y*y, (1-c)*y*z - s*x],
        [(1-c)*z*x - s*y, (1-c)*z*y + s*x, c+(1-c)*z*z]
    ])

    M = np.eye(4)
    M[:3,:3] = R
    return M


def translate(dx, dy, dz):
    return np.array([
        [1,0,0,dx],
        [0,1,0,dy],
        [0,0,1,dz],
        [0,0,0,1]
    ])


def scale(sx, sy, sz):
    return np.array([
        [sx,0,0,0],
        [0,sy,0,0],
        [0,0,sz,0],
        [0,0,0,1]
    ])


def compose(*matrices):
    M = np.eye(4)
    for m in matrices[::-1]:
        M = M @ m
    return M


def apply(points, matrix):
    return points @ matrix.T


def euler_xyz(ax, ay, az):
    return compose(rot_x(ax), rot_y(ay), rot_z(az))


def euler_zyx(ax, ay, az):
    return compose(rot_z(az), rot_y(ay), rot_x(ax))


def around_point(M, pivot):
    px, py, pz = pivot
    return compose(
        translate(-px, -py, -pz),
        M,
        translate(px, py, pz)
    )


def print_points(label, pts):
    print(f"\n{label}:")
    for p in pts:
        print(f"({p[0]:.3f}, {p[1]:.3f}, {p[2]:.3f})")
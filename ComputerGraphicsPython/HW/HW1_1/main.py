import numpy as np

from src.engine.scene.AnimatedScene import AnimatedScene
from src.engine.model.Polygon import Polygon

SHAPE_NAME = "rect"


class AnimatedSceneSample(AnimatedScene):
        def __init__(self, pivot, **kwargs):
            super().__init__(**kwargs)

            polygon = Polygon(
                0, 0,
                1, 0,
                1, 1,
                0, 1
            )


            polygon["color"] = "blue"
            polygon["line_style"] = "-"
            polygon.pivot(pivot[0], pivot[1])
            polygon.show_pivot()

            self[SHAPE_NAME] = polygon


def square():
    return np.array([
        [0, 0, 1],
        [1, 0, 1],
        [1, 1, 1],
        [0, 1, 1]
    ])


def rotate(angle_deg):
    a = np.radians(angle_deg)
    return np.array([
        [np.cos(a), -np.sin(a), 0],
        [np.sin(a),  np.cos(a), 0],
        [0, 0, 1]
    ])


def translate(dx, dy):
    return np.array([
        [1, 0, dx],
        [0, 1, dy],
        [0, 0, 1]
    ])


def scale(sx, sy):
    return np.array([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ])


def apply(points, matrix):
    return points @ matrix.T


def print_points(name, pts):
    print(f"\n{name}:")
    for p in pts:
        print(f"({p[0]:.3f}, {p[1]:.3f})")


def rotate_around(angle_deg, pivot):
    return translate(pivot[0], pivot[1]) @ rotate(angle_deg) @ translate(-pivot[0], -pivot[1])


def scale_around(sx, sy, pivot):
    return translate(pivot[0], pivot[1]) @ scale(sx, sy) @ translate(-pivot[0], -pivot[1])


def inverse_matrix(matrix):
    return np.linalg.inv(matrix)


def decompose_trs(matrix):

    translation = matrix[0:2, 2]
    rs_matrix = matrix[0:2, 0:2]

    sx = np.linalg.norm(rs_matrix[:, 0])
    sy = np.linalg.norm(rs_matrix[:, 1])

    rotation_matrix = rs_matrix.copy()
    rotation_matrix[:, 0] /= sx
    rotation_matrix[:, 1] /= sy

    det = np.linalg.det(rotation_matrix)
    if abs(det - 1) > 1e-6:
        print(f"Визначник матриці повороту = {det:.3f} (має бути 1)")

    angle = np.arctan2(rotation_matrix[1, 0], rotation_matrix[0, 0])
    angle_deg = np.degrees(angle)

    return translation, angle_deg, (sx, sy)


def decompose_trs_with_pivot(matrix, pivot):

    to_pivot = translate(-pivot[0], -pivot[1])
    from_pivot = translate(pivot[0], pivot[1])

    T_no_pivot = to_pivot @ matrix @ from_pivot

    translation, angle, scales = decompose_trs(T_no_pivot)

    R = rotate(angle)
    pivot_correction = np.array(pivot) - (R @ np.array([pivot[0], pivot[1], 0]))[0:2]
    translation_global = translation + pivot_correction

    return translation_global, angle, scales


def run_task(transformations, title, pivot=[0,0]):
    scene = AnimatedSceneSample(pivot=pivot,
        image_size=(7, 7),
        coordinate_rect=(-1, -1, 6, 6),
        title=title,
        base_axis_show=False,
        axis_show=True,
        axis_color=("red", "green"),
        axis_line_width=2.0,
        axis_line_style="--",
        keep_aspect_ratio=True, )



    for t in transformations:
        scene.add_animation(t)

    scene.show()
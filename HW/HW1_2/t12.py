from HW1_2.main import *

M = compose(
    scale(2, 3, 1),
    rot_axis(45, (1, 1, 0)),
    translate(3, -2, 5)
)

print("Matrix:\n", M)

translation = M[:3, 3]
print("Translation:", translation)

sx = np.linalg.norm(M[:3, 0])
sy = np.linalg.norm(M[:3, 1])
sz = np.linalg.norm(M[:3, 2])

scale_vec = (sx, sy, sz)
print("Scale:", scale_vec)

R = M[:3, :3] / np.array([sx, sy, sz])

print("Rotation:\n", R)

angle = np.arccos((np.trace(R) - 1) / 2)
print("Angle:", np.degrees(angle))

axis = np.array([
    R[2, 1] - R[1, 2],
    R[0, 2] - R[2, 0],
    R[1, 0] - R[0, 1]
]) / (2 * np.sin(angle))

print("Axis:", axis)
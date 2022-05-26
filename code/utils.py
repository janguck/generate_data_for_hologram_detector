import numpy as np
import numpy.linalg as la

color_pallete = [[255, 0, 0], [0, 255, 0], [0, 0, 255], [0, 255, 255], [255, 255, 0], [255, 0, 255]]


def angle(v1, v2):

    c = np.dot(v1, v2)
    s = la.norm(np.cross(v1, v2))
    return np.arctan2(s, c)


def closest(points, x, y, n=10):

    dist = (points[:, 0] - x) ** 2 + (points[:, 1] - y) ** 2
    return points[dist.argsort()[:n]]

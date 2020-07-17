import math

from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QPolygonF


def regular_polygon(n_sides, x, y, radius, theta_0):
    polygon = QPolygonF()
    d_theta = 360 / n_sides
    for i in range(n_sides):
        theta_i = theta_0 + i * d_theta
        vertex_x = x + radius * math.cos(math.radians(theta_i))
        vertex_y = y + radius * math.sin(math.radians(theta_i))
        polygon.append(QPointF(vertex_x, vertex_y))
    return polygon


def rotated_rectangle(x, y, w, h, theta_0):
    polygon = QPolygonF()
    dx_w = math.cos(math.radians(theta_0)) * w / 2
    dy_w = math.sin(math.radians(theta_0)) * w / 2
    dx_h = math.sin(math.radians(theta_0)) * h / 2
    dy_h = math.cos(math.radians(theta_0)) * h / 2
    polygon.append(QPointF(x + dx_w - dx_h, y - dy_w - dy_h))
    polygon.append(QPointF(x - dx_w - dx_h, y + dy_w - dy_h))
    polygon.append(QPointF(x - dx_w + dx_h, y + dy_w + dy_h))
    polygon.append(QPointF(x + dx_w + dx_h, y - dy_w + dy_h))
    return polygon

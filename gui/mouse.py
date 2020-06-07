import numpy as np

from gui.drawing.vertex import vertex_center, VERTEX_RADIUS


def moused_vertices(window, vertex_grid):
    colliding_vertices = []
    for vertex in vertex_grid.vertices:
        dist = np.linalg.norm(np.array([window.mouse_x, window.mouse_y]) - np.array(vertex_center(window, vertex)))
        if dist < VERTEX_RADIUS:
            colliding_vertices.append(vertex)
    return colliding_vertices

import math
import sys

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtGui import QPen
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow


PEN_SIZE = 5
HEX_RADIUS = 100
HEX_ROTATION = 90
HEX_DX = math.sqrt(3) * HEX_RADIUS
HEX_DY = 1.5 * HEX_RADIUS
HEX_PHASE = HEX_DX / 2
HONEYCOMB_RADIUS = 2


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Semaphores of Catan")
        self.showMaximized()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, PEN_SIZE, Qt.SolidLine))
        X_0 = self.width()/2
        Y_0 = self.height()/2

        for honeycomb_row in range(-HONEYCOMB_RADIUS, HONEYCOMB_RADIUS + 1):
            if honeycomb_row % 2 == 0:
                for honeycomb_col in range(-HONEYCOMB_RADIUS + abs(honeycomb_row) // 2, HONEYCOMB_RADIUS - abs(honeycomb_row) // 2 + 1):
                    painter.drawPolygon(self.make_polygon(6, X_0 + honeycomb_col * HEX_DX, Y_0 + honeycomb_row * HEX_DY, HEX_RADIUS, HEX_ROTATION))
            else:
                for honeycomb_col in range(-HONEYCOMB_RADIUS + abs(honeycomb_row) // 2, HONEYCOMB_RADIUS - abs(honeycomb_row) // 2):
                    painter.drawPolygon(self.make_polygon(6, X_0 + HEX_PHASE + honeycomb_col * HEX_DX, Y_0 + honeycomb_row * HEX_DY, HEX_RADIUS, HEX_ROTATION))

    def make_polygon(self, num_sides, center_x, center_y, radius, theta_0):
        polygon = QtGui.QPolygonF()
        d_theta = 360 / num_sides
        for i in range(num_sides):
            theta_i = theta_0 + i * d_theta
            vertex_x = center_x + radius * math.cos(math.radians(theta_i))
            vertex_y = center_y + radius * math.sin(math.radians(theta_i))
            polygon.append(QtCore.QPointF(vertex_x, vertex_y))
        return polygon


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())

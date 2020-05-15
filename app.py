import math
import sys

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QPainter
from PyQt5.QtGui import QPen
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from board import Board
from game import Game


PEN_SIZE = 5
TILE_RADIUS = 100
TILE_ROTATION = 90

DX_DHEXX = math.sqrt(3) * TILE_RADIUS
DY_DHEXX = 0
DX_DHEXY = DX_DHEXX / 2
DY_DHEXY = 1.5 * TILE_RADIUS


class Window(QMainWindow):

    def __init__(self, game):
        super().__init__()
        self.setWindowTitle("Semaphores of Catan")
        self.showMaximized()
        self.game = game
        self.X0 = self.width() / 2
        self.Y0 = self.height() / 2

    def get_xy(self, tile):
        x = self.X0 + DX_DHEXX * tile.hex_x + DX_DHEXY * tile.hex_y
        y = self.Y0 + DY_DHEXX * tile.hex_x - DY_DHEXY * tile.hex_y
        return (x, y)

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.setBrush(QBrush(QColor(0, 158, 220)))
        painter.drawRect(0, 0, self.width(), self.height())

        painter.setPen(QPen(Qt.black, PEN_SIZE, Qt.SolidLine))
        painter.setFont(QFont("Monospaced", 55))
        

        NUMBER_WIDTH, NUMBER_HEIGHT = [.75 * TILE_RADIUS] * 2

        

        for row in self.game.board.grid:
            for tile in row:
                if tile:
                    x, y = self.get_xy(tile)
                    painter.setBrush(QBrush(QColor(*tile.RGB)))
                    painter.drawPolygon(self.make_polygon(6, x, y, TILE_RADIUS, TILE_ROTATION))
                    if tile.number is not None:
                        painter.drawEllipse(x - NUMBER_WIDTH / 2, y - NUMBER_HEIGHT / 2, NUMBER_WIDTH, NUMBER_HEIGHT)
                        painter.drawText(x - NUMBER_WIDTH / 2, y - NUMBER_HEIGHT / 2, NUMBER_WIDTH, NUMBER_HEIGHT, Qt.AlignCenter, str(tile.number))

        # painter.drawPolygon(self.make_settlement(self.X0, self.Y0, 40))


        for vertex in self.game.board.vertices:

            if not vertex.building:
                continue

            x, y = 0, 0
            if vertex.n_tile:
                tile_x, tile_y = self.get_xy(vertex.n_tile)
                x = tile_x
                y = tile_y + TILE_RADIUS
            elif vertex.sw_tile:
                tile_x, tile_y = self.get_xy(vertex.sw_tile)
                x = tile_x + math.sqrt(3) * TILE_RADIUS / 2
                y = tile_y - TILE_RADIUS / 2
            elif vertex.se_tile:
                tile_x, tile_y = self.get_xy(vertex.se_tile)
                x = tile_x - math.sqrt(3) * TILE_RADIUS / 2
                y = tile_y - TILE_RADIUS / 2
            elif vertex.s_tile:
                tile_x, tile_y = self.get_xy(vertex.s_tile)
                x = tile_x
                y = tile_y - TILE_RADIUS
            # elif vertex.nw_tile:
            #     pass
            # elif vertex.ne_tile:
            #     pass
            else:
                pass
                # raise ValueError("Invalid Vertex")

            if vertex.building:
                painter.drawPolygon(self.make_settlement(x, y, 40))

            # painter.drawEllipse(x - 10, y - 10, 20, 20)
            # print(self.game.board.vertices[-1])

    def mousePressEvent(self, e):
        self.game = Game()
        self.update()

    def make_polygon(self, num_sides, center_x, center_y, radius, theta_0):
        polygon = QtGui.QPolygonF()
        d_theta = 360 / num_sides
        for i in range(num_sides):
            theta_i = theta_0 + i * d_theta
            vertex_x = center_x + radius * math.cos(math.radians(theta_i))
            vertex_y = center_y + radius * math.sin(math.radians(theta_i))
            polygon.append(QtCore.QPointF(vertex_x, vertex_y))
        return polygon

    def make_settlement(self, center_x, center_y, side_len):
        polygon = QtGui.QPolygonF()
        polygon.append(QtCore.QPointF(center_x + side_len / 2, center_y + side_len / 2))
        polygon.append(QtCore.QPointF(center_x + side_len / 2, center_y - side_len / 5))
        polygon.append(QtCore.QPointF(center_x, center_y - 7 * side_len / 10))
        polygon.append(QtCore.QPointF(center_x - side_len / 2, center_y - side_len / 5))
        polygon.append(QtCore.QPointF(center_x - side_len / 2, center_y + side_len / 2))
        return polygon


if __name__ == "__main__":
    App = QApplication(sys.argv)
    game = Game()
    window = Window(game)
    sys.exit(App.exec())

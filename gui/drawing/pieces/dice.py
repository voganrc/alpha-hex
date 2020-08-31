import math

from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPainter, QPen, QBrush

from game.indexing.hex import HexGrid
from gui.drawing.indexing.hex import HexDrawingMixin


class DiceDrawingMixin:
    DIE_WIDTH = 90
    DIE_OFFSET = (DIE_WIDTH / 10) + (DIE_WIDTH / 2)

    def get_die_centers(self):
        island_width = HexGrid.N_ROWS * math.sqrt(3) * HexDrawingMixin.HEX_RADIUS
        side_water_width = (self.frameGeometry().width() - island_width) / 2

        center_x = self.center[0] + (island_width / 2) + (side_water_width / 2)
        center_y = self.center[1]

        center_x1 = center_x - DiceDrawingMixin.DIE_OFFSET
        center_x2 = center_x + DiceDrawingMixin.DIE_OFFSET

        return ((center_x1, center_y), (center_x2, center_y))

    def get_die_polygons(self, dice):
        (center_x1, center_y), (center_x2, center_y) = self.get_die_centers()
        die_1 = QRect(
            center_x1 - DiceDrawingMixin.DIE_WIDTH / 2,
            center_y - DiceDrawingMixin.DIE_WIDTH / 2,
            DiceDrawingMixin.DIE_WIDTH,
            DiceDrawingMixin.DIE_WIDTH,
        )
        pips_1 = self._get_pips(center_x1, center_y, DiceDrawingMixin.DIE_WIDTH, dice.first_die)
        die_2 = QRect(
            center_x2 - DiceDrawingMixin.DIE_WIDTH / 2,
            center_y - DiceDrawingMixin.DIE_WIDTH / 2,
            DiceDrawingMixin.DIE_WIDTH,
            DiceDrawingMixin.DIE_WIDTH,
        )
        pips_2 = self._get_pips(center_x2, center_y, DiceDrawingMixin.DIE_WIDTH, dice.second_die)
        return (die_1, pips_1), (die_2, pips_2)

    def draw_dice(self, dice):
        painter = QPainter(self)
        (die_1, pips_1), (die_2, pips_2) = self.get_die_polygons(dice)

        painter.setPen(QPen(Qt.black, 3, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.white))
        painter.drawRect(die_1)
        painter.drawRect(die_2)

        painter.setBrush(QBrush(Qt.black))
        for ellipse_args in pips_1 + pips_2:
            painter.drawEllipse(*ellipse_args)

    def _get_pips(self, center_x, center_y, die_width, die_number):
        pip_diameter = die_width / 6
        pen_offset = pip_diameter / 2
        adjusted_x = center_x - pen_offset
        adjusted_y = center_y - pen_offset
        if die_number == 1:
            return [
                (adjusted_x, adjusted_y, pip_diameter, pip_diameter),
            ]
        elif die_number == 2:
            return [
                (adjusted_x - die_width / 4, adjusted_y + die_width / 4, pip_diameter, pip_diameter),
                (adjusted_x + die_width / 4, adjusted_y - die_width / 4, pip_diameter, pip_diameter),
            ]
        elif die_number == 3:
            return [
                (adjusted_x - die_width / 4, adjusted_y + die_width / 4, pip_diameter, pip_diameter),
                (adjusted_x, adjusted_y, pip_diameter, pip_diameter),
                (adjusted_x + die_width / 4, adjusted_y - die_width / 4, pip_diameter, pip_diameter),
            ]
        elif die_number == 4:
            return [
                (adjusted_x - die_width / 4, adjusted_y - die_width / 4, pip_diameter, pip_diameter),
                (adjusted_x + die_width / 4, adjusted_y - die_width / 4, pip_diameter, pip_diameter),
                (adjusted_x - die_width / 4, adjusted_y + die_width / 4, pip_diameter, pip_diameter),
                (adjusted_x + die_width / 4, adjusted_y + die_width / 4, pip_diameter, pip_diameter),

            ]
        elif die_number == 5:
            return [
                (adjusted_x - die_width / 4, adjusted_y - die_width / 4, pip_diameter, pip_diameter),
                (adjusted_x + die_width / 4, adjusted_y - die_width / 4, pip_diameter, pip_diameter),
                (adjusted_x, adjusted_y, pip_diameter, pip_diameter),
                (adjusted_x - die_width / 4, adjusted_y + die_width / 4, pip_diameter, pip_diameter),
                (adjusted_x + die_width / 4, adjusted_y + die_width / 4, pip_diameter, pip_diameter),
            ]
        elif die_number == 6:
            return [
                (adjusted_x - die_width / 4, adjusted_y - die_width / 4, pip_diameter, pip_diameter),
                (adjusted_x + die_width / 4, adjusted_y - die_width / 4, pip_diameter, pip_diameter),
                (adjusted_x - die_width / 4, adjusted_y, pip_diameter, pip_diameter),
                (adjusted_x + die_width / 4, adjusted_y, pip_diameter, pip_diameter),
                (adjusted_x - die_width / 4, adjusted_y + die_width / 4, pip_diameter, pip_diameter),
                (adjusted_x + die_width / 4, adjusted_y + die_width / 4, pip_diameter, pip_diameter),
            ]
        else:
            raise ValueError(f"Invalid die number `{die_number}`")

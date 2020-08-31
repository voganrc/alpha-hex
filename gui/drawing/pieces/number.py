from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPainter, QPen, QFont, QBrush


class NumberDrawingMixin:
    NUMBER_DIAMETER = 90

    def draw_number(self, hex_):
        center_x, center_y = self.get_hex_center(hex_)
        bounding_box = QRect(
            center_x - NumberDrawingMixin.NUMBER_DIAMETER / 2,
            center_y - NumberDrawingMixin.NUMBER_DIAMETER / 2,
            NumberDrawingMixin.NUMBER_DIAMETER,
            NumberDrawingMixin.NUMBER_DIAMETER,
        )

        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 3, Qt.SolidLine))
        painter.setFont(QFont("Minion", 60))
        painter.drawText(bounding_box, Qt.AlignCenter, self._format_number(hex_.number))

        painter.setBrush(QBrush())
        painter.drawEllipse(bounding_box)

    def _format_number(self, number):
        return 'X' if number == 7 else str(number)

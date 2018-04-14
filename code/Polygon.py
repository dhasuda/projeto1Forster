from PyQt5.QtGui import QColor, QPolygon

class Polygon(QPolygon):

    def __init__(self, color=QColor.fromHsv(0, 0, 150)):
        QPolygon.__init__(self)
        self.color = color

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color
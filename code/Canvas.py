import Model
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter, QColor, QPolygon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout

class Canvas(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.model = Model.Model()
        self.model.addCanvas(self)

    def initUI(self):
        self.resize(500, 300)
        self.move(300, 300)
        self.setWindowTitle('Exercise 1')

        self.show()

        self.polygon = None

    def mousePressEvent(self, QMouseEvent):
        self.model.addPoint(QMouseEvent.pos())
        self.update()


    def paintEvent(self, QPaintEvent):
        qp = QPainter()
        qp.begin(self)

        for point in self.model.getLastPoints():
            self.drawPointAt(qp, point.x(), point.y())
        if len(self.model.getLastPoints()) >= 3:
            self.polygon = self.getPolygon()
            self.drawSelfPolygon(qp)

        for point in self.model.getPoints():
            self.drawPointAt(qp, point.x(), point.y())

        for singlePolygon in self.model.getPolygons():
            self.drawSinglePolygon(qp, singlePolygon)
        qp.end()

    def getPolygon(self):
        pol = QPolygon()
        for point in self.model.getLastPoints():
            pol.append(point)
        return pol

    def drawPointAt(self, qp, x, y):
        radius = 4
        qp.setBrush(Qt.black)
        qp.setPen(Qt.NoPen)
        qp.drawEllipse(x-radius, y-radius, 2*radius, 2*radius)

    def drawSelfPolygon(self, qp):
        qp.setBrush(Qt.red)
        qp.setPen(Qt.NoPen)
        qp.drawPolygon(self.polygon)

    def drawSinglePolygon(self, qp, pol):
        qp.setBrush(Qt.blue)
        qp.setPen(Qt.NoPen)
        qp.drawPolygon(pol)

    def drawTriangle(self, qp):
        qp.setBrush(Qt.red)
        qp.setPen(Qt.NoPen)
        qp.drawPolygon(self.points)
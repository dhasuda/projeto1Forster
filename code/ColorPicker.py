import Model
import Polygon
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter, QColor, QPolygon
from PyQt5.QtCore import Qt,QRect
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout

class ColorPicker(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.model = Model.Model()
        self.model.addColorPicker(self)

    def initUI(self):
        self.resize(40+256, 20+256+20+40+20+40+20)
        self.move(1300, 300)
        self.setWindowTitle('Color Picker')
        self.HValue = 0.5

        self.selectedHValue = 0
        self.selectedSValue = 0
        self.selectedVValue = 0

        self.lastPointX = 0
        self.lastPointY = 0

        self.show()

        self.polygon = None

    def mousePressEvent(self, QMouseEvent):
        self.lastPointX = QMouseEvent.x()
        self.lastPointY = QMouseEvent.y()
        self.update()


    def paintEvent(self, QPaintEvent):
        qp = QPainter()
        qp.begin(self)

        self.drawHSpectrum(qp)
        self.drawSVSpectrum(qp)

        if(self.lastPointX >= 20 and self.lastPointX <= 276 and self.lastPointY >= 296 and self.lastPointY <= 336 ):
            self.HValue = (self.lastPointX - 20)/256
        elif(self.lastPointX >= 20 and self.lastPointX <= 276 and self.lastPointY >= 20 and self.lastPointY <= 276 ):
                    self.selectedHValue = self.HValue
                    self.selectedSValue = (self.lastPointX - 20)/256
                    self.selectedVValue = (self.lastPointY - 20)/256
                    self.model.setSelectedColor(self.selectedHValue,self.selectedSValue,self.selectedVValue)

        self.drawSelectedColor(qp)
        self.drawHSpectrum(qp)
        self.drawSVSpectrum(qp)

        qp.end()


    def drawHSpectrum(self, qp):
        for i in range(256):
            qp.setBrush(QtGui.QColor.fromHsvF(i/255, 1, 1))
            qp.setPen(Qt.NoPen)
            qp.drawRect(20 + i, 296, 1, 40)

    def drawSVSpectrum(self, qp):
        for x in range(256):
            for y in range (256):
                qp.setBrush(QtGui.QColor.fromHsvF(self.HValue, x/255, y/255))
                qp.setPen(Qt.NoPen)
                qp.drawRect(20 + x, 20 + y, 1, 1)

    def drawSelectedColor(self, qp):
        qp.setBrush(QtGui.QColor.fromHsvF(self.selectedHValue, self.selectedSValue, self.selectedVValue))
        qp.drawRect(256/2, 60 + 256+ 40, 40, 40)

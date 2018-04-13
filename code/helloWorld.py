import sys
import Canvas
import Button
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    canvas = Canvas.Canvas()
    buttons = Button.Button()
    sys.exit(app.exec_())

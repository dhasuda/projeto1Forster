import Model
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QListWidget, QListWidgetItem, QAbstractItemView, QColorDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class Button(QWidget):

    def __init__(self):
        super().__init__()
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 400
        self.list = None
        self.initUI()
        self.model = Model.Model()
        self.model.addButton(self)

    def initUI(self):
        self.setGeometry(self.left, self.top, self.width, self.height)

        newButton = QPushButton('New polygon', self)
        newButton.clicked.connect(self.newPolygon)

        saveButton = QPushButton('Save polygon', self)
        saveButton.clicked.connect(self.savePolygon)
        saveButton.move(0, 30)

        importButton = QPushButton('Import polygon', self)
        importButton.clicked.connect(self.importPolygon)
        importButton.move(0, 60)

        unionButton = QPushButton('Unite', self)
        unionButton.clicked.connect(self.unite)
        unionButton.move(280, 100)

        intersectionButton = QPushButton('Intersect', self)
        intersectionButton.clicked.connect(self.intersect)
        intersectionButton.move(280, 130)

        intersectionButton = QPushButton('Delete selected', self)
        intersectionButton.clicked.connect(self.delete)
        intersectionButton.move(280, 160)

        buttonButton = QPushButton('Change color', self)
        buttonButton.clicked.connect(self.changeColor)
        buttonButton.move(280, 190)

        self.list = QListWidget(self)
        self.list.move(10, 100)
        self.list.setSelectionMode(QAbstractItemView.MultiSelection)
        self.list.selectionModel().selectionChanged.connect(self.onListChage)

        self.show()

    def updateList(self):
        self.list.clear()
        i = 1
        for pol in self.model.getPolygons():
            item = QListWidgetItem()
            item.setText("Polygon " + str(i))
            self.list.addItem(item)
            i += 1

    @pyqtSlot()
    def newPolygon(self):
        self.model.createPolygon()

    @pyqtSlot()
    def savePolygon(self):
        self.model.savePolygon()

    @pyqtSlot()
    def importPolygon(self):
        self.model.importPolygon()

    @pyqtSlot()
    def unite(self):
        selected = [x.row() for x in self.list.selectedIndexes()]
        if len(selected) >= 2:
            self.model.unite(selected)

    @pyqtSlot()
    def intersect(self):
        selected = [x.row() for x in self.list.selectedIndexes()]
        if len(selected) >= 2:
            self.model.intersect(selected)

    @pyqtSlot()
    def delete(self):
        selected = [x.row() for x in self.list.selectedIndexes()]
        if len(selected) >= 1:
            self.model.delete(selected)

    @pyqtSlot()
    def changeColor(self):
        selected = [x.row() for x in self.list.selectedIndexes()]
        if len(selected) >= 1:
            self.model.changeColor(selected)

    def onListChage(self, current, previour):
        selected = [x.row() for x in self.list.selectedIndexes()]
        self.model.changeSelection(selected)

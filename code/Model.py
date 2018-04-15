import File
import Polygon
from PyQt5.QtGui import QColor, QPolygon

class Model:
    class __Model:
        def __init__(self):
            self.polygons = []
            self.points = []
            self.lastPoints = []
            self.canvas = None
            self.colorPicker = None
            self.button = None
            self.selectedH = 0
            self.selectedS = 0
            self.selectedV = 0

        def addPoint(self, point):
            self.points.append(point)
            self.lastPoints.append(point)

        def addMultiPolygon(self, multiPol):
            for newPol in multiPol:
                self.polygons.append(newPol)
            self.updateCanvas()
            self.updateButton()

        def getPoints(self):
            return self.points

        def getLastPoints(self):
            return self.lastPoints

        def getPolygons(self):
            return self.polygons

        def startNewPolygon(self):
            if len(self.lastPoints) >= 3:
                self.polygons.append(self.getPolygon())
            self.lastPoints = []
            self.points = []
            self.updateCanvas()
            self.updateButton()

        def unite(self, selected):
            first = selected[0]
            selected.pop(0)
            deleted = []
            for i in selected:
                self.polygons[first] = self.polygons[first].united(self.polygons[i])
                deleted.append(self.polygons[i])
            for deletedPolygon in deleted:
                self.polygons.remove(deletedPolygon)
            self.updateCanvas()
            self.updateButton()

        def intersect(self, selected):
            first = selected[0]
            selected.pop(0)
            deleted = []
            for i in selected:
                self.polygons[first] = self.polygons[first].intersected(self.polygons[i])
                deleted.append(self.polygons[i])
            for deletedPolygon in deleted:
                self.polygons.remove(deletedPolygon)
            self.updateCanvas()
            self.updateButton()

        def delete(self, selected):
            deleted = []
            for i in selected:
                deleted.append(self.polygons[i])
            for deletedPolygon in deleted:
                self.polygons.remove(deletedPolygon)
            self.updateCanvas()
            self.updateButton()

        def changeColor(self, selected):
            for i in selected:
                self.polygons[i].setColor(QColor.fromHsvF(self.selectedH, self.selectedS, self.selectedV))
            self.updateCanvas()
            self.updateButton()
            print("Color changed to" + "hsv("+str(self.selectedH)+","+str(self.selectedS)+","+str(self.selectedV)+")")

        def changeSelection(self, selected):
            self.points = []
            for i in selected:
                for index in range(self.polygons[i].count()):
                    self.points.append(self.polygons[i].point(index))

            self.updateCanvas()

        def getPolygon(self):
            pol = Polygon.Polygon()
            for point in self.lastPoints:
                pol.append(point)
            return pol

        def setCanvas(self, canvas):
            self.canvas = canvas

        def setColorPicker(self, colorPicker):
            self.colorPicker = colorPicker

        def setButton(self, button):
            self.button = button

        def setSelectedColor(self, h, s ,v ):
            self.selectedH = h
            self.selectedS = s
            self.selectedV = v

        def updateCanvas(self):
            if self.canvas:
                self.canvas.update()

        def updateButton(self):
            if self.button:
                self.button.updateList()

    instance = None
    def __init__(self):
        if not Model.instance:
            Model.instance = Model.__Model()

    def addPoint(self, point):
        self.instance.addPoint(point)

    def getPoints(self):
        return self.instance.getPoints()

    def getLastPoints(self):
        return self.instance.getLastPoints()

    def getPolygons(self):
        return self.instance.getPolygons()

    def createPolygon(self):
        print("Polygon created")
        self.instance.startNewPolygon()

    def savePolygon(self):
        File.File.serializeAndSave(self.instance.getPolygons())
        print("Polygon saved")

    def importPolygon(self):
        multiPol = File.File.deserialize()
        self.instance.addMultiPolygon(multiPol)

    def addCanvas(self, canvas):
        self.instance.setCanvas(canvas)

    def addColorPicker(self, colorPicker):
        self.instance.setColorPicker(colorPicker)

    def addButton(self, button):
        self.instance.setButton(button)

    def setSelectedColor(self, h, s ,v ):
            self.instance.setSelectedColor(h, s ,v)

    def unite(self, selected):
        self.instance.unite(selected)

    def intersect(self, selected):
        self.instance.intersect(selected)

    def delete(self, selected):
        self.instance.delete(selected)

    def changeColor(self, selected):
        self.instance.changeColor(selected)


    def changeSelection(self, selected):
        self.instance.changeSelection(selected)

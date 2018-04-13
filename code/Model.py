import File
from PyQt5.QtGui import QPolygon

class Model:
    class __Model:
        def __init__(self):
            self.polygons = []
            self.points = []
            self.lastPoints = []
            self.canvas = None
            self.button = None

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

        def changeSelection(self, selected):
            self.points = []
            for i in selected:
                for index in range(self.polygons[i].count()):
                    self.points.append(self.polygons[i].point(index))

            self.updateCanvas()

        def getPolygon(self):
            pol = QPolygon()
            for point in self.lastPoints:
                pol.append(point)
            return pol

        def setCanvas(self, canvas):
            self.canvas = canvas

        def setButton(self, button):
            self.button = button

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

    def addButton(self, button):
        self.instance.setButton(button)

    def unite(self, selected):
        self.instance.unite(selected)

    def intersect(self, selected):
        self.instance.intersect(selected)

    def delete(self, selected):
        self.instance.delete(selected)

    def changeSelection(self, selected):
        self.instance.changeSelection(selected)

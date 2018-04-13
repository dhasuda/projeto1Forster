from PyQt5.QtGui import QPolygon
from PyQt5.QtCore import QPoint

class File:

    @staticmethod
    def serializeAndSave(multiPolygon):
        file = open("multiPolygon.txt", "w")
        for pol in multiPolygon:
            file.write(str(pol.count()) + "\n")
            for i in range(pol.count()):
                file.write(str(pol.point(i).x()) + " " + str(pol.point(i).y()) + "\n")

        file.close()


    @staticmethod
    def deserialize():
        file = open("multiPolygon.txt", "r")
        multiPol = []
        numberOfPoints = 0
        pol = QPolygon()
        for line in file:
            if numberOfPoints == 0:
                data = line.strip()
                numberOfPoints = int(data)
                pol = QPolygon()
            else:
                data = line.strip().split(" ")
                x = int(data[0])
                y = int(data[1])
                point = QPoint(x, y)
                pol.append(point)
                numberOfPoints -= 1
                if numberOfPoints == 0:
                    multiPol.append(pol)

        return multiPol



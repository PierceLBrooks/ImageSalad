
# Author: Pierce Brooks

from PIL import Image
import utilities as util
import vector as vec
import traceback
import os

class Grid(object):
    def __init__(self, width, height):
        self.width = abs(int(width))
        self.height = abs(int(height))
        self.size = (self.width, self.height)
        rows = []
        for x in range(self.width):
            column = []
            for y in range(self.height):
                column.append(None)
            rows.append(column)
        self.units = rows

    def getCopy(self):
        copy = Grid(self.width, self.height)
        for x in range(self.width):
            for y in range(self.height):
                copy.setUnit(x, y, self.units[x][y])
        return copy

    def getSize(self):
        return self.size

    def getUnit(self, x, y):
        if ((x < 0) or (x >= self.width)):
            return None
        if ((y < 0) or (y >= self.height)):
            return None
        return self.units[x][y]

    def setUnit(self, x, y, unit):
        if ((x < 0) or (x >= self.width)):
            return False
        if ((y < 0) or (y >= self.height)):
            return False
        self.units[x][y] = unit
        return True

    def getString(self):
        for x in range(self.width):
            for y in range(self.height):
                print("("+str(x)+", "+str(y)+") = <\n" +str(self.units[x][y])+"\n>")

    def mix(self, other, rate):
        rows = []
        for x in range(self.width):
            column = []
            for y in range(self.height):
                column.append(self.units[x][y]+vec.Vector(util.multiplyVector(other.getUnit(x, y)-self.units[x][y], rate)))
            rows.append(column)
        self.units = rows
        return self

    def export(self, name):
        success = True
        try:
            path = os.path.join(util.getPath(), str(name)+".png")
            image = Image.new("RGBA", (self.width, self.height), "black")
            pixels = image.load()
            for x in range(self.width):
                for y in range(self.height):
                    pixel = self.units[x][y].getElements()
                    for i in range(len(pixel)):
                        pixel[i] = util.getClamp(int(pixel[i]), 0, 255)
                    pixels[x, y] = tuple(pixel)
            image.save(path)
        except:
            traceback.print_exc()
            success = False
        return success

    def __str__(self):
        return self.getString()

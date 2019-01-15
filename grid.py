
# Author: Pierce Brooks

class Grid(object):
    def __init__(self, width, height):
        self.width = abs(int(width))
        self.height = abs(int(height))
        self.size = (self.width, self.height)
        self.units = []
        for x in range(self.width):
            units = []
            for y in range(self.height):
                units.append(None)
            self.units.append(units)

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

    def __str__(self):
        return self.getString()


# Author: Pierce Brooks

import utilities as util

class Vector(object):
    def __init__(self, elements):
        self.elements = list(elements)
        for i in range(len(self.elements)):
            self.elements[i] = float(self.elements[i])

    def __getitem__(self, index):
        if (index < 0):
            return None
        if (index >= len(self)):
            return None
        return self.elements[index]

    def __call__(self):
        return self.getElements()

    def __list__(self):
        return self.getElements()

    def __str__(self):
        return self.getString()

    def __len__(self):
        return len(self.elements)

    def __abs__(self):
        return self.getMagnitude()

    def __invert(self):
        return Vector(self.elements).normalize()

    def __add__(self, other):
        return Vector(util.addVectors(self.elements, other.elements))

    def __sub__(self, other):
        return Vector(util.subtractVectors(self.elements, other.elements))

    def __mul__(self, other):
        return Vector(util.multiplyVectors(self.elements, other.elements))

    def __div__(self, other):
        return Vector(util.divideVectors(self.elements, other.elements))

    def __truediv__(self, other):
        return self.__div__(self, other)

    def __floordiv__(self, other):
        return self.__div__(self, other)

    def getString():
        return str(self.elements)

    def getElements(self):
        return util.getVectorCopy(self.elements)

    def getMagnitude(self):
        return util.getVectorMagnitude(self.elements)

    def getNormalization(self):
        return Vector(util.getVectorNormalization(self.elements))

    def normalize(self):
        self.elements = self.getNormalization().getElements()
        return self

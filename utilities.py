
# Author: Pierce Brooks

from PIL import Image
import vector as vec
import grid as g
import traceback
import inspect
import os

def getPath():
    frame = None
    path = ""
    try:
        frame = inspect.currentframe()
        path += str(os.path.dirname(os.path.abspath(inspect.getfile(frame))))
    except:
        traceback.print_exc()
    finally:
        del frame
    if not (len(path) == 0):
        path = path.replace("\\", "/")
        if not (path[(len(path)-1):] == "/"):
            path += "/"
	return path

def loadPixelVectors(path):
    grid = None
    try:
        image = os.path.join(getPath(), str(path))
        print(image)
        image = Image.open(image)
        image = image.convert()
        pixels = image.load()
        width = image.size[0]
        height = image.size[1]
        grid = g.Grid(width, height)
        for x in range(width):
            for y in range(height):
                grid.setUnit(x, y, vec.Vector(pixels[x, y]))
    except:
        grid = None
        traceback.print_exc()
    return grid

def getClamp(number, minimum, maximum):
    return min(maximum, max(minimum, number))

def getVectorCopy(vector):
	result = []
	for i in range(len(vector)):
		result.append(vector[i])
	return result

def getVectorMagnitude(vector):
    result = 0.0
    for i in range(len(vector)):
        result += float(vector[i])**2.0
    return result**0.5

def getVectorNormalization(vector):
    return divideVector(vector, getVectorMagnitude(vector))

def addVector(vector, number):
	result = []
	for i in range(len(vector)):
		result.append(vector[i]+number)
	return result

def subtractVector(vector, number):
	result = []
	for i in range(len(vector)):
		result.append(vector[i]-number)
	return result

def multiplyVector(vector, number):
	result = []
	for i in range(len(vector)):
		result.append(vector[i]*number)
	return result

def divideVector(vector, number):
	result = []
	for i in range(len(vector)):
		result.append(vector[i]/number)
	return result

def addVectors(vector, other):
	result = []
	if (len(vector) < len(other)):
		return None
	for i in range(len(vector)):
		result.append(vector[i]+other[i])
	return result

def subtractVectors(vector, other):
	result = []
	if (len(vector) < len(other)):
		return None
	for i in range(len(vector)):
		result.append(vector[i]-other[i])
	return result

def multiplyVectors(vector, other):
	result = []
	if (len(vector) < len(other)):
		return None
	for i in range(len(vector)):
		result.append(vector[i]*other[i])
	return result

def divideVectors(vector, other):
	result = []
	if (len(vector) < len(other)):
		return None
	for i in range(len(vector)):
		result.append(vector[i]/other[i])
	return result

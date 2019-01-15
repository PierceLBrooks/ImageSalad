
# Author: Pierce Brooks

import vector as vec
import utilities as util
import grid as g

def mix(origin, target):
    return origin.getCopy()

def run(arguments):
    if (len(arguments) < 2):
        print("This module needs at least two path string arguments to load images for mixing!")
        return None
    left = util.loadPixelVectors(arguments[0])
    right = util.loadPixelVectors(arguments[1])
    if ((left == None) or (right == None)):
        print("This module was unable to load both the specified images!")
        return None
    grid = left
    grids = []
    grids.append(left.getCopy())
    steps = 5
    for i in range(abs(int(steps))):
        print(i)
        grids.append(mix(grid, right))
    grids.append(right.getCopy())
    return grids

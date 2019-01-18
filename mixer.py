
# Author: Pierce Brooks

import vector as vec
import utilities as util
import grid as g

def mix(origin, target, rate):
    return origin.getCopy().mix(target, rate)

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
    #grids.append(left.getCopy())
    steps = 5
    rate = 1.0/float(steps)
    for i in range(abs(int(steps))):
        print(i)
        grid = mix(grid, right, rate)
        grids.append(grid)
    #grids.append(right.getCopy())
    for i in range(len(grids)):
        if not (grids[i].export("mixer/output/"+str(i+1))):
            print("Failure on export "+str(i+1)+"!")
            break
    return grids

matrixSize = 3
yEdgeMatrix = (-1, 0, 1, -2, 0, 2, -1, 0, 1)
xEdgeMatrix = (1, 2, 1, 0, 0, 0, -1, -2, -1)

def getEdge(pixels, x, y, w, h):
    yEdge = 0
    xEdge = 0
    for y1 in range(0, matrixSize):
        for x1 in range(0, matrixSize):
            if(x == 0 or y == 0 or x == w-1 or y == h-1):
                yEdge = 0
                xEdge = 0
            else:
                yEdge += pixels[x-1+x1, y-1+y1]*yEdgeMatrix[x1+matrixSize*y1]
                xEdge += pixels[x-1+x1, y-1+y1]*xEdgeMatrix[x1+matrixSize*y1]


    return (xEdge, yEdge)

def colorWheel(d, scale):
    d1 = 0
    d2 = 0
    d3 = 0
    if(d < 120):
        d1 = 1-(d/120)
        d2 = (d/120)
    if (120 <= d and d < 240):
        d2 = 1 - ((d-120) / 120)
        d3 = ((d-120) / 120)
    if (240 <= d):
        d3 = 1 - ((d-240) / 120)
        d1 = ((d-240) / 120)
    return (int(d1*scale), int(d2*scale), int(d3*scale))

def RGWheel(d, scale, height):
    d1 = 0
    d2 = 0
    if(d < 180):
        d1 = 1-(d/180)
        d2 = (d/180)
    if (180 <= d and d < 360):
        d1 = (d/180)-1
        d2 = 1-((d/180)-1)
    return (int((d1*scale+height)/2), int((d2*scale+height)/2), int(height))
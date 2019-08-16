from Vector import Vector
import ImageKernel
from PIL import Image
import math

Inputimage = Image.open(input("source image: "))

Heightmap = Image.new("L", Inputimage.size, 0)
normalmap = Image.new("RGB", Inputimage.size, (0,0,0))
im = Inputimage.load()
hm = Heightmap.load()
nm = normalmap.load()
for y in range (0, Heightmap.height):
    for x in range (0, Heightmap.width):
        val = im[x,y]
        nval = (val[0]+val[1]+val[2])/3
        hm[x,y] = (int(nval), )

def Sobol():
    for y in range (0, Heightmap.height):
        for x in range (0, Heightmap.width):
            edges = ImageKernel.getEdge(hm, x, y, Heightmap.width, Heightmap.height)
            if(edges[0] == 0 or edges[1] == 0):
                nm[x,y] = (0,0,0)
            else:
                a = math.atan2(edges[1], edges[0])
                a = ((180/math.pi)*a)+180
                s = math.sqrt(edges[0]**2 + edges[1]**2)
                nm[x,y] = ImageKernel.colorWheel(a, s)


def Normal():
    for y in range (0, Heightmap.height):
        for x in range(0, Heightmap.width):
            Blue = (hm[x,y]/2)+128
            edges = ImageKernel.getEdge(hm, x, y, Heightmap.width, Heightmap.height)
            if(edges[0] != 0 or edges[1] != 0):
                a = math.atan2(edges[1], edges[0])
                a = ((180 / math.pi) * a) + 180
                s = math.sqrt(edges[0] ** 2 + edges[1] ** 2)
                nm[x, y] = ImageKernel.RGWheel(a, s, Blue)
Normal()
normalmap.show()
normalmap.save("normal", "JPEG")
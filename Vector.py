import math
class Vector:

    def __init__(self, x,y,z):
        self.position = (x,y,z)

    def __add__(self, other):
        if (type(other) is Vector):
            X = self.position[0] + other.position[0]
            Y = self.position[1] + other.position[1]
            Z = self.position[2] + other.position[2]
        else:
            X = self.position[0] + other
            Y = self.position[1] + other
            Z = self.position[2] + other
        return Vector(X,Y,Z)

    def __mul__(self, other):
        if(type(other) is Vector):
            X = self.position[0] * other.position[0]
            Y = self.position[1] * other.position[1]
            Z = self.position[2] * other.position[2]
        else:
            X = self.position[0] * other
            Y = self.position[1] * other
            Z = self.position[2] * other
        return Vector(X, Y, Z)


    def Magnitude(self):
        x0 = math.pow(self.position[0], 2)
        y0 = math.pow(self.position[1], 2)
        z0 = math.pow(self.position[2], 2)
        X = math.sqrt(x0 + y0 + z0)
        return abs(X)


    def Zero(self):
        return Vector(0,0,0)

    @property
    def x(self):
        return self.position[0]

    @property
    def y(self):
        return self.position[1]

    @property
    def z(self):
        return self.position[2]
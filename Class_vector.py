
import math
class Points(object):
    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z

    def __sub__(self, no):
        self.x=self.x-no.x
        self.y=self.y-no.y
        self.z=self.z-no.z
        return Points(self.x,self.y,self.z)

    def dot(self, no):
        print("dot")

    def cross(self, no):
        print("cross")
        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)


points = []
for i in range(4):
    #a=list(input().split())
    a = list(map(float, input().split()))
    points.append(a)
    print(a)
    print(points)

a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
x = (b - a).cross(c - b)
y = (c - b).cross(d - c)
angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

print("%.2f" % math.degrees(angle))

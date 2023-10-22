class Shape():
    def __init__(self):
        pass
def getArea(self):
        pass

class Rectangle(Shape):
    def __init__(self, a, w):
        super().__init__()
        self.a = a
        self.w = w 

    def getArea(self):
        return self.a * self.w

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def getArea(self):
        return 3.14 * self.radius * self.radius
    
class Triangle(Shape):
    def __init__(self, b, h):
        super().__init__()
        self.b = b
        self.h = h

    def getArea(self):
        return 0.5 * self.b * self.h
    
file = open("C:\GISPLAB\GISProgramming\Lab3\shape.txt")
lines = file.readlines()
file.close()   

totalShapes = []

for line in lines:
    componets = line.split(',')
    shape = componets[0]
    print ("Shape:" + shape)

    if shape == 'Rectangle':
        x = float(componets[1])
        y = float(componets[2])
        totalShapes.append(Rectangle(x,y))
    elif shape == 'Circle':
        x = float(componets[1])
        totalShapes.append(Circle(x))
    elif shape == 'Triangle':
        x = float(componets[1])
        y = float(componets[2])
        totalShapes.append(Triangle(x,y))
    else:
        pass

for shape in totalShapes:
    print(shape.getArea())


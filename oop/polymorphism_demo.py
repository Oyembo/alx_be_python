class Shape:
    def __init__(self, area):
        self.area = area

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(area)
        self.length = length
        self.width = width
        self.area = length * width

class Circle(Shape):
    def __init__(self, radius):
        super().__init__(area)
        self.radius = radius
        self.area = math.pi * radius * radius

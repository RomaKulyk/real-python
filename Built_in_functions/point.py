class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        self._x = self.validate(value)

    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, value):
        self._y = self.validate(value)

    def validate(self, value):
        if not isinstance(value, int|float):
            raise ValueError("coordinates must be numbers")
        return value
    
from point import Point
point = Point(42,21)
print(point.x)
print(point.y)
point.x = 0
print(point.x)
point.x = "7"

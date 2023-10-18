# Python

import unittest
import math

class Shape2D:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        if isinstance(self, Rectangle) or isinstance(self, Square):
            return self.width * self.height
        elif isinstance(self, Triangle):
            return 0.5 * self.width * self.height
        elif isinstance(self, Circle):
            return math.pi * (self.width / 2) ** 2
        else:
            print('Invalid shape')

class Rectangle(Shape2D):
    pass

class Square(Shape2D):
    pass

class Triangle(Shape2D):
    pass

class Circle(Shape2D):
    def __init__(self, radius):
        super().__init__(radius, 0)

class TestGetArea(unittest.TestCase):
    def runTest(self):
        rectangle = Rectangle(2, 3)
        self.assertEqual(rectangle.get_area(), 6, "incorrect area")
        square = Square(2, 2)
        self.assertEqual(square.get_area(), 4, "incorrect area")
        triangle = Triangle(2, 3)
        self.assertEqual(triangle.get_area(), 3, "incorrect area")
        circle = Circle(2)
        self.assertEqual(circle.get_area(), math.pi * 1, "incorrect area")
        
unittest.main()
from abc import ABC, abstractmethod
import math
import json

# Abstract base class for all shapes
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Circle class — no change needed to AreaCalculator
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Square class — same
class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

# NEW shape: Triangle — no modification in AreaCalculator needed!
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# AreaCalculator remains unchanged — it's closed for modification
class AreaCalculator:
    def __init__(self, shapes=None):
        if shapes is None:
            shapes = []
        self.shapes = shapes

    def sum(self):
        return sum(shape.area() for shape in self.shapes)

    def output(self):
        return f"\nSum of the areas of provided shapes: {self.sum()}\n"

# Outputter class
class SumCalculatorOutputter:
    def __init__(self, calculator):
        self.calculator = calculator

    def json(self):
        return json.dumps({'sum': self.calculator.sum()})

    def html(self):
        return f"<p>Sum of the areas of provided shapes: {self.calculator.sum()}</p>"

# Example usage
shapes = [
    Circle(2),
    Square(5),
    Square(6),
    Triangle(10, 4)
]

areas = AreaCalculator(shapes)

print(areas.output())

outputter = SumCalculatorOutputter(areas)
print(outputter.json())
print(outputter.html())

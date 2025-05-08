from abc import ABC, abstractmethod
import math
import json

# Interface / Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Concrete implementation of Square
class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

# Concrete implementation of Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# AreaCalculator works with the Shape interface only
class AreaCalculator:
    def __init__(self, shapes=None):
        if shapes is None:
            shapes = []
        self.shapes = shapes

    def sum(self):
        return sum(shape.area() for shape in self.shapes)

    def output(self):
        return f"\nSum of the areas of provided shapes: {self.sum()}\n"

# Output formatting class
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
    Square(6)
]

areas = AreaCalculator(shapes)

print(areas.output())

outputter = SumCalculatorOutputter(areas)
print(outputter.json())
print(outputter.html())

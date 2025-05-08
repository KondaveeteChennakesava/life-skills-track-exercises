import math
import json

# Define the Square class
class Square:
    def __init__(self, length):
        self.length = length

# Define the Circle class
class Circle:
    def __init__(self, radius):
        self.radius = radius

# Define the AreaCalculator class
class AreaCalculator:
    def __init__(self, shapes=None):
        if shapes is None:
            shapes = []
        self.shapes = shapes

    def sum(self):
        area = []
        for shape in self.shapes:
            if isinstance(shape, Square):
                area.append(shape.length ** 2)
            elif isinstance(shape, Circle):
                area.append(math.pi * (shape.radius ** 2))
        return sum(area)

    def output(self):
        return f"\nSum of the areas of provided shapes: {self.sum()}\n"

# Define the SumCalculatorOutputter class
class SumCalculatorOutputter:
    def __init__(self, calculator):
        self.calculator = calculator

    def json(self):
        data = {'sum': self.calculator.sum()}
        return json.dumps(data)

    def html(self):
        return f"\nSum of the areas of provided shapes: {self.calculator.sum()}\n"

# Usage
shapes = [
    Circle(2),
    Square(5),
    Square(6)
]

areas = AreaCalculator(shapes)

# Output in plain text
print(areas.output())

# Output using SumCalculatorOutputter
outputter = SumCalculatorOutputter(areas)
print(outputter.json())
print(outputter.html())
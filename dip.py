from abc import ABC, abstractmethod
import math
import json

# Abstraction for shapes
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Concrete shapes
class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Area Calculator (high-level module)
class AreaCalculator:
    def __init__(self, shapes):
        self.shapes = shapes

    def sum(self):
        return sum(shape.area() for shape in self.shapes)

# Abstract Output Formatter (this is the dependency)
class OutputFormatter(ABC):
    @abstractmethod
    def format(self, calculator):
        pass

# HTML Formatter (low-level module)
class HTMLOutputFormatter(OutputFormatter):
    def format(self, calculator):
        return f"<p>Total area is: {calculator.sum():.2f}</p>"

# JSON Formatter (low-level module)
class JSONOutputFormatter(OutputFormatter):
    def format(self, calculator):
        return json.dumps({"total_area": calculator.sum()})

# Client code (depends only on abstractions)
if __name__ == "__main__":
    shapes = [Square(4), Circle(3)]
    calculator = AreaCalculator(shapes)

    html_formatter = HTMLOutputFormatter()
    json_formatter = JSONOutputFormatter()

    print(html_formatter.format(calculator))
    print(json_formatter.format(calculator))

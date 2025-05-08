from abc import ABC, abstractmethod
import math
import json

# Abstract base class for 3D shapes
class SolidShape(ABC):
    @abstractmethod
    def volume(self):
        pass

# Cube shape
class Cube(SolidShape):
    def __init__(self, length):
        self.length = length

    def volume(self):
        return self.length ** 3

# Sphere shape
class Sphere(SolidShape):
    def __init__(self, radius):
        self.radius = radius

    def volume(self):
        return (4/3) * math.pi * self.radius ** 3

# Cylinder shape
class Cylinder(SolidShape):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        return math.pi * self.radius ** 2 * self.height

# VolumeCalculator class
class VolumeCalculator:
    def __init__(self, solid_shapes):
        self.solid_shapes = solid_shapes

    def sum(self):
        return sum(shape.volume() for shape in self.solid_shapes)

    def output(self):
        return f"Sum of volumes of provided shapes: {self.sum():.2f}"

# Output formatter for VolumeCalculator
class VolumeCalculatorOutputter:
    def __init__(self, calculator):
        self.calculator = calculator

    def json(self):
        return json.dumps({'volume_sum': self.calculator.sum()})

    def html(self):
        return f"<p>Sum of the volumes of provided shapes: {self.calculator.sum():.2f}</p>"

    def plain_text(self):
        return f"Sum of the volumes of provided shapes: {self.calculator.sum():.2f}"

# Example usage
if __name__ == "__main__":
    shapes_3d = [
        Cube(3),
        Sphere(2),
        Cylinder(2, 5)
    ]

    calculator = VolumeCalculator(shapes_3d)
    outputter = VolumeCalculatorOutputter(calculator)

    print(outputter.plain_text())
    print(outputter.html())
    print(outputter.json())

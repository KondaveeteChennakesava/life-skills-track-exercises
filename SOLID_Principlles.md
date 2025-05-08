# SOLID Principles

* SOLID principles are the design principles that enble us manage most of the software design problems.
* This is an acronym for fivve design principles intended to make most software design more understandable, flexible and maintainable.
* These principles are the subset of many principles promoted by Robert C. Martin.
* This acronym was first introduced by Michael Feathers.

**S: Single Responsibility Principle**

**O: Open Closed Principle**

**L: Liskov Substitution Principle**

**I: Interface Segregation Principle**

**D: Dependency Inversion Principle**

---

## Single Responsibility Principle

Every module or class should have responsibility over a single part of the functionality provided by the softwware and that responsibility should be entirely encapsulated by that class.

<pre>
<code>
'''
import math
import json

class Square:
    def __init__(self, length):
        self.length = length

class Circle:
    def __init__(self, radius):
        self.radius = radius

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

class SumCalculatorOutputter:
    def __init__(self, calculator):
        self.calculator = calculator

    def json(self):
        data = {'sum': self.calculator.sum()}
        return json.dumps(data)

    def html(self):
        return f"\nSum of the areas of provided shapes: {self.calculator.sum()}\n"

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
'''
</code>
</pre>


## Open Closed Principle

A class or a module should be open for extension and should be closed for modification.


```
<pre>
<code>
'''
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
'''
</code>
</pre>
```


## Liskov Substitution Princciple

---

## Interface Segregation Principle

---

## Dependency Inversion Principle

# SOLID Principles

## Introduction

* SOLID principles are the design principles that enable us to manage most of the software design problems.
* This is an acronym for five design principles intended to make most software design more understandable, flexible, and maintainable.
* These principles are a subset of many principles promoted by Robert C. Martin.
* This acronym was first introduced by Michael Feathers.

**S: Single Responsibility Principle**

**O: Open Closed Principle**

**L: Liskov Substitution Principle**

**I: Interface Segregation Principle**

**D: Dependency Inversion Principle**

## Single Responsibility Principle

Every module or class should have responsibility over a single part of the functionality provided by the software, and that responsibility should be entirely encapsulated by that class.

<pre>
<code>
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
        return f"\nSum of the areas of provided shapes{self.calculator.sum()}\n"

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

</code>
</pre>


## Open Closed Principle

* Software entities such as classes, modules, functions, etc, should be open for extension, but closed for modification.

* Any new functionality should be implemented by adding new classes, attributes, and methods, instead of changing the current ones or existing ones.

<pre>
<code>
from abc import ABC, abstractmethod
import math
import json

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class AreaCalculator:
    def __init__(self, shapes=None):
        if shapes is None:
            shapes = []
        self.shapes = shapes

    def sum(self):
        return sum(shape.area() for shape in self.shapes)

    def output(self):
        return f"\nSum of the areas of provided shapes: {self.sum()}\n"

class SumCalculatorOutputter:
    def __init__(self, calculator):
        self.calculator = calculator

    def json(self):
        return json.dumps({'sum': self.calculator.sum()})

    def html(self):
        return f"Sum of the areas of provided shapes:{self.calculator.sum()}"

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
</code>
</pre>


## Liskov Substitution Principle

* S is a subtype of T, then objects of type T may be replaced with objects of type S.
* Derived types must be completely substitutable for their base types.

* LSP is a particular definition of a sub-typing relation, called behavioral sub-typing.

<pre>
<code>
from abc import ABC, abstractmethod
import math
import json

class SolidShape(ABC):
    @abstractmethod
    def volume(self):
        pass

class Cube(SolidShape):
    def __init__(self, length):
        self.length = length

    def volume(self):
        return self.length ** 3

class Sphere(SolidShape):
    def __init__(self, radius):
        self.radius = radius

    def volume(self):
        return (4/3) * math.pi * self.radius ** 3

class Cylinder(SolidShape):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        return math.pi * self.radius ** 2 * self.height

class VolumeCalculator:
    def __init__(self, solid_shapes):
        self.solid_shapes = solid_shapes

    def sum(self):
        return sum(shape.volume() for shape in self.solid_shapes)

    def output(self):
        return f"Sum of volumes of provided shapes: {self.sum():.2f}"

class VolumeCalculatorOutputter:
    def __init__(self, calculator):
        self.calculator = calculator

    def json(self):
        return json.dumps({'volume_sum': self.calculator.sum()})

    def html(self):
        return f"Sum of the volumes of provided shapes: {self.calculator.sum():.2f}"

    def plain_text(self):
        return f"Sum of the volumes of provided shapes: {self.calculator.sum():.2f}"


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

</code>
</pre>


## Interface Segregation Principle

* No client should be forced to depend on methods it does not use.
* One fat interface needs to be split into many smaller and relevant interfaces so that clients can know about the interfaces that are relevant to them.

* The LSP was first used and formulated by Robert C. Martin while consulting for Xerox.

<pre>
<code>
from abc import ABC, abstractmethod
import math
import json

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

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

class AreaCalculator:
    def __init__(self, shapes=None):
        if shapes is None:
            shapes = []
        self.shapes = shapes

    def sum(self):
        return sum(shape.area() for shape in self.shapes)

    def output(self):
        return f"\nSum of the areas of provided shapes: {self.sum()}\n"

class SumCalculatorOutputter:
    def __init__(self, calculator):
        self.calculator = calculator

    def json(self):
        return json.dumps({'sum': self.calculator.sum()})

    def html(self):
        return f"<p>Sum of the areas of provided shapes: {self.calculator.sum()}</p>"

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

</code>
</pre>


## Dependency Inversion Principle

* High-level modules should not depend on low-level modules. Both should depend on abstractions.
* Abstractions should not depend on details. Details should depend on abstractions.

* The interaction between high-level and low-level modules should be thought of as an abstract interaction between them.

<pre>
<code>
from abc import ABC, abstractmethod
import math
import json

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

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

class AreaCalculator:
    def __init__(self, shapes):
        self.shapes = shapes

    def sum(self):
        return sum(shape.area() for shape in self.shapes)

class OutputFormatter(ABC):
    @abstractmethod
    def format(self, calculator):
        pass

class HTMLOutputFormatter(OutputFormatter):
    def format(self, calculator):
        return f"Total area is: {calculator.sum():.2f}"

class JSONOutputFormatter(OutputFormatter):
    def format(self, calculator):
        return json.dumps({"total_area": calculator.sum()})


shapes = [Square(4), Circle(3)]
calculator = AreaCalculator(shapes)

html_formatter = HTMLOutputFormatter()
json_formatter = JSONOutputFormatter()

print(html_formatter.format(calculator))
print(json_formatter.format(calculator))

</code>
</pre>


## References

*  [SOLID: The First 5 Principles of Object Oriented Design](https://www.digitalocean.com/community/conceptual-articles/s-o-l-i-d-the-first-five-principles-of-object-oriented-design " By Digital Ocean")

*  [SOLID DESIGN PRINCIPLES(Video Series)](https://www.youtube.com/playlist?list=PL6n9fhu94yhXjG1w2blMXUzyDrZ_eyOme " By Kudden")

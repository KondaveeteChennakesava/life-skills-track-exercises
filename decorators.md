# Python Decorators

## What is a Decorator?
A **decorator** is a function that modifies or enhances another function without changing its actual code.

### A Simple Function:

```
def a_function():
    return "1+1"

if __name__ == "__main__":
    value = a_function()
    print(value)
```

All we do in the code above is call the function and print the return value. Let’s create `another_function`:

```
def another_function(func):
    def other_func():
        val = "The result of %s is %s" % (func(), eval(func()))
        return val
    return other_func

def a_function():
    return "1+1"

if __name__ == "__main__":
    value = a_function()
    print(value)
    decorator = another_function(a_function)
    print(decorator())
```

Let’s change the code slightly to turn `another_function` into a decorator:

```
def another_function(func):

    def other_func():
        val = "The result of %s is %s" % (func(),eval(func()))
        return val
    return other_func

@another_function
def a_function():
    return "1+1"

if __name__ == "__main__":
    value = a_function()
    print(value)
```

Let’s create a decorator that actually does something useful.

### Creating a Logging Decorator

```
import logging

def log(func):
    def wrap_log(*args, **kwargs):
        name = func.__name__
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

        # add file handler
        fh = logging.FileHandler("%s.log" % name)
        logger.addHandler(fh)

        logger.info("Running function: %s" % name)
        result = func(*args, **kwargs)
        logger.info("Result: %s" % result)
        return func
    return wrap_log

@log
def int_function(a):
    return a*2

if __name__ == "__main__":
    value = int_function(5)
```

This little script has a log function that accepts a function as its sole argument. It will create a logger object and a log file name based on the name of the function. Then the log function will log what function was called and what the function returned, if anything.

## Built-in Decorators

Python comes with several built-in decorators. The big three are:

* @classmethod
* @staticmethod
* @property

### @classmethod

* A method that **receives the class (`cls`) as the first argument**, not the instance.
* Can be used to create **alternative constructors**.
* Can access and modify class state that applies across all instances.

```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        from datetime import date
        return cls(name, date.today().year - birth_year)

p = Person.from_birth_year("Alice", 2000)
print(p.name, p.age)

```

### @staticmethod

* Does not receive self or cls as the first argument.
* Behaves like a regular function that belongs to the class’s namespace.
* Cannot access or modify class or instance state.
* Useful when the method is logically related to the class but doesn’t use its data.

```
class Math:
    @staticmethod
    def add(x, y):
        return x + y

print(Math.add(5, 3))  # 8
```

Use Case: Utility Functions

```
class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return 9/5 * c + 32
```

### @property

* Turns a method into a read-only property.
* Allows access like an attribute, but with method logic behind it.
* Use @property for getter, and .setter/.deleter to define corresponding methods.

```
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def diameter(self):
        return self._radius * 2

c = Circle(5)
print(c.diameter)  # 10
```

@property with @`property`.setter

```
class Employee:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value
```

## Wrapping Up

At this point you should know how to create your own decorators and how to use a few of Python’s built-in decorators. We looked at @classmethod, @property and @staticmethod. I would be curious to know how my readers use the built-in decorators and how they use their own custom decorators.

## References

* [Python101 Article](https://python101.pythonlibrary.org/chapter25_decorators.html)
* [Python Decorators: The Complete Guide](https://youtu.be/QH5fw9kxDQA?si=_gqx8qCdPJoAUewL) 
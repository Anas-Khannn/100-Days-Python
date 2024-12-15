# Abstraction 

"""

Abstraction hides the complexity of implementation and exposes only the necessary functionality. 
This can be achieved using abstract classes in Python.

"""

# Code 
from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract class
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Usage
rect = Rectangle(5, 10)
print(rect.area())      # Output: 50
print(rect.perimeter()) # Output: 30

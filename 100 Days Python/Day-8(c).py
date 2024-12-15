# Polymorpism
# Polymorphism allows the same method to have different implementations depending on the object. It can be achieved through method overriding.

# Code 


class Shape:
    def draw(self):
        print("Drawing a generic shape.")

class Circle(Shape):
    def draw(self):  # Overriding the draw method
        print("Drawing a circle.")

class Rectangle(Shape):
    def draw(self):  # Overriding the draw method
        print("Drawing a rectangle.")

# Usage
shapes = [Shape(), Circle(), Rectangle()]
for shape in shapes:
    shape.draw()


# Inheritance 
# Inheritance allows a class to inherit attributes and methods from another class.

# code 

class Animal:
    def eat(self):
        print("This animal eats food.")

class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        print("The dog barks.")

# Usage
dog = Dog()
dog.eat()  # Inherited from Animal
dog.bark() # Specific to Dog

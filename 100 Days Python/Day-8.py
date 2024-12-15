# Its Day 8 Of Covering and Mastering Python
# Topics covered  Today
#        (a) OOP Concepts
#        (b) 4 Main Pillars of OOP
#        (c) Encapsulation
#        (d) Abstraction
#        (e) Inheritance
#        (f) Polymorphism

"""


The four pillars of Object-Oriented Programming (OOP) are the fundamental principles that define the approach to software design in OOP. 
These are Encapsulation, Abstraction, Inheritance, and Polymorphism.


1 - Encapsulation is the bundling of data (variables) and methods (functions) that operate on the data into a single unit called a class. 
    It restricts direct access to some of an object's components, promoting controlled interaction.

            Key Idea: Keep data safe by using access modifiers like private, protected, or public.
            Benefit: Protects data integrity and makes code easier to maintain.


2 - Abstraction involves hiding complex implementation details and showing only the essential features of an object. 
    It allows users to interact with objects at a high level, without worrying about the underlying complexity.

      Key Idea: "What an object does" rather than "how it does it."
      Benefit: Simplifies problem-solving and reduces complexity.
          
      
 3 - Inheritance allows a class (child/derived class) to inherit properties and behaviors (methods) from another class (parent/base class). 
     This promotes reusability and establishes a relationship between classes.

         Key Idea: "Is-a" relationship between classes.
        Benefit: Reduces redundancy and enhances code maintainability. 

 4-  Polymorphism allows objects to be treated as instances of their parent class, with the ability to override or change behavior based on the object. 
      This includes method overloading and overriding.

         Key Idea: "Many forms" – a method behaves differently depending on the context.
         Benefit: Enables flexibility and scalability in code.           


"""

# ----------------------------------------------------#
# - Incapsulation

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def get_balance(self):  # Public method to access private variable
        return self.__balance

# Usage
account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500
# account.__balance = 0  # This will raise an AttributeError

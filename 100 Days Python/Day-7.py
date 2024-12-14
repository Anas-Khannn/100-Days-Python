# Day NUmber 7 of learning and Mastering Python 
#  Topics Covered Today are :
#      1- Classes and Objects 
#      2- Constructors and Destructors in it
#      3- Ver Basic OOP


#--------------------------------------------------------------------------------------#
 

class Book:

    # Constructor: Initializes the attributes of a Book object
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        print(f"Book '{self.title}' by {self.author} has been created.")

    # Method to display details of the book
    def display_details(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nPages: {self.pages}")

    # Destructor: Cleans up resources when the object is deleted
    def __del__(self):
        print(f"Book '{self.title}' is being removed from memory.")

# Interactive example with user input
print("Welcome to Anas Khan Book Center !!!!! ")
num_books = int(input("How many books would you like to create? "))
books = []

for i in range(num_books):
    print(f"\nEnter details for Book {i+1}:")
    title = input("Title: ")
    author = input("Author: ")
    pages = int(input("Pages: "))
    books.append(Book(title, author, pages))

print("\nDisplaying details of all books:")
for i, book in enumerate(books, 1):
    print(f"\nBook {i}:")
    book.display_details()

# Demonstrate destructor by deleting all books
print("\nDeleting all book objects...")
while books:
    del books[0]






    # ------------------------------------------------------ #


"""
        A class in Python is a blueprint or template for creating objects. It defines a set of attributes (data) and methods (functions) 
         that the objects created from the class will have.

# Key Points:
 # 1- A class encapsulates data and behavior into a single unit.
 # 2- Objects are instances of a class.
 # 3- Classes are defined using the class keyword.

 """


"""
--->   A constructor is a special method in a class that is automatically called when an object is created. 
         It is used to initialize the attributes of the class.

# Key Points:
In Python, the constructor method is named __init__.
It is commonly used to assign values to the attributes of an object.

----> A destructor is a special method in a class that is automatically called when an object is destroyed or deleted. 
           It is used to clean up resources, such as closing files or releasing memory, associated with the object.

# Key Points:
In Python, the destructor method is named __del__.
It is not commonly used, as Python has a garbage collector to manage memory automatically.









"""
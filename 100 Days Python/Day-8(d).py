# Over all Code to Cover ALl these Concepts in ONe COde 


from abc import ABC, abstractmethod

# --- Encapsulation ---
class User:
    def __init__(self, username, password):
        self.__username = username  # Private attribute
        self.__password = password  # Private attribute

    def login(self, username, password):
        """Checks if the provided credentials match the user's data."""
        if self.__username == username and self.__password == password:
            return True
        else:
            return False

# --- Abstraction ---
class Product(ABC):  # Abstract base class
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def display_info(self):
        pass

class Electronic(Product):
    def __init__(self, name, price, brand, warranty):
        super().__init__(name, price)
        self.brand = brand
        self.warranty = warranty

    def display_info(self):
        return f"Electronic: {self.name}, Price: ${self.price}, Brand: {self.brand}, Warranty: {self.warranty} years"

class Grocery(Product):
    def __init__(self, name, price, expiry_date):
        super().__init__(name, price)
        self.expiry_date = expiry_date

    def display_info(self):
        return f"Grocery: {self.name}, Price: ${self.price}, Expiry Date: {self.expiry_date}"

# --- Inheritance ---
class ShoppingCart:
    def __init__(self):
        self.items = []  # List to store products

    def add_item(self, product):
        self.items.append(product)
        print(f"{product.name} added to the cart.")

    def remove_item(self, product_name):
        for product in self.items:
            if product.name == product_name:
                self.items.remove(product)
                print(f"{product_name} removed from the cart.")
                return
        print(f"{product_name} not found in the cart.")

    def display_cart(self):
        if not self.items:
            print("Your cart is empty.")
        else:
            print("\nItems in your cart:")
            for item in self.items:
                print(item.display_info())

# --- Polymorphism ---
def checkout(cart, payment_method):
    print("\n--- Checkout ---")
    if not cart.items:
        print("Cart is empty! Please add items before checking out.")
        return
    
    total = sum(item.price for item in cart.items)
    print(f"Total amount: ${total}")
    print(f"Payment processed via {payment_method}. Thank you for shopping with us!")

# --- Main Program ---
if __name__ == "__main__":
    print("Welcome to the Online Shopping System!\n")

    # Step 1: Create a user
    name = input("Enter your name: ")
    username = input("Create a username: ")
    password = input("Create a password: ")
    user = User(username, password)
    print(f"Thank you, {name}! Your account has been created.\n")

    # Step 2: User login
    print("Please log in to continue.")
    while True:
        input_username = input("Username: ")
        input_password = input("Password: ")
        if user.login(input_username, input_password):
            print(f"Login successful! Welcome, {name}.\n")
            break
        else:
            print("Invalid credentials. Please try again.\n")

    # Step 3: Create products
    laptop = Electronic("Laptop", 1200, "Dell", 2)
    apple = Grocery("Apple", 3, "2024-12-31")
    tv = Electronic("Smart TV", 800, "Samsung", 3)
    products = [laptop, apple, tv]

    # Step 4: Use ShoppingCart
    cart = ShoppingCart()
    while True:
        print("\nAvailable Products:")
        for idx, product in enumerate(products, 1):
            print(f"{idx}. {product.display_info()}")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")
        if choice in ["1", "2", "3"]:
            product = products[int(choice) - 1]
            cart.add_item(product)
        elif choice == "4":
            cart.display_cart()
        elif choice == "5":
            payment_method = input("Enter payment method (e.g., Credit Card, PayPal): ")
            checkout(cart, payment_method)
            break
        elif choice == "6":
            print("Thank you for visiting the Online Shopping System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

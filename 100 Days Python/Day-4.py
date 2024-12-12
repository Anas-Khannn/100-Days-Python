
# In Day 4 of Mastering and Learning Python I Today Covered List and Practised it 
# Here is the Code of MY Day 4 of 100 
# Lets Go


# Creating a list of fruits
fruits = ["Apple", "Banana", "Cherry"]

# Printing the list
print("Original list of fruits:", fruits)

# Adding an item to the list
fruits.append("Orange")
print("After adding a fruit:", fruits)

# Removing an item from the list
fruits.remove("Banana")
print("After removing a fruit:", fruits)

# Accessing items in the list
print("First fruit in the list:", fruits[0])

# Iterating over the list
print("Fruits in the list:")
for fruit in fruits:
    print(fruit)

# Sorting the list
fruits.sort()
print("Sorted list of fruits:", fruits)

# Finding the length of the list
print("Number of fruits in the list:", len(fruits))

# Checking if an item exists in the list
if "Apple" in fruits:
    print("Apple is in the list.")
else:
    print("Apple is not in the list.")

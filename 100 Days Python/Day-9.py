# In Todays Session We Will be learning about Mastering Data Structures in Python Where we Start from the very Basic TO advance further Going On

# Topics To be Covered Today Are 
#    1- Array(List)



# --------------------------------------------------------------------------------------------#
# Mastering Data Structures in Python: Arrays (Lists)
# --------------------------------------------------------------------------------------------#

# Introduction
print("Welcome to the session on Mastering Data Structures in Python!")
print("Today, we'll start with the fundamental data structure: Arrays (Lists).")
print("Let's explore basic to advanced concepts step by step.\n")

# 1. Creating and Accessing Arrays (Lists)
print("# Step 1: Creating and Accessing Arrays (Lists)")
basic_list = [10, 20, 30, 40, 50]
print("Array (List):", basic_list)
print("Accessing first element:", basic_list[0])
print("Accessing last element:", basic_list[-1])
print("Slicing (2nd to 4th):", basic_list[1:4])
print()

# 2. Modifying Arrays
print("# Step 2: Modifying Arrays")
basic_list[2] = 100  # Changing the 3rd element
print("After modification:", basic_list)
basic_list.append(60)  # Adding an element
print("After appending 60:", basic_list)
basic_list.extend([70, 80])  # Adding multiple elements
print("After extending:", basic_list)
basic_list.remove(20)  # Removing an element
print("After removing 20:", basic_list)
print()

# 3. Iterating Over Arrays
print("# Step 3: Iterating Over Arrays")
print("Using a for loop:")
for item in basic_list:
    print(item, end=" ")
print("\n")

# 4. List Comprehensions
print("# Step 4: List Comprehensions")
squared_list = [x ** 2 for x in basic_list]
print("Original List:", basic_list)
print("Squared List:", squared_list)
print()

# 5. Advanced Operations
print("# Step 5: Advanced Operations")
print("Sorting:", sorted(basic_list))
print("Reversing:", list(reversed(basic_list)))
print("Sum of elements:", sum(basic_list))
print()

# 6. Multi-Dimensional Arrays
print("# Step 6: Multi-Dimensional Arrays")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matrix (2D List):")
for row in matrix:
    print(row)
print("Accessing an element (2nd row, 3rd column):", matrix[1][2])
print()

# 7. Copying Arrays
print("# Step 7: Copying Arrays")
copy_list = basic_list.copy()  # Using the copy method
print("Original List:", basic_list)
print("Copied List:", copy_list)
copy_list.append(90)
print("Modified Copied List:", copy_list)
print("Original List remains unchanged:", basic_list)
print()

# 8. Working with Python's `array` Module
print("# Step 8: Using the `array` Module")
import array
array_data = array.array('i', [10, 20, 30, 40, 50])  # 'i' represents integer type
print("Array Module Data:", array_data)
array_data.append(60)
print("After appending 60:", array_data)
print()

# 9. Combining Lists
print("# Step 9: Combining Lists")
combined_list = basic_list + squared_list
print("Combined List:", combined_list)
print()

# Conclusion
print("That's a wrap for today's session on Arrays (Lists) in Python!")
print("We covered creation, modification, advanced operations, multi-dimensional arrays, and more.")
print("Stay tuned for the next session as we dive deeper into other data structures!")

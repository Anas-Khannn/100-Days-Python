# Creating a list of numbers
numbers = [1, 2, 3, 4, 5]

# Accessing elements
print(numbers[0])  # Output: 1
print(numbers[-1])  # Output: 5

# Slicing a list
print(numbers[1:4])  # Output: [2, 3, 4]

# Modifying elements
numbers[2] = 10
print(numbers)  # Output: [1, 2, 10, 4, 5]

# Appending elements
numbers.append(6)
print(numbers)  # Output: [1, 2, 10, 4, 5, 6]

# Removing elements
numbers.remove(10)
print(numbers)  # Output: [1, 2, 4, 5, 6]
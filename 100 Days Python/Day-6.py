# Its Day 6 Of Covering and Mastering Python 
# Topics Covered Today
   # 1- Functions 
   # 2- Lambda
   # 3- Arrays 

#--------------------------------------------------#----------------
   #------- CODE ------------#


# 1. Functions

#  function to calculate the factorial of a number
def factorial(n):
    """
    Calculate the factorial of a number using recursion.
    :param n: Integer value for which factorial is calculated.
    :return: Factorial of n.
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Define a function to check if a number is prime
def is_prime(number):
    """
    Check if a number is prime.
    :param number: Integer value to check for primality.
    :return: Boolean indicating if the number is prime.
    """
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Using the functions
print("Factorial of 5:", factorial(5))
print("Is 29 prime?", is_prime(29))

# 2. Lambda Functions
# Using lambda to define small, anonymous functions

# Lambda to calculate the square of a number
square = lambda x: x ** 2
print("Square of 7:", square(7))

# Lambda to filter even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# Lambda to sort a list of tuples by the second value
pairs = [(1, 3), (4, 1), (5, 2), (2, 4)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print("Sorted pairs by second value:", sorted_pairs)

# 3. Arrays
# Demonstrating arrays using Python's array module

import array as arr

# Creating an array of integers
int_array = arr.array('i', [10, 20, 30, 40, 50])
print("Original array:", int_array)

# Accessing elements
print("First element:", int_array[0])
print("Last element:", int_array[-1])

# Adding elements
int_array.append(60)
print("Array after appending 60:", int_array)

# Removing elements
int_array.remove(20)
print("Array after removing 20:", int_array)

# Slicing arrays
print("Slice (2nd to 4th elements):", int_array[1:4])

# Using arrays for mathematical operations

import numpy as np

# Creating numpy arrays
np_array = np.array([1, 2, 3, 4, 5])
print("Numpy array:", np_array)

# Element-wise operations
print("Array + 5:", np_array + 5)
print("Array squared:", np_array ** 2)

# Summing array elements
print("Sum of elements:", np.sum(np_array))

# Finding maximum and minimum
print("Maximum element:", np.max(np_array))
print("Minimum element:", np.min(np_array))

# Putting it all together in a meaningful example
# Function to calculate the square of all prime numbers in an array using lambdas and numpy

def prime_squares(arr):
    """
    Calculate the squares of all prime numbers in an array.
    :param arr: List or array of integers.
    :return: List of squares of prime numbers.
    """
    primes = filter(is_prime, arr)  # Filter primes using is_prime function
    return list(map(lambda x: x ** 2, primes))

# Example usage
input_array = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print("Squares of primes in array:", prime_squares(input_array))

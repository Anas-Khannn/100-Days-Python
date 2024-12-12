# Its Day 5 of covering and mastering Python 
# Topics Covered Today 
 #      1- if else 
 #      2- While Loop
 #      3- For Loops 


# ---------------------- C O D E -----------------------------------#

# 1- if else
# Example: Check if a number is positive, negative, or zero
number = int(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

# 2- While Loop
# Example: Print numbers from 1 to 5
print("Numbers from 1 to 5 using while loop:")
i = 1
while i <= 5:
    print(i)
    i += 1

# 3- For Loops
# Example: Print each character in a string
print("Characters in the string 'Python':")
for char in "Python":
    print(char)

# Example: Calculate the sum of the first 10 natural numbers
sum_of_numbers = 0
for num in range(1, 11):
    sum_of_numbers += num
print(f"Sum of the first 10 natural numbers: {sum_of_numbers}")
def find_max(numbers):
    """Finds the maximum number in a list."""
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

my_numbers = [10, 5, 8, 20, 15]
max_value = find_max(my_numbers)
print(max_value)  # Output: 20
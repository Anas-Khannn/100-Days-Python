import numpy as np

def calculate_statistics(numbers):
    """Calculates various statistical measures of a list of numbers.

    Args:
        numbers: A list of numbers.

    Returns:
        A tuple containing the mean, median, and standard deviation.
    """

    mean = np.mean(numbers)
    median = np.median(numbers)
    std_dev = np.std(numbers)

    return mean, median, std_dev

# Sample data
data = [10, 25, 15, 30, 22, 18, 28]

# Calculate statistics
mean, median, std_dev = calculate_statistics(data)

print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)
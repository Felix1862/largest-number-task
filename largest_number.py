#  **********Compulsory Task 2**********
# Follow these steps:
# ● In a file called largest_number.py, create a function that returns the
# largest number in a list of integers taken as an argument. The problem
# needs to be solved recursively without using loops.
# Examples of input and output:
# largest_number([1, 4, 5, 3])
# => 5
# largest_number([3, 1, 6, 8, 2, 4, 5])
# => 8

# Functions for differentiating the Maximum number in a list
def largest_number(number_list):
    """Find the largest number in a list.

    Args:
        ln (integers): Randomly placed numbers in a list.

    Returns:
        integers: Leveraging slicing to get the highest number.
    """
    if len(number_list) == 1:
        return number_list[0]
    return max(number_list[0], largest_number(number_list[1:]))  # Compares 1st element & last.


# Number input
sample_list1 = [1, 4, 5, 3]
sample_list2 = [3, 1, 6, 8, 2, 4, 5]
print(largest_number(sample_list1))
print(largest_number(sample_list2))

"""
Session 3

Problem 1: Count Even Numbers

Description:
Given a list of integers, return the number of even
numbers in the list.

Example:

Input:
[3, 8, 5, 12, 7, 10]

Output:
3
"""

def count_even_numbers(numbers):
    count = 0

    for n in numbers:
        if n % 2 == 0:
            count += 1
    return count


print(count_even_numbers([3, 8, 5, 12, 7, 10]))

"""
Session 3

Problem 2: Find the Smallest Number

Description:
Given a list of integers, return the smallest number
in the list.

Example:

Input:
[8, 3, 12, 1, 6]

Output:
1
"""

def smallest_number(numbers):
    smallest = float("inf")
    for n in numbers:
        if n < smallest:
            smallest = n
    return smallest

print(smallest_number([8, 3, 12, 1, 6]))

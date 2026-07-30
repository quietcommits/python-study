"""
Session 5

Problem 1: Count Numbers Greater Than a Value

Description:
Given a list of integers and a target value, return
the number of elements that are greater than the target.

Example:

Input:
numbers = [3, 8, 5, 12, 7, 10]
target = 6

Output:
4
"""

def count_greater_than(numbers, target):
    count = 0
    for n in numbers:
        if n > target:
            count += 1
    return count

print(count_greater_than([3, 8, 5, 12, 7, 10], 6))

"""
Session 5

Problem 2: Find the Sum of Positive Numbers

Description:
Given a list of integers, return the sum of all positive
numbers in the list.

Zero and negative numbers should not be included.

Example:

Input:
[-3, 5, 0, 8, -1, 2]

Output:
15
"""

def sum_positive_numbers(numbers):
    total = 0
    for n in numbers:
        if n > 0:
            total += n
    return total

print(sum_positive_numbers([-3, 5, 0, 8, -1, 2]))

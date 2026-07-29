"""
Session 4

Problem 1: Count Positive Numbers

Description:
Given a list of integers, return the number of positive
numbers in the list.

Note:
Zero is not a positive number.

Example:

Input:
[-3, 5, 0, 8, -1, 2]

Output:
3
"""

def count_positive_numbers(numbers):
    count = 0
    for n in numbers:
        if n > 0:
            count += 1
    return count

print(count_positive_numbers([-3, 5, 0, 8, -1, 2]))

"""
Session 4

Problem 2: Reverse a List

Description:
Given a list of integers, return a new list with the
elements in reverse order.

Do not use built-in functions that directly reverse
the list.

Example:

Input:
[1, 2, 3, 4, 5]

Output:
[5, 4, 3, 2, 1]
"""

def reverse_list(numbers):
    result = []
    for n in range(len(numbers) - 1, -1, -1):
        result.append(numbers[n])
    return result

print(reverse_list([1, 2, 3, 4, 5]))

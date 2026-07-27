"""
Session 2

Problem 1: Remove Duplicates While Keeping Order

Description:
Given a list of integers, return a new list with
duplicate values removed while keeping the original order.

Example:

Input:
[3, 1, 2, 3, 2, 4, 1]

Output:
[3, 1, 2, 4]
"""

def remove_duplicates(numbers):

    result = []

    for n in numbers:
        if n not in result:
            result.append(n)
    return result

print(remove_duplicates([3, 1, 2, 3, 2, 4, 1]))

"""
Session 2

Problem 2: Find the Second Largest Number

Description:
Given a list of unique integers, return the second
largest number in the list.

Example:

Input:
[7, 2, 9, 4, 5]

Output:
7
"""

def second_largest(numbers):

    largest = float("-inf")
    second = float("-inf")

    for n in numbers:
        if n > largest:
            largest = n

    for n in numbers:
        if n > second and n < largest:
            second = n
    return second

print(second_largest([7, 2, 9, 4, 5]))

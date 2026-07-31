"""
Session 6

Problem 1: Find the First Negative Number

Description:
Given a list of integers, return the first negative
number in the list.

If there are no negative numbers, return None.

Example 1:

Input:
[5, 8, -3, 7, -1]

Output:
-3

Example 2:

Input:
[2, 4, 6]

Output:
None
"""

def first_negative_number(numbers):
    result = None
    for n in numbers:
        if n < 0:
            result = n
            break
    return result


print(first_negative_number([5, 8, -3, 7, -1]))
print(first_negative_number([2, 4, 6]))

"""
Session 6

Problem 2: Count Consecutive Equal Numbers

Description:
Given a list of integers, return the length of the
longest consecutive streak of equal numbers.

Example:

Input:
[2, 2, 2, 1, 1, 3, 3, 3, 3, 2]

Output:
4
"""

def longest_equal_streak(numbers):
    streak = 1
    longest = 1
    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i-1]:
            streak += 1
        else:
            streak = 1
        if streak > longest:
            longest = streak
    return longest

print(longest_equal_streak([2, 2, 2, 1, 1, 3, 3, 3, 3, 2]))

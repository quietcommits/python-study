"""
Session 8

Problem 1: Remove Spaces from a String

Description:
Given a string, return a new string with all spaces
removed.

Example:

Input:
"python data analysis"

Output:
"pythondatanalysis"
"""

def remove_spaces(text):
    result = ""
    for char in text:
        if char != " ":
            result += char
    return result

print(remove_spaces("python data analysis"))

"""
Session 8

Problem 2: Check Palindrome

Description:
Given a string, return True if the string is a
palindrome, otherwise return False.

A palindrome is a word that reads the same forward
and backward.

Example 1:

Input:
"level"

Output:
True

Example 2:

Input:
"python"

Output:
False
"""

def is_palindrome(text):
    for i in range(len(text)):
        if text[i] != text[len(text) - 1 - i]:
            return False
    return True

print(is_palindrome("level"))
print(is_palindrome("python"))

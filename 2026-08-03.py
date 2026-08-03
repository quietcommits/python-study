"""
Session 7

Problem 1: Count Vowels

Description:
Given a string, return the number of vowels in the string.

Vowels are:
a, e, i, o, u

Example:

Input:
"python programming"

Output:
4
"""

def count_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

print(count_vowels("python programming"))

"""
Session 7

Problem 2: Count Character Frequency

Description:
Given a string and a target character, return how many
times the target character appears in the string.

Example:

Input:
text = "banana"
target = "a"

Output:
3
"""

def count_character(text, target):
    count = 0
    for char in text:
        if char == target:
            count += 1
    return count

print(count_character("banana", "a"))

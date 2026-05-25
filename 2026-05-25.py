# Problem 1 (loops + condition)

nums = [2, 5, 8, 3, 10, 7]

# Print only even numbers that are greater than 5.

for n in nums:
    if n % 2 == 0 and n > 5:
        print(n)

# Problem 2 (list building)

nums = [1, 2, 3, 4, 5]

# Create a new list that contains each number multiplied by 3.
# Print the result.

results = []

for n in nums:
    results.append(n * 3)

print(results)

# Problem 3 (strings + condition)

words = ["apple", "hi", "banana", "cat", "grape"]

# Print only words that have 5 or more characters.

for n in words:
    if len(n) >= 5:
        print(n)

# Problem 4 (nested condition)

nums = [2, 5, 8, 11, 14, 17, 20]

# Print numbers that are:
# - even
# - and greater than 10

for n in nums:
    if n % 2 == 0 and n > 10:
        print(n)

# Problem 5 (basic filtering)

nums = [4, 9, 12, 7, 18, 3, 20]

# Print only numbers that are divisible by 3.

for n in nums:
    if n % 3 == 0:
        print(n)

# Problem 6 (accumulation - product)

nums = [1, 2, 3, 4, 5, 6, 7]

# Calculate the product of all numbers in the list.
# Print the result.

results = 1

for n in nums:
    results = results * n

print(results)

# Problem 7 (string filtering)

words = ["apple", "banana", "hi", "grape", "cat"]

# Create a new list that contains only words that end with the letter "e".
# Print the result.

results = []

for w in words:
    if w.endswith("e"):
        results.append(w)

print(results)

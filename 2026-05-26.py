# Problem 1 (multiple conditions + accumulation)

nums = [12, 5, 18, 7, 20, 3, 15]

# Count how many numbers:
# 1. are greater than or equal to 10
# 2. are odd
# 
# Print the final count. 

count = 0

for n in nums:
    if n >= 10 and n % 2 == 1:
        count += 1

print(count)

# Problem 2 (build a filtered list with transformation)

words = ["apple", "hi", "banana", "sky", "grape", "a"]

# Create a new list that:
# 1. keeps only words with length >= 5
# 2. stores them in uppercase
# Print the final list.

new = []

for w in words:
    if len(w) >= 5:
        new.append(w.upper())

print(new)

# Problem 3 (nested loop basic pattern)

nums = [1, 2, 3]
letters = ["a", "b"]

# Print all combinations like:
# 1a
# 1b
# 2a
# 2b 
# 3a
# 3b

for n in nums:
    for l in letters:
        print(str(n) + l)

# Problem 4 (simple nested loop count)

nums = [1, 2, 3]
letters = ["x", "y"]
# How many total combinations exist?
# Just print the count, not the pairs

count = 0

for n in nums:
    for l in letters:
        count += 1

print(count)

# Problem 5 (pattern integration: filter + count + condition chain)

nums = [2, 5, 8, 11, 14, 17, 20]

# Count numbers that are:
# 1. greater than 10
# 2. even
# Print result

count = 0

for n in nums:
    if n > 10 and n % 2 == 0:
        count += 1

print(count)

# Problem 6 (state tracking + conditional selection)

nums = [3, 7, 2, 9, 12, 5, 18, 6]

# Find the SECOND largest number in the list
# DO NOT use sort() or max()
# Print the result

largest = float("-inf")
second_largest = float("-inf")

for n in nums:
    if n > largest:
        second_largest = largest
        largest = n
    elif n > second_largest:
        second_largest = n
    
print(second_largest)

# Problem 7 (index + condition + state interaction)

nums = [4, 1, 7, 3, 9, 2, 8]

# Find the first number that is greater than its previous number
# Print that number

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        print(nums[i])
        break

# mistake log

# Problem 3 (nested loop basic pattern)

nums = [1, 2, 3]
letters = ["a", "b"]

# Print all combinations like:
# 1a
# 1b
# 2a
# 2b 
# 3a
# 3b

for n in nums:
    for l in letters:
        print(str(n) + l)
    

# Problem 4 (simple nested loop count)

nums = [1, 2, 3]
letters = ["x", "y"]
# How many total combinations exist?
# Just print the count, not the pairs

count = 0

for n in nums:
    for l in letters:
        count += 1

print(count)

# Problem 7 (index + condition + state interaction)

nums = [4, 1, 7, 3, 9, 2, 8]

# Find the first number that is greater than its previous number
# Print that number

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        print(nums[i])
        break

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

# Problem 8 (state + full scan counting pattern)

nums = [5, 12, 8, 20, 3, 15, 10]

# Count how many times a number is greater than the previous number
# Print the count

count = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        count += 1

print(count)

# Problem 9 (state tracking + first occurrence logic)

nums = [4, 9, 2, 7, 6, 3, 8]

# Find the FIRST number that is greater than ALL previous numbers
# Print that number

max_so_far = nums[0]

for n in nums[1:]:
    if n > max_so_far:
        max_so_far = n
        print(n)
        break

# Problem 10 (state tracking + no early break)

nums = [3, 6, 1, 9, 3, 12, 5]

# Find the largest number in the list
# WITHOUT using max()
# BUT you must NOT use break or slicing tricks

largest = float("-inf")

for n in nums:
    if n > largest:
        largest = n

print(largest)

# Problem 11 (multi-state tracking)

nums = [5, 2, 9, 1, 7, 6, 3]

# Find BOTH:
# 1. largets number
# 2. second largest number
# without using sort() or max()

largest = float("-inf")
second_largest = float("-inf")

for n in nums:
    if n > largest:
        second_largest = largest
        largest = n
    elif n > second_largest and n != largest:
        second_largest = n

print("largest:", largest, "and", "second largest:", second_largest)

# Problem 12 (pattern combination: filter + state + transformation)

nums = [3, 10, 5, 8, 15, 2, 20]

# From numbers greater than 5:
# 1. square them
# 2. count how many results are greater than 100
# Print the count

count = 0

for n in nums:
    if n > 5:
        squared = n * n
        if squared > 100:
            count += 1

print(count)

# Problem 13 (multi-step logic + reuse of transformed values)

nums = [4, 7, 12, 3, 9, 15, 6]

# For numbers greater than 3:
# 1. double them
# 2. count how many of those doubled values are divisible by 6
# Print the count

count = 0

for n in nums:
    if n > 3:
        double = n * 2
        if double % 6 == 0:
            count += 1

print(count)

# Problem 14 (combined pattern: nested + state + filter)

nums = [1, 2, 3, 4]
letters = ["a", "b", "c"]

# Print combinations BUT only when:
# 1. number is even
# 2. letter is not "b"
# Output format: number + letter

for n in nums:
    for l in letters:
        if n % 2 == 0 and l != "b":
                print(str(n) + l)

# Problem 15 (mini algorithm synthesis)

nums = [3, 8, 5, 12, 7, 10, 6]

# From numbers greater than 5:
# 1. subtract 1
# 2. count how many results are even AND greater than 5
# Print the count

count = 0

for n in nums:
    x = n - 1
    if n > 5 and x % 2 == 0 and x > 5:
        count += 1

print(count)

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

# Problem 9 (state tracking + first occurrence logic)

nums = [4, 9, 2, 7, 6, 3, 8]

# Find the FIRST number that is greater than ALL previous numbers
# Print that number

max_so_far = nums[0]

for n in nums[1:]:
    if n > max_so_far:
        max_so_far = n
        print(n)
        break

# Problem 1 (Count increases)

nums = [5, 8, 3, 7, 10, 6]

# Task:
# Count how many times a number is larger than
# the number immediately before it.
#
# Examples:
# 5 -> 8  (increase)
# 8 -> 3  (not)
# 3 -> 7  (increase)
#
# Print the count.

count = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        count += 1

print(count)

# Problem 2 (Count decreases)

nums = [12, 7, 9, 4, 8, 2]

# Task:
# Count how many times a number is smaller than
# the number immediately before it.
#
# Examples:
# 12 -> 7 (decrease)
# 7 -> 9  (not)
#
# Print the count.

count = 0

for i in range(1, len(nums)):
    if nums[i] < nums[i-1]:
        count += 1

print(count)

# Problem 3 (Count equal neighbors)

nums = [5, 5, 2, 2, 2, 7, 7, 3]

# Task:
# Count how many neighboring pairs
# have equal values.
#
# Examples:
# 5 -> 5 (equal)
# 2 -> 2 (equal)
# 2 -> 2 (equal)
# 7 -> 7 (equal)
#
# Print the count.

count = 0

for i in range(1, len(nums)):
    if nums[i] == nums[i - 1]:
        count += 1

print(count)

# Problem 4 (Sum of increases)

nums = [5, 8, 3, 7, 10, 6]

# Task:
# Whenever a number is larger than the previous one,
# add it to a running total.
#
# Examples:
# 5 -> 8  (add 8)
# 3 -> 7  (add 7)
# 7 -> 10 (add 10)
#
# Print the total.

total = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        total += nums[i]

print(total)

# Problem 5 (Sum of decreases)

nums = [12, 7, 9, 4, 8, 2]

# Task:
# Whenever a number is smaller than the previous one,
# add it to a running total.
#
# Examples:
# 12 -> 7 (add 7)
# 9 -> 4  (add 4)
# 8 -> 2  (add 2)
#
# Print the total.

total = 0

for i in range(1, len(nums)):
    if nums[i] < nums[i-1]:
        total += nums[i]

print(total)

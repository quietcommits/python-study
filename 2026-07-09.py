# Problem 1 (Largest even record high difference)

nums = [6, 11, 8, 16, 15, 24, 20]

# A record high is larger than every number before it.
#
# Whenever a NEW EVEN record high appears,
# calculate the difference from the previous record high.
#
# Example:
#
# 6   (first even record high)
# 11
# 16 -> difference = 5 (16 - 11)
# 24 -> difference = 8 (24 - 16)
#
# Task:
# Find the largest difference.
#
# Print the value.

largest = nums[0]
largest_diff = float("-inf")

for i in range(1, len(nums)):
    if nums[i] > largest:
        if nums[i] % 2 == 0:
            diff = nums[i] - largest
            if diff > largest_diff:
                largest_diff = diff
        largest = nums[i]

print(largest_diff)

# Problem 2 (Index of the largest even record high difference)

nums = [8, 13, 10, 18, 16, 26, 21]

# A record high is larger than every number before it.
#
# Whenever a NEW EVEN record high appears,
# calculate the difference from the previous record high.
#
# Task:
# Find the STARTING INDEX of the largest difference.
#
# Example:
# 18 -> 26
#
# Starting index = 3
#
# Print the index.

largest = nums[0]
largest_diff = float("-inf")
prev_index = 0

for i in range(1, len(nums)):
    if nums[i] > largest:
        if nums[i] % 2 == 0:
            diff = nums[i] - largest
            if diff > largest_diff:
                largest_diff = diff
                index = prev_index
        largest = nums[i]
        prev_index = i

print(index)

# Problem 3 (Value of the largest even record high difference)

nums = [10, 15, 14, 22, 19, 30, 28]

# A record high is larger than every number before it.
#
# Whenever a NEW EVEN record high appears,
# calculate the difference from the previous record high.
#
# Task:
# Print:
# 1. The previous record high
# 2. The new even record high
#
# that produce the largest difference.
#
# Example output:
# 22 30

largest = nums[0]
best_current = nums[0]
best_previous = nums[0]
largest_diff = float("-inf")

for i in range(1, len(nums)):
    if nums[i] > largest:
        if nums[i] % 2 == 0:
            diff = nums[i] - largest
            if diff > largest_diff:
                largest_diff = diff
                best_previous = largest
                best_current = nums[i]
        largest = nums[i]

print(best_previous, best_current)

# Problem 4 (Smallest even record high difference)

nums = [8, 13, 10, 18, 17, 24, 22]

# A record high is larger than every number before it.
#
# Whenever a NEW EVEN record high appears,
# calculate the difference from the previous record high.
#
# Task:
# Find the SMALLEST difference.
#
# Print the value.

largest = nums[0]
smallest_diff = float("inf")

for i in range(1, len(nums)):
    if nums[i] > largest:
        if nums[i] % 2 == 0:
            if nums[i] - largest < smallest_diff:
                smallest_diff = nums[i] - largest
        largest = nums[i]

print(smallest_diff)

# Problem 5 (Index of the smallest even record high difference)

nums = [10, 15, 14, 22, 21, 28, 27]

# A record high is larger than every number before it.
#
# Whenever a NEW EVEN record high appears,
# calculate the difference from the previous record high.
#
# Task:
# Find the STARTING INDEX of the smallest difference.
#
# Example:
# 15 -> 22
#
# Starting index = 1
#
# Print the index.

largest = nums[0]
smallest_diff = float("inf")
index = 0
starting_index = 0

for i in range(1, len(nums)):
    if nums[i] > largest:
        if nums[i] % 2 == 0:
            diff = nums[i] - largest
            if diff < smallest_diff:
                smallest_diff = diff
                index = starting_index
        largest = nums[i]
        starting_index = i

print(index)

# Problem 1 (Index of the last record low)

nums = [20, 17, 19, 14, 16, 11, 13]

# A record low is smaller than every number before it.
#
# Task:
# Find the index of the LAST record low.
#
# Print the index.

smallest = float("inf")
index = 0

for i in range(len(nums)):
    if nums[i] < smallest:
        smallest = nums[i]
        index = i

print(index)

# Problem 2 (How many times was the record high broken?)

nums = [4, 9, 7, 12, 15, 13, 18]

# A record high is larger than every number before it.
#
# The first element starts as the record high.
#
# Task:
# Count how many times the record high
# was BROKEN after the first element.
#
# Print the count.

highest = nums[0]
count = 0

for i in range(1, len(nums)):
    if nums[i] > highest:
        highest = nums[i]
        count +=1

print(count)

# Problem 3 (Largest drop from a record high)

nums = [10, 16, 13, 20, 12, 18, 9]

# A record high is larger than every number before it.
#
# Whenever a number is NOT a record high,
# calculate how far below the current
# record high it is.
#
# Example:
# Record high = 16
# 13 -> drop = 3
#
# Record high = 20
# 12 -> drop = 8
# 18 -> drop = 2
# 9  -> drop = 11
#
# Task:
# Find the largest drop.
#
# Print the value.

largest = nums[0]
largest_drop = float("-inf")

for i in range(1, len(nums)):
    if nums[i] > largest:
        largest = nums[i]
    else:
        if largest - nums[i] > largest_drop:
            largest_drop = largest - nums[i]

print(largest_drop)

# Problem 4 (Index of the largest drop)

nums = [8, 15, 11, 18, 10, 16, 7]

# A record high is larger than every number before it.
#
# Whenever a number is NOT a record high,
# calculate how far below the current
# record high it is.
#
# Task:
# Find the INDEX of the largest drop.
#
# Print the index.

largest = nums[0]
largest_drop = float("-inf")
index = 0

for i in range(1, len(nums)):
    if nums[i] > largest:
        largest = nums[i]
    else:
        if largest - nums[i] > largest_drop:
            largest_drop = largest - nums[i]
            index = i

print(index)

# Problem 5 (Largest drop value and index)

nums = [9, 14, 12, 20, 11, 17, 8]

# A record high is larger than every number before it.
#
# Whenever a number is NOT a record high,
# calculate how far below the current
# record high it is.
#
# Task:
# Print:
# 1. The largest drop
# 2. The index where it occurs
#
# Example output:
# 12 6

largest = nums[0]
largest_drop = float("-inf")
index = 0

for i in range(1, len(nums)):
    if nums[i] > largest:
        largest = nums[i]
    else:
        if largest - nums[i] > largest_drop:
            largest_drop = largest - nums[i]
            index = i

print(largest_drop, index)

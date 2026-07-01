# Problem 1 (Smallest local valley)

nums = [12, 5, 9, 3, 8, 2, 10]

# A local valley is smaller than both neighbors.
#
# Task:
# Find the smallest local valley.
#
# Print the value.
#
# You may assume there is at least one local valley.

smallest = float("inf")

for i in range(1, len(nums) - 1):
    if nums[i-1] > nums[i] < nums[i+1]:
        if nums[i] < smallest:
            smallest = nums[i]

print(smallest)

# Problem 2 (Index of the largest local valley)

nums = [15, 6, 12, 9, 14, 8, 20]

# A local valley is smaller than both neighbors.
#
# Task:
# Find the index of the largest local valley.
#
# Print the index.

largest = float("-inf")
index = 0

for i in range(1, len(nums) - 1):
    if nums[i-1] > nums[i] < nums[i+1]:
        if nums[i] > largest:
            largest = nums[i]
            index = i

print(index)

# Problem 3 (Sum of increasing differences)

nums = [5, 9, 7, 12, 15, 10]

# Whenever a number is larger than the previous one,
# add the difference to the total.
#
# Examples:
# 5 -> 9   add 4
# 7 -> 12  add 5
# 12 -> 15 add 3
#
# Task:
# Print the total.

total = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        total += nums[i] - nums[i-1]

print(total)

# Problem 4 (Largest increasing difference)

nums = [6, 11, 8, 17, 20, 15, 23]

# Whenever a number is larger than the previous one,
# calculate the difference.
#
# Examples:
# 6 -> 11   difference = 5
# 8 -> 17   difference = 9
# 17 -> 20  difference = 3
# 15 -> 23  difference = 8
#
# Task:
# Find the largest increasing difference.
#
# Print the value.

largest = float("-inf")

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        if nums[i] - nums[i - 1] > largest:
            largest = nums[i] - nums[i - 1]

print(largest)

# Problem 5 (Index of the largest increasing difference)

nums = [6, 11, 8, 17, 20, 15, 23]

# Whenever a number is larger than the previous one,
# calculate the difference.
#
# Task:
# Find the starting index of the
# largest increasing difference.
#
# Print the index.

largest = float("-inf")
index = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        if nums[i] - nums[i-1] > largest:
            largest = nums[i] - nums[i-1]
            index = i-1

print(index)

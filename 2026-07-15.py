# Problem 1 (Largest sum of an increasing streak)

nums = [2, 5, 8, 3, 6, 9, 12, 4]

# An increasing streak is a sequence of
# consecutive numbers where each number
# is larger than the previous one.
#
# Task:
# Find the LARGEST SUM among all
# increasing streaks.
#
# Example:
#
# 2, 5, 8        sum = 15
# 3, 6, 9, 12    sum = 30
# 4              sum = 4
#
# Print the sum.

total = nums[0]
largest = nums[0]

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        total += nums[i]
    else:
        if total > largest:
            largest = total
        total = nums[i]

if total > largest:
    largest = total

print(largest)

# Problem 2 (Smallest sum of a decreasing streak)

nums = [12, 9, 6, 15, 11, 8, 4, 10]

# A decreasing streak is a sequence of
# consecutive numbers where each number
# is smaller than the previous one.
#
# Task:
# Find the SMALLEST SUM among all
# decreasing streaks.
#
# Example:
#
# 12, 9, 6        sum = 27
# 15, 11, 8, 4    sum = 38
# 10              sum = 10
#
# Print the sum.

total = nums[0]
smallest = float("inf")

for i in range(1, len(nums)):
    if nums[i] < nums[i-1]:
        total += nums[i]
    else:
        if total < smallest:
            smallest = total
        total = nums[i]

if total < smallest:
    smallest = total

print(smallest)

# Problem 3 (Starting value of the increasing streak with the largest sum)

nums = [4, 7, 9, 3, 6, 10, 13, 5]

# An increasing streak is a sequence of
# consecutive numbers where each number
# is larger than the previous one.
#
# Task:
# Print the STARTING VALUE of the
# increasing streak that has the
# LARGEST SUM.
#
# Example:
#
# 4, 7, 9         sum = 20
# 3, 6, 10, 13    sum = 32
# 5               sum = 5
#
# Output:
# 3

total = nums[0]
largest = nums[0]
value = nums[0]
largest_value = nums[0]

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        total += nums[i]
    else:
        if total > largest:
            largest = total
            largest_value = value
        total = nums[i]
        value = nums[i]

if total > largest:
    largest = total
    largest_value = value

print(largest_value)

# Problem 4 (Ending value of the decreasing streak with the smallest sum)

nums = [14, 11, 8, 15, 10, 6, 3, 9]

# A decreasing streak is a sequence of
# consecutive numbers where each number
# is smaller than the previous one.
#
# Task:
# Print the ENDING VALUE of the
# decreasing streak that has the
# SMALLEST SUM.
#
# Example:
#
# 14, 11, 8      sum = 33 (ends with 8)
# 15, 10, 6, 3   sum = 34 (ends with 3)
# 9              sum = 9  (ends with 9)
#
# Output:
# 9

total = nums[0]
smallest = float("inf")
value = nums[0]
smallest_value = nums[0]

for i in range(1, len(nums)):
    if nums[i] < nums[i-1]:
        total += nums[i]
        value = nums[i]
    else:
        if total < smallest:
            smallest = total
            smallest_value = value
        total = nums[i]
        value = nums[i]

if total < smallest:
    smallest = total
    smallest_value = value

print(smallest_value)

# Problem 5 (Starting index of the increasing streak with the largest sum)

nums = [5, 8, 10, 4, 7, 11, 15, 6]

# An increasing streak is a sequence of
# consecutive numbers where each number
# is larger than the previous one.
#
# Task:
# Print the STARTING INDEX of the
# increasing streak that has the
# LARGEST SUM.
#
# Example:
#
# 5, 8, 10        sum = 23 (starts at index 0)
# 4, 7, 11, 15    sum = 37 (starts at index 3)
# 6               sum = 6
#
# Output:
# 3

total = nums[0]
largest = nums[0]
index = 0
largest_index = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        total += nums[i]
    else:
        if total > largest:
            largest = total
            largest_index = index
        total = nums[i]
        index = i

if total > largest:
    largest = total
    largest_index = index

print(largest_index)

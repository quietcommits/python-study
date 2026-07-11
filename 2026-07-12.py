# Problem 1 (Largest increasing streak sum)

nums = [3, 5, 8, 4, 6, 9, 12, 7]

# An increasing streak is a sequence of
# consecutive numbers where each number
# is larger than the previous one.
#
# Example:
#
# 3, 5, 8        sum = 16
# 4, 6, 9, 12    sum = 31
# 7              sum = 7
#
# Task:
# Find the LARGEST streak sum.
#
# Print the sum.

total = nums[0]
largest_total = nums[0]

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        total += nums[i]
    else:
        total = nums[i]
    if total > largest_total:
        largest_total = total

print(largest_total)

# Problem 2 (Smallest increasing streak sum)

nums = [4, 7, 9, 3, 5, 2, 6, 8]

# An increasing streak is a sequence of
# consecutive numbers where each number
# is larger than the previous one.
#
# Task:
# Find the SMALLEST streak sum.
#
# Print the sum.

total = nums[0]
smallest_total = float("inf")

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        total += nums[i]
    else:
        if total < smallest_total:
            smallest_total = total
        total = nums[i]

if total < smallest_total:
    smallest_total = total

print(smallest_total)

# Problem 3 (Largest decreasing streak sum)

nums = [12, 9, 5, 10, 7, 3, 1, 8]

# A decreasing streak is a sequence of
# consecutive numbers where each number
# is smaller than the previous one.
#
# Example:
#
# 12, 9, 5       sum = 26
# 10, 7, 3, 1    sum = 21
# 8              sum = 8
#
# Task:
# Find the LARGEST streak sum.
#
# Print the sum.

total = nums[0]
largest_total = nums[0]

for i in range(1, len(nums)):
    if nums[i] < nums[i-1]:
        total += nums[i]
    else:
        if total > largest_total:
            largest_total = total
        total = nums[i]

if total > largest_total:
    largest_total = total

print(largest_total)

# Problem 4 (Smallest decreasing streak sum)

nums = [15, 11, 8, 12, 10, 6, 9]

# A decreasing streak is a sequence of
# consecutive numbers where each number
# is smaller than the previous one.
#
# Example:
#
# 15, 11, 8   -> sum = 34
# 12, 10, 6   -> sum = 28
# 9           -> sum = 9
#
# Task:
# Find the SMALLEST streak sum.
#
# Print the sum.

total = nums[0]
smallest_total = float("inf")

for i in range(1, len(nums)):
    if nums[i] < nums[i-1]:
        total += nums[i]
    else:
        if total < smallest_total:
            smallest_total = total
        total = nums[i]

if total < smallest_total:
    smallest_total = total

print(smallest_total)

# Problem 5 (Starting value of the largest increasing streak sum)

nums = [3, 5, 8, 4, 6, 9, 12, 7]

# An increasing streak is a sequence of
# consecutive numbers where each number
# is larger than the previous one.
#
# Task:
# Print the STARTING VALUE of the
# increasing streak that has the
# LARGEST sum.
#
# Example:
#
# 3, 5, 8       sum = 16
# 4, 6, 9, 12   sum = 31
#
# Output:
# 4

total = nums[0]
largest_total = nums[0]
value = nums[0]
largest_value = nums[0]

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        total += nums[i]
    else:
        if total > largest_total:
            largest_total = total
            largest_value = value
        value = nums[i]
        total = nums[i]

if total > largest_total:
    largest_total = total
    largest_value = value

print(largest_value)

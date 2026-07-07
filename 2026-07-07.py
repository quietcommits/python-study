# Problem 1 (Largest rise from a record low)

nums = [20, 15, 18, 12, 17, 10, 16]

# A record low is smaller than every number before it.
#
# Whenever a number is NOT a record low,
# calculate how much higher it is than
# the current record low.
#
# Example:
# Record low = 15
# 18 -> rise = 3
#
# Record low = 12
# 17 -> rise = 5
#
# Record low = 10
# 16 -> rise = 6
#
# Task:
# Find the largest rise.
#
# Print the value.

smallest = nums[0]
largest_rise = float("-inf")

for i in range(1, len(nums)):
    if nums[i] < smallest:
        smallest = nums[i]
    else:
        if nums[i] - smallest > largest_rise:
            largest_rise = nums[i] - smallest

print(largest_rise)

# Problem 2 (Index of the largest rise)

nums = [18, 12, 15, 10, 17, 8, 16]

# A record low is smaller than every number before it.
#
# Whenever a number is NOT a record low,
# calculate how much higher it is than
# the current record low.
#
# Task:
# Find the INDEX where the largest rise occurs.
#
# Print the index.

smallest = nums[0]
largest_rise = float("-inf")
index = 0

for i in range(1, len(nums)):
    if nums[i] < smallest:
        smallest = nums[i]
    else:
        if nums[i] - smallest > largest_rise:
            largest_rise = nums[i] - smallest
            index = i

print(index)

# Problem 3 (Largest rise value and index)

nums = [25, 18, 20, 14, 22, 10, 19]

# A record low is smaller than every number before it.
#
# Whenever a number is NOT a record low,
# calculate how much higher it is than
# the current record low.
#
# Task:
# Print:
# 1. The largest rise
# 2. The index where it occurs

smallest = nums[0]
largest_rise = float("-inf")
index = 0

for i in range(1, len(nums)):
    if nums[i] < smallest:
        smallest = nums[i]
    else:
        if nums[i] - smallest > largest_rise:
            largest_rise = nums[i] - smallest
            index = i

print(largest_rise, index)

# Problem 4 (Smallest rise from a record low)

nums = [22, 18, 21, 15, 17, 12, 13]

# A record low is smaller than every number before it.
#
# Whenever a number is NOT a record low,
# calculate how much higher it is than
# the current record low.
#
# Task:
# Find the SMALLEST rise.
#
# Print the value.

smallest = nums[0]
smallest_rise = float("inf")

for i in range(1, len(nums)):
    if nums[i] < smallest:
        smallest = nums[i]
    else:
        if nums[i] - smallest < smallest_rise:
            smallest_rise = nums[i] - smallest

print(smallest_rise)

# Problem 5 (Index of the smallest rise)

nums = [30, 24, 27, 20, 22, 18, 19]

# A record low is smaller than every number before it.
#
# Whenever a number is NOT a record low,
# calculate how much higher it is than
# the current record low.
#
# Task:
# Find the INDEX where the smallest rise occurs.
#
# Print the index.

smallest = nums[0]
smallest_rise = float("inf")
index = 0

for i in range(1, len(nums)):
    if nums[i] < smallest:
        smallest = nums[i]
    else:
        if nums[i] - smallest < smallest_rise:
            smallest_rise = nums[i] - smallest
            index = i

print(index)

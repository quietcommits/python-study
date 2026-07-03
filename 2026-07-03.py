# Problem 1 (Count record highs)

nums = [8, 12, 10, 15, 14, 18, 16, 20]

# A record high is a number that is
# larger than every number before it.
#
# Example:
# 8   (record high)
# 12  (record high)
# 15  (record high)
# 18  (record high)
# 20  (record high)
#
# Task:
# Count how many record highs exist.
#
# Print the count.

largest = float("-inf")
count = 0

for n in nums:
    if n > largest:
        largest = n
        count += 1

print(count)

# Problem 2 (Sum of record highs)

nums = [6, 11, 9, 14, 13, 18, 17]

# A record high is larger than every
# number before it.
#
# Task:
# Find the sum of all record highs.
#
# Print the total.

largest = float("-inf")
total = 0

for n in nums:
    if n > largest:
        largest = n
        total += n

print(total)

# Problem 3 (Largest record high and its index)

nums = [9, 14, 12, 18, 16, 22, 20]

# A record high is larger than every
# number before it.
#
# Task:
# Find the last record high.
#
# Print:
# 1. The value
# 2. Its index

largest = float("-inf")
index = 0

for i in range(len(nums)):
    if nums[i] > largest:
        largest = nums[i]
        index = i

print(largest, index)

# Problem 4 (Count record lows)

nums = [20, 18, 22, 15, 17, 10, 12, 8]

# A record low is a number that is
# smaller than every number before it.
#
# Example:
# 20 (record low)
# 18 (record low)
# 15 (record low)
# 10 (record low)
# 8  (record low)
#
# Task:
# Count how many record lows exist.
#
# Print the count.

smallest = float("inf")
count = 0

for n in nums:
    if n < smallest:
        smallest = n
        count += 1

print(count)

# Problem 5 (Sum of record lows)

nums = [18, 15, 20, 12, 14, 9, 11, 7]

# A record low is smaller than every
# number before it.
#
# Task:
# Find the sum of all record lows.
#
# Print the total.

smallest = float("inf")
total = 0

for n in nums:
    if n < smallest:
        smallest = n
        total += n

print(total)

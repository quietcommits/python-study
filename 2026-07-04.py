# Problem 1 (Index of the first record high after index 0)

nums = [8, 6, 10, 9, 12, 11, 15]

# A record high is larger than every number before it.
#
# Ignore index 0.
#
# Task:
# Find the index of the first record high
# after index 0.
#
# Print the index.

largest = nums[0]

for i in range(1, len(nums)):
    if nums[i] > largest:
        print(i)
        break

# Problem 2 (Count record highs after the first element)

nums = [7, 5, 9, 8, 11, 10, 13]

# A record high is larger than every number before it.
#
# Ignore index 0 when counting.
#
# Task:
# Count how many record highs occur
# after the first element.
#
# Print the count.

largest = nums[0]
count = 0

for i in range(1, len(nums)):
    if nums[i] > largest:
        largest = nums[i]
        count += 1

print(count)

# Problem 3 (Sum of record highs after the first element)

nums = [10, 8, 13, 12, 15, 11, 18]

# A record high is larger than every number before it.
#
# Ignore index 0 when summing.
#
# Task:
# Find the sum of all record highs
# after the first element.
#
# Print the total.

largest = nums[0]
total = 0

for i in range(1, len(nums)):
    if nums[i] > largest:
        largest = nums[i]
        total += nums[i]

print(total)

# Problem 4 (First record low after index 0)

nums = [20, 18, 19, 15, 17, 12, 10]

# A record low is smaller than every number before it.
#
# Ignore index 0.
#
# Task:
# Find the index of the first record low
# after the first element.
#
# Print the index.

smallest = nums[0]

for i in range(1, len(nums)):
    if nums[i] < smallest:
        print(i)
        break

# Problem 5 (Count record lows after the first element)

nums = [15, 12, 14, 10, 11, 8, 9, 6]

# A record low is smaller than every number before it.
#
# Ignore index 0 when counting.
#
# Task:
# Count how many record lows occur
# after the first element.
#
# Print the count.

smallest = nums[0]
count = 0

for i in range(1, len(nums)):
    if nums[i] < smallest:
        smallest = nums[i]
        count += 1

print(count)

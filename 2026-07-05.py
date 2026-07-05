# Problem 1 (Largest record high difference)

nums = [8, 12, 10, 17, 15, 23, 20]

# A record high is larger than every number before it.
#
# Whenever a new record high appears,
# calculate how much larger it is than
# the previous record high.
#
# Example:
#
# 8   (first record high)
# 12  difference = 4
# 17  difference = 5
# 23  difference = 6
#
# Task:
# Find the largest difference.
#
# Print the value.

largest = nums[0]
largest_diff = float("-inf")

for i in range(1, len(nums)):
    if nums[i] > largest:
        diff = nums[i] - largest
        largest = nums[i]
        if diff > largest_diff:
            largest_diff = diff

print(largest_diff)

# Problem 2 (Smallest record high difference)

nums = [5, 9, 8, 13, 20, 18, 24]

# A record high is larger than every number before it.
#
# Whenever a new record high appears,
# calculate the difference from the
# previous record high.
#
# Task:
# Find the smallest such difference.
#
# Print the value.

largest = nums[0]
smallest = float("inf")

for i in range(1, len(nums)):
    if nums[i] > largest:
        diff = nums[i] - largest
        largest = nums[i]
        if diff < smallest:
            smallest = diff

print(smallest)

# Problem 3 (Index of the largest record high difference)

nums = [6, 10, 9, 15, 14, 22, 21]

# A record high is larger than every number before it.
#
# Whenever a new record high appears,
# calculate the difference from the
# previous record high.
#
# Task:
# Find the starting index of the
# largest record high difference.
#
# Example:
# 15 -> 22
#
# Starting index = 3
#
# Print the index.

largest = nums[0]
largest_diff = float("-inf")
index = 0
record_index = 0

for i in range(1, len(nums)):
    if nums[i] > largest:
        diff = nums[i] - largest
        if diff > largest_diff:
            largest_diff = diff
            index = record_index
        largest = nums[i]
        record_index = i

print(index)

# Problem 4 (Value of the largest record high difference)

nums = [7, 13, 11, 16, 15, 25, 22]

# A record high is larger than every number before it.
#
# Whenever a new record high appears,
# calculate the difference from the
# previous record high.
#
# Task:
# Print:
# 1. The previous record high
# 2. The new record high
#
# that produce the largest difference.
#
# Example output:
# 16 25

largest = nums[0]
largest_diff = float("-inf")
best_previous = nums[0]
best_current = nums[0]


for i in range(1, len(nums)):
    if nums[i] > largest:
        if nums[i] - largest > largest_diff:
            largest_diff = nums[i] - largest
            best_previous = largest
            best_current = nums[i]
        largest = nums[i]

print(best_previous, best_current)

# Problem 5 (Top 2 record high differences sum)

nums = [5, 10, 7, 14, 12, 20, 18]

# Task:
# Find sum of the TWO largest record high differences

largest = nums[0]
diff = []

for i in range(1, len(nums)):
    if nums[i] > largest:
        diff.append(nums[i] - largest)
        largest = nums[i]

largest1 = float("-inf")
largest2 = float("-inf")

for n in diff:
    if n > largest1:
        largest2 = largest1
        largest1 = n
    elif n > largest2:
        largest2 = n

print(largest1 + largest2)

# Problem 1 (Count increases)

nums = [4, 9, 3, 7, 8, 2, 10]

# Task:
# Count how many times a number is larger than
# the previous number.
#
# Examples:
# 4 -> 9  (increase)
# 3 -> 7  (increase)
# 7 -> 8  (increase)
# 2 -> 10 (increase)
#
# Print the count.

count = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        count +=1

print(count)

# Problem 2 (Sum of increases)

nums = [4, 9, 3, 7, 8, 2, 10]

# Task:
# Whenever a number is larger than the previous number,
# add that number to a running total.
#
# Examples:
# 4 -> 9  (add 9)
# 3 -> 7  (add 7)
# 7 -> 8  (add 8)
# 2 -> 10 (add 10)
#
# Print the total.

total = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        total += nums[i]

print(total)

# Problem 3 (Largest increase)

nums = [4, 9, 3, 7, 8, 2, 10]

# An increase is:
# nums[i] - nums[i-1]
#
# Only consider cases where nums[i] > nums[i-1].
#
# Examples:
# 4 -> 9  increase = 5
# 3 -> 7  increase = 4
# 7 -> 8  increase = 1
# 2 -> 10 increase = 8
#
# Task:
# Find the largest increase.
#
# Print the increase amount.

largest = float("-inf")

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        increase = nums[i] - nums[i-1]
        if increase > largest:
            largest = increase

print(largest)

# Problem 4 (Index of largest increase)

nums = [4, 9, 3, 7, 8, 2, 10]

# An increase is:
# nums[i] - nums[i-1]
#
# Only consider cases where nums[i] > nums[i-1].
#
# Examples:
# 4 -> 9  increase = 5
# 3 -> 7  increase = 4
# 7 -> 8  increase = 1
# 2 -> 10 increase = 8
#
# Task:
# Find the index where the largest increase ends.
#
# Example:
# The largest increase is 2 -> 10 (increase = 8),
# so print 6.

largest = float("-inf")
largest_index = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        increase = nums[i] - nums[i-1]
        if increase > largest:
            largest = increase
            largest_index = i

print(largest_index)

# Problem 5 (Sum of decreases)

nums = [12, 7, 9, 4, 8, 2, 10]

# Task:
# Whenever a number is smaller than the previous number,
# add it to a running total.
#
# Examples:
# 12 -> 7  (add 7)
# 9 -> 4   (add 4)
# 8 -> 2   (add 2)
#
# Print the total.

total = 0

for i in range(1, len(nums)):
    if nums[i] < nums[i-1]:
        total += nums[i]

print(total)

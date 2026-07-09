# Problem 1 (Longest increasing streak)

nums = [5, 8, 10, 7, 9, 11, 13, 6]

# An increasing streak is a sequence of
# consecutive numbers where each number
# is larger than the previous one.
#
# Example:
#
# 5, 8, 10      length = 3
# 7, 9, 11, 13  length = 4
# 6             length = 1
#
# Task:
# Find the length of the LONGEST
# increasing streak.
#
# Print the length.

streak = 1
longest = 1

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        streak += 1
    else:
        streak = 1
    if streak > longest:
        longest = streak

print(longest)

# Problem 2 (Longest decreasing streak)

nums = [15, 12, 10, 14, 11, 8, 5, 9]

# A decreasing streak is a sequence of
# consecutive numbers where each number
# is smaller than the previous one.
#
# Example:
#
# 15, 12, 10      length = 3
# 14, 11, 8, 5    length = 4
# 9               length = 1
#
# Task:
# Find the length of the LONGEST
# decreasing streak.
#
# Print the length.

streak = 1
longest = 1

for i in range(1, len(nums)):
    if nums[i] < nums[i-1]:
        streak += 1
    else:
        streak = 1
    if streak > longest:
        longest = streak

print(longest)

# Problem 3 (Index where the longest increasing streak starts)

nums = [4, 7, 9, 6, 8, 10, 12, 5]

# Task:
# Find the STARTING INDEX of the
# longest increasing streak.
#
# Example:
#
# 4, 7, 9          starts at index 0
# 6, 8, 10, 12     starts at index 3
#
# Print the index.

streak = 1
longest = 1
index = 0
longest_index = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        streak += 1
    else:
        streak = 1
        index = i
    if streak > longest:
        longest = streak
        longest_index = index

print(longest_index)

# Problem 4 (Value where the longest increasing streak starts)

nums = [3, 6, 8, 5, 9, 12, 15, 7]

# Task:
# Print the VALUE where the
# longest increasing streak starts.
#
# Example:
#
# 3, 6, 8          starts with value 3
# 5, 9, 12, 15     starts with value 5
#
# Output:
# 5

streak = 1
longest = 1
value = nums[0]
longest_value = nums[0]

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        streak += 1
    else:
        streak = 1
        value = nums[i]
    if streak > longest:
        longest = streak
        longest_value = value

print(longest_value)

# Problem 5 (Ending value of the longest increasing streak)

nums = [4, 7, 9, 5, 8, 10, 13, 6]

# Task:
# Print the VALUE where the
# longest increasing streak ENDS.
#
# Example:
#
# 4, 7, 9          ends with 9
# 5, 8, 10, 13     ends with 13
#
# Output:
# 13

streak = 1
longest = 1
value = nums[0]
longest_value = nums[0]

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        streak += 1
        value = nums[i]
    else:
        streak = 1
        value = nums[i]
    if streak > longest:
        longest = streak
        longest_value = value

print(longest_value)

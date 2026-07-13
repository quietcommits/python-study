# Problem 1 (Longest increasing EVEN streak)

nums = [2, 4, 6, 5, 8, 10, 12, 7]

# An increasing EVEN streak is a sequence of
# consecutive EVEN numbers where each number
# is larger than the previous one.
#
# Example:
#
# 2, 4, 6        length = 3
# 8, 10, 12      length = 3
#
# Task:
# Find the length of the LONGEST
# increasing EVEN streak.
#
# Print the length.

streak = 0
longest = 0

if nums[0] % 2 == 0:
    streak = 1
    longest = 1

for i in range(1, len(nums)):
    if nums[i] % 2 == 0 and nums[i] > nums[i-1]:
        streak += 1
    elif nums[i] % 2 == 0:
        streak = 1
    else:
        streak = 0
    if streak > longest:
        longest = streak

print(longest)

# Problem 2 (Longest decreasing ODD streak)

nums = [9, 7, 5, 8, 3, 1, 4, 11]

# A decreasing ODD streak is a sequence of
# consecutive ODD numbers where each number
# is smaller than the previous one.
#
# Example:
#
# 9, 7, 5      length = 3
# 3, 1         length = 2
#
# Task:
# Find the length of the LONGEST
# decreasing ODD streak.
#
# Print the length.

streak = 0
longest = 0

if nums[0] % 2 == 1:
    streak = 1
    longest = 1

for i in range(1, len(nums)):
    if nums[i] % 2 == 1:
        if nums[i] < nums[i-1]:
            streak += 1
        else:
            streak = 1
    else:
        streak = 0
    if streak > longest:
        longest = streak

print(longest)

# Problem 3 (Starting index of the longest increasing EVEN streak)

nums = [1, 2, 4, 6, 5, 8, 10, 12]

# Task:
# Find the STARTING INDEX of the
# longest increasing EVEN streak.
#
# Example:
#
# 2, 4, 6      starts at index 1
# 8, 10, 12    starts at index 5
#
# Print the index.

streak = 0
longest = 0
index = 0
longest_index = 0

if nums[0] % 2 == 0:
    streak = 1
    longest = 1

for i in range(1, len(nums)):
    if nums[i] % 2 == 0:
        if nums[i] > nums[i-1] and streak > 0:
            streak += 1
        else:
            index = i
            streak = 1
    else:
        streak = 0
    if streak > longest:
        longest = streak
        longest_index = index

print(longest_index)

# Problem 4 (Starting value of the longest decreasing ODD streak)

nums = [10, 9, 7, 5, 8, 3, 1, 6]

# A decreasing ODD streak is a sequence of
# consecutive ODD numbers where each number
# is smaller than the previous one.
#
# Task:
# Print the VALUE where the
# longest decreasing ODD streak starts.
#
# Example:
#
# 9, 7, 5      starts with 9
# 3, 1         starts with 3
#
# Output:
# 9

streak = 0 
longest = 0
value = nums[0]
longest_value = nums[0]

if nums[0] % 2 == 1:
    streak = 1
    longest = 1

for i in range(1, len(nums)):
    if nums[i] % 2 == 1: 
        if nums[i] < nums[i-1] and streak > 0:
            streak += 1
        else:
            streak = 1
            value = nums[i]
    else:
        streak = 0
    if streak > longest:
        longest = streak
        longest_value = value

print(longest_value)

# Problem 5 (Ending value of the longest increasing EVEN streak)

nums = [2, 4, 6, 5, 8, 10, 12, 7]

# An increasing EVEN streak is a sequence of
# consecutive EVEN numbers where each number
# is larger than the previous one.
#
# Task:
# Print the VALUE where the
# longest increasing EVEN streak ENDS.
#
# Example:
#
# 2, 4, 6        ends with 6
# 8, 10, 12      ends with 12
#
# Output:
# 12

streak = 0
longest = 0
value = nums[0]
longest_value = nums[0]

if nums[0] % 2 == 0:
    streak = 1
    longest = 1

for i in range(1, len(nums)):
    if nums[i] % 2 == 0:
        if nums[i] > nums[i-1] and streak > 0:
            streak += 1
            value = nums[i]
        else:
            streak = 1
            value = nums[i]
    else:
        streak = 0
    if streak > longest:
        longest = streak
        longest_value = value

print(longest_value)

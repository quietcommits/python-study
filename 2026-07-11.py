# Problem 1 (Longest even streak)

nums = [2, 4, 6, 3, 8, 10, 12, 5]

# An even streak is a sequence of
# consecutive EVEN numbers.
#
# Example:
#
# 2, 4, 6         length = 3
# 8, 10, 12       length = 3
#
# Task:
# Find the length of the LONGEST
# even streak.
#
# Print the length.

streak = 0
longest = 0

for n in nums:
    if n % 2 == 0:
        streak += 1
    else:
        streak = 0
    
    if streak > longest:
        longest = streak

print(longest)

# Problem 2 (Longest odd streak)

nums = [1, 3, 5, 2, 7, 9, 4, 11]

# An odd streak is a sequence of
# consecutive ODD numbers.
#
# Example:
#
# 1, 3, 5      length = 3
# 7, 9         length = 2
# 11           length = 1
#
# Task:
# Find the length of the LONGEST
# odd streak.
#
# Print the length.

streak = 0
longest = 0

for n in nums:
    if n % 2 == 1:
        streak += 1
    else:
        streak = 0
    if streak > longest:
        longest = streak

print(longest)

# Problem 3 (Starting index of the longest even streak)

nums = [1, 2, 4, 6, 3, 8, 10, 5]

# Task:
# Find the STARTING INDEX of the
# longest even streak.
#
# Example:
#
# 2, 4, 6      starts at index 1
# 8, 10        starts at index 5
#
# Print the index.

streak = 0
longest = 0
start_index = 0
longest_index = 0

for i in range(len(nums)):
    if nums[i] % 2 == 0:
        if streak == 0:
            start_index = i
        streak += 1
    else:
        streak = 0
    if streak > longest:
        longest = streak
        longest_index = start_index

print(longest_index)

# Problem 4 (Starting value of the longest odd streak)

nums = [2, 5, 7, 9, 4, 11, 13, 6]

# Task:
# Print the VALUE where the
# longest odd streak starts.
#
# Example:
#
# 5, 7, 9      starts with value 5
# 11, 13       starts with value 11
#
# Output:
# 5

streak = 0
longest = 0

for n in nums:
    if n % 2 == 1:
        if streak == 0:
            value = n
        streak += 1
    else:
        streak = 0
    if streak > longest:
        longest = streak
        longest_value = value

print(longest_value)

# Problem 5 (Ending value of the longest even streak)

nums = [1, 2, 4, 6, 3, 8, 10, 12]

# Task:
# Print the VALUE where the
# longest even streak ends.
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

for n in nums:
    if n % 2 == 0:
        streak += 1
        value = n
    else:
        streak = 0
    if streak > longest:
        longest = streak
        longest_value = value

print(longest_value)


# Problem 1 (Longest MULTIPLE OF 3 streak)

nums = [3, 6, 9, 4, 12, 15, 18, 21, 5]

# A multiple of 3 streak is a sequence of
# consecutive numbers where each number is a multiple of 3.
# (It doesn't matter if it increases or decreases, just multiples of 3!)
#
# Task:
# Find the length of the LONGEST multiple of 3 streak.
#
# Print the length.

streak = 0
longest = 0

for n in nums:
    if n % 3 == 0:
        streak += 1
    else:
        streak = 0
    if streak > longest:
        longest = streak

print(longest)

# Problem 2 (Starting INDEX of the longest multiple of 5 streak)

nums = [7, 5, 10, 15, 3, 20, 25, 30, 35, 4]

# Task:
# Find the STARTING INDEX of the longest 
# consecutive sequence of numbers that are multiples of 5.
#
# Print the starting index.

streak = 0
longest = 0
index = 0
longest_index = 0

if nums[0] % 5 == 0:
    streak = 1
    longest = 1
    index = 0
    longest_index = 0

for i in range(1, len(nums)):
    if nums[i] % 5 == 0:
        if streak > 0:
            streak += 1
        else:
            streak = 1
            index = i
    else:
        streak = 0
    if streak > longest:
        longest = streak
        longest_index = index

print(longest_index)

# Problem 3 (Longest strictly INCREASING streak - Any numbers)

nums = [10, 20, 30, 15, 20, 25, 30, 40, 10]

# An increasing streak is a sequence of consecutive numbers
# where each number is strictly LARGER than the previous one.
# (This time, it can be any number, not just even or odd!)
#
# Task:
# Find the length of the LONGEST increasing streak.
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

# Problem 4 (Ending VALUE of the longest strictly DECREASING streak)

nums = [5, 4, 3, 6, 7, 5, 3, 1, 8]

# A decreasing streak is a sequence of consecutive numbers
# where each number is strictly SMALLER than the previous one.
#
# Task:
# Print the VALUE where the longest decreasing streak ENDS.
#
# Example:
# 5, 4, 3     ends with 3
# 7, 5, 3, 1  ends with 1
#
# Output: 1

streak = 1
longest = 1
value = nums[0]
longest_value = nums[0]

for i in range(1, len(nums)):
    if nums[i] < nums[i-1]:
        streak += 1
        value = nums[i]
    else:
        streak = 1
        value = nums[i]
    if streak > longest:
        longest = streak
        longest_value = value

print(longest_value)

# Problem 5 (Longest MULTIPLE OF 2 OR 3 streak)

nums = [2, 4, 9, 15, 7, 8, 12, 6, 5]

# Task:
# Find the length of the LONGEST consecutive sequence of numbers 
# where each number is EITHER a multiple of 2 OR a multiple of 3.
#
# Example:
# [2, 4, 9, 15] -> All are multiples of 2 or 3. (Length = 4)
# [8, 12, 6]    -> All are multiples of 2 or 3. (Length = 3)
#
# Print the length.

streak = 0
longest = 0

for n in nums:
    if n % 2 == 0 or n % 3 == 0:
        streak += 1
    else:
        streak = 0
    if streak > longest:
        longest = streak

print(longest)

# Problem 1 (Longest decreasing streak)

nums = [10, 8, 5, 7, 4, 3, 1, 6]

# A decreasing streak is a sequence where each number
# is smaller than the previous number.
#
# Example:
# 7, 4, 3, 1 is a decreasing streak of length 4.
#
# Task:
# Find the length of the longest decreasing streak.
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

# Problem 2 (Count increasing streaks)

nums = [2, 5, 7, 3, 4, 6, 1, 8]

# Count how many increasing streaks exist.
#
# Examples:
#
# 2, 5, 7
# is one increasing streak.
#
# 3, 4, 6
# is another increasing streak.
#
# 1, 8
# is another increasing streak.
#
# Task:
# Count the number of increasing streaks.
#
# Print the count.

streak = 1
count = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        streak += 1
    else:
        if streak > 1:
            count += 1
        streak = 1

if streak > 1:
    count += 1

print(count)

# Problem 3 (Longest streak sum)

nums = [2, 4, 7, 3, 5, 8, 10, 1]

# Find the increasing streak with the greatest length.
#
# Then find the SUM of that streak.
#
# Example:
# 3, 5, 8, 10
# is the longest increasing streak.
#
# Sum = 26
#
# Print the sum.

streak = 1
longest = 1
sum = nums[0]
longest_sum = nums[0]

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        streak +=1
        sum += nums[i]
    else:
        streak = 1
        sum = nums[i]
    if streak > longest:
        longest = streak
        longest_sum = sum

print(longest_sum)

# Problem 4 (Starting index of longest increasing streak)

nums = [2, 4, 7, 3, 5, 8, 10, 1]

# Find the starting index of the longest
# increasing streak.
#
# Example:
# 3, 5, 8, 10
#
# Starting index = 3
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

# Problem 5 (Sum of all peak values)

nums = [4, 9, 5, 8, 3, 10, 2]

# A peak is larger than both neighbors.
#
# Peaks:
# 9
# 8
# 10
#
# Task:
# Find the sum of all peak values.
#
# Print the total.

total = 0

for i in range(1, len(nums) - 1):
    if nums[i-1] < nums[i] > nums[i+1]:
        total += nums[i]

print(total)

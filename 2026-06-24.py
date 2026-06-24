# Problem 1 (Count local peaks)

nums = [3, 8, 5, 10, 7, 12, 4]

# A local peak is a value that is larger than
# both its immediate neighbors.
#
# Example:
# 8 is a peak because:
# 8 > 3 and 8 > 5
#
# 10 is a peak because:
# 10 > 5 and 10 > 7
#
# Task:
# Count how many local peaks exist.
#
# Print the count.

count = 0

for i in range(1, len(nums) - 1):
    if nums[i-1] < nums[i] > nums[i+1]:
        count +=1 

print(count)

# Problem 2 (Sum of local valleys)

nums = [9, 3, 8, 2, 7, 1, 6]

# A local valley is a value that is smaller than
# both its immediate neighbors.
#
# Example:
# 3 is a valley because:
# 3 < 9 and 3 < 8
#
# 2 is a valley because:
# 2 < 8 and 2 < 7
#
# Task:
# Find the sum of all local valleys.
#
# Print the total.

total = 0

for i in range(1, len(nums) - 1):
    if nums[i-1] > nums[i] < nums[i+1]:
        total += nums[i]

print(total)

# Problem 3 (Index of first local peak)

nums = [4, 9, 5, 8, 3, 10, 2]

# A local peak is larger than both neighbors.
#
# Task:
# Find the index of the FIRST local peak.
#
# Print the index.

for i in range(1, len(nums) - 1):
    if nums[i-1] < nums[i] > nums[i+1]:
        print(i)
        break

# Problem 4 (Largest peak value)

nums = [5, 12, 7, 9, 4, 15, 6, 11]

# A local peak is a value larger than both neighbors.
#
# Task:
# Find the largest local peak value.
#
# Print the value.
#
# If there is no local peak, print -1.

largest = -1

for i in range(1, len(nums) - 1):
    if nums[i-1] < nums[i] > nums[i+1]:
        peak = nums[i]
        if peak > largest:
            largest = peak

print(largest)

# Problem 5 (Longest increasing streak)

nums = [2, 5, 7, 3, 4, 6, 8, 1]

# An increasing streak is a sequence where each number
# is larger than the previous number.
#
# Example:
# 3, 4, 6, 8 is an increasing streak of length 4.
#
# Task:
# Find the length of the longest increasing streak.
#
# Print the length.

streak = 1
longest = 1

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        streak +=1
    else:
        streak = 1
    if streak > longest:
        longest = streak

print(longest)

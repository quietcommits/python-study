# Problem 1 (Count values larger than both neighbors)

nums = [3, 8, 5, 10, 7, 12, 4]

# Task:
# Count how many elements are larger than
# both their immediate neighbors.
#
# Example:
# 8 is larger than 3 and 5.
# 10 is larger than 5 and 7.
#
# Print the count.

count = 0

for i in range(1, len(nums) - 1):
    if nums[i-1] < nums[i] > nums[i+1]:
        count += 1

print(count)

# Problem 2 (Index of first local minimum)

nums = [8, 5, 7, 3, 6, 2, 9]

# A local minimum is a value that is smaller
# than both immediate neighbors.

# Task:
# Find the index of the first local minimum.
#
# Example:
# 5 is smaller than 8 and 7,
# so the answer is 1.
#
# Print the index

for i in range(1, len(nums) - 1):
    if nums[i-1] > nums[i] < nums[i+1]:
        print(i)
        break

# Problem 3 (Longest increasing adjacent pair count)

nums = [1, 3, 5, 2, 4, 6, 8, 3]

# An increasing pair means:
# nums[i] < nums[i+1]

# Task:
# Find the longest consecutive sequence of increasing pairs.
#
# Example:
# 1 < 3 < 5 gives 2 increasing pairs.
# 2 < 4 < 6 < 8 gives 3 increasing pairs.
#
# Print the longest count.

count = 0
longest = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        count += 1
    else: 
        count = 0
    if count > longest:
        longest = count

print(longest)

# Problem 4 (Start index of longest increasing streak)

nums = [4, 6, 8, 3, 5, 7, 9, 2]

# An increasing streak means:
# each next element is greater than the previous one.
#
# Task:
# Find the start index of the longest increasing streak.
#
# Example:
# [3, 5, 7, 9] is the longest streak.
# It starts at index 3.
#
# Print the start index.

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

# Problem 5 (Index of largest neighboring difference)

nums = [10, 3, 8, 1, 12, 5]

# Difference means absolute difference:
# abs(nums[i] - nums[i+1])
#
# Example:
# 10 -> 3 : difference = 7
# 3 -> 8  : difference = 5
# 8 -> 1  : difference = 7
#
# Task:
# Find the index where the largest difference starts.
#
# If the largest difference is between nums[0] and nums[1],
# print 0.
#
# Print the index.

diff = 0
largest = 0
index = 0
largest_index = 0

for i in range(1, len(nums)):
    diff = abs(nums[i] - nums[i-1])
    index = i-1
    if diff > largest:
        largest = diff
        largest_index = index

print(largest_index)

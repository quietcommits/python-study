# Problem 1 (Local maxima detection)

nums = [1, 3, 2, 5, 4, 6, 1]

# A local maximum is a number that is greater than both neighbors.
# Example:
# nums = [1, 3, 2, 5, 4, 6, 1]
# local maxima: 
# 3 (1 < 3 > 2)
# 5 (2 < 5 > 4)
# 6 (4 < 6 > 1)
# Task:
# Count how many local maxima exist in the list.
# Rules:
# - Do NOT check first and last elements
# - Only check indices 1 to n-2
# Print the answer.

count = 0

for i in range(1, len(nums) - 1):
    if nums[i - 1] < nums[i] > nums[i + 1]:
        count += 1

print(count)

# Problem 2 (longest increasing continguous subarray)

nums = [1, 2, 3, 1, 2, 3, 4, 1]

# A strictly increasing continguous subarray means:
# each next element is greater than the previous one.
#
# Example increasing streaks:
# [1, 2, 3] -> length 3
# [1, 2, 3, 4] -> length 4
# 
# Task:
# Find the maximum length of any increasing contiguous streak.
# 
# Rules:
# - Only consecutive elements matter
# - If nums[i] <= nums[i-1], reset the streak
#
# Print the answer.

streak = longest = 1

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        streak += 1
    else: 
        streak = 1
    longest = max(longest, streak)

print(longest)

# Problem 3 (count increasing streak segments)

nums = [1, 2, 3, 1, 4, 5, 2, 7, 8, 9, 1]

# An increasing streak segment is a maximal contiguous subarray
# where each next element is strictly greater than
# the previous one.
#
# Example:
# [1, 2, 3]
# [1, 4, 5]
# [2, 7, 8, 9] 
# [1]
#
# Task:
# Count how many increasing streak segments exist.
# Rules:
# - A new streak starts when nums[i] <= nums[i - 1]
# - Count how many such streaks appear.
#
# Print the answer.

count = 0

for i in range(len(nums)):
    if i == 0 or nums[i] <= nums[i - 1]:
        count += 1

print(count)

# Problem 4 (length of each increasing streak segment)

nums = [1, 2, 3, 1, 4, 5, 2, 7, 8, 9, 1]

# An increasing streak segment is a maximal
# continguous subarray
# where each next element is strictly greater than
# the previous one.
#
# Example segments:
# [1, 2, 3]
# [1, 4, 5]
# [2, 7, 8, 9]
# [1]
# 
# Task:
# Print the length of each increasing streak
# segment.
#
# Rules:
# - A new streak starts when nums[i] <= nums[i - 1]
# - You must print all streak lengths in order
# 
# Expected output for this example:
# 3
# 3
# 4
# 1

streak = 1

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        streak += 1
    else: 
        print(streak)
        streak = 1

print(streak)

# Problem 5 (Print start and end indices of
# increasing streak segments)

nums = [1, 2, 3, 1, 4, 5, 2, 7, 8, 9, 1]

# An increasing streak segment is a maximal 
# contiguous subarray
# where each next element is strictly greater than
# the previous one.
# 
# Task:
# Print the start and end indices of each increasing streak segment.
# 
# Rules:
# - A new streak starts when nums[i] <= nums[i - 1]
#
# Example output:
# 0 2
# 3 4
# 5 8
# 10 10 

start = 0

for i in range(1, len(nums)):
    if nums[i] <= nums[i - 1]:
        end = i - 1
        print(start, end)
        start = i

print(start, len(nums) - 1)

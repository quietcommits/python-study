# Problem 1 (Index of the smallest odd number)

nums = [14, 9, 22, 5, 11, 8, 7]

# Task:
# Find the index of the smallest odd number.
#
# Print the index.
#
# You may assume there is at least one odd number.

smallest = float("inf")
index = 0

for i in range(len(nums)):
    if nums[i] % 2 == 1:
        if nums[i] < smallest:
            smallest = nums[i]
            index = i

print(index)

# Problem 2 (Closest number to 50 and its index)

nums = [42, 61, 47, 55, 49, 70]

# Task:
# Find the number closest to 50.
#
# Print:
# 1. The number
# 2. Its index
#
# You may assume there is only one correct answer.

smallest = float("inf")
closest = nums[0]
index = 0

for i in range(len(nums)):
    if abs(50-nums[i]) < smallest:
        smallest = abs(50-nums[i])
        closest = nums[i]
        index = i

print(closest, index)

# Problem 3 (Largest even number and its index)

nums = [13, 24, 8, 31, 42, 16, 7]

# Task:
# Find the largest even number.
#
# Print:
# 1. The value
# 2. The index
#
# You may assume there is at least one even number.

largest = float("-inf")

for i in range(len(nums)):
    if nums[i] % 2 == 0:
        if nums[i] > largest:
            largest = nums[i]
            index = i

print(largest, index)

# Problem 4 (Longest streak value and index)

nums = [3, 5, 8, 2, 4, 6, 9, 1]

# An increasing streak is a sequence where each number
# is larger than the previous number.
#
# Task:
# Find the starting index of the longest increasing streak.
#
# Print the starting index.

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

# Problem 5 (Closest number to average)

nums = [10, 18, 7, 25, 12, 15]

# Task:
# Find the number closest to the average.
#
# Print:
# 1. The number
# 2. Its index
#
# You may assume there is only one correct answer.

total = 0

for n in nums:
    total += n

average = total / len(nums)

smallest = float("inf")
closest = nums[0]
index = 0

for i in range(len(nums)):
    if abs(average - nums[i]) < smallest:
        smallest = abs(average-nums[i])
        closest = nums[i]
        index = i

print(closest, index)

# Problem 1 (Count local valleys below 10)

nums = [14, 6, 12, 9, 15, 4, 11]

# A local valley is smaller than both neighbors.
#
# Task:
# Count how many local valleys
# are less than 10.
#
# Print the count.

count = 0

for i in range(1, len(nums) - 1):
    if nums[i-1] > nums[i] < nums[i+1]:
        if nums[i] < 10:
            count += 1

print(count)

# Problem 2 (Sum of local peaks above average)

nums = [8, 15, 10, 18, 7, 20, 12]

# First find the average of the list.
#
# Then find all local peaks that are
# greater than the average.
#
# Print the sum of those peak values.

total = 0

for n in nums:
    total += n 

average = total / len(nums)

total = 0

for i in range(1, len(nums) - 1):
    if nums[i-1] < nums[i] > nums[i+1]:
        if nums[i] > average:
            total += nums[i]

print(total)

# Problem 3 (Largest local peak above average)

nums = [10, 17, 12, 21, 8, 19, 15]

# First find the average of the list.
#
# Then find the largest local peak
# that is greater than the average.
#
# Print:
# 1. The value
# 2. Its index

total = 0

for n in nums:
    total += n

average = total / len(nums)
largest = float("-inf")
index = 0

for i in range(1, len(nums) - 1):
    if nums[i-1] < nums[i] > nums[i+1]:
        if nums[i] > average:
            if nums[i] > largest:
                largest = nums[i]
                index = i

print(largest, index) 

# Problem 4 (Smallest increasing difference)

nums = [7, 12, 9, 15, 18, 10, 13]

# Whenever a number is larger than the previous one,
# calculate the difference.
#
# Examples:
# 7 -> 12   difference = 5
# 9 -> 15   difference = 6
# 15 -> 18  difference = 3
# 10 -> 13  difference = 3
#
# Task:
# Find the smallest increasing difference.
#
# Print the value.

smallest = float("inf")

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        diff = nums[i] - nums[i-1]
        if diff < smallest:
            smallest = diff

print(smallest)

# Problem 5 (Index of the smallest increasing difference)

nums = [7, 12, 9, 15, 18, 10, 13]

# Whenever a number is larger than the previous one,
# calculate the difference.
#
# Task:
# Find the starting index of the
# smallest increasing difference.
#
# Print the index.

smallest = float("inf")
index = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        diff = nums[i] - nums[i-1]
        if diff < smallest:
            smallest = diff
            index = i-1

print(index)

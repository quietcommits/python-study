# Problem 1 (index of the largest odd number)

nums = [18, 7, 25, 14, 31, 10, 19]

# Task:
# Find the index of the largest odd number.
#
# Print the index.
#
# You may assume there is at least one odd number.

largest = float("-inf")
index = 0

for i in range(len(nums)):
    if nums[i] % 2 == 1:
        if nums[i] > largest:
            largest = nums[i]
            index = i

print(index)

# Problem 2 (Second largest even number)

nums = [14, 8, 21, 30, 18, 5, 26]

# Task:
# Find the second largest even number.
#
# Print the value.
#
# You may assume there are at least two even numbers.

largest = float("-inf")
second_largest = float("-inf")

for n in nums:
    if n % 2 == 0:
        if n > largest:
            second_largest = largest
            largest = n
        elif n > second_largest:
            second_largest = n

print(second_largest)

# Problem 3 (Closest even number to 50)

nums = [41, 52, 48, 35, 60, 46, 29]

# Task:
# Find the even number closest to 50.
#
# Print:
# 1. The value
# 2. Its index
#
# You may assume there is only one correct answer.

smallest = float("inf")

for i in range(len(nums)):
    if nums[i] % 2 == 0:
        if abs(nums[i] - 50) < smallest:
            smallest = abs(nums[i] - 50)
            value = nums[i]
            index = i

print(value, index)

# Problem 4 (Largest gap between consecutive numbers)

nums = [5, 12, 9, 20, 18, 30]

# The gap between consecutive numbers is:
#
# |12 - 5| = 7
# |9 - 12| = 3
# |20 - 9| = 11
# |18 - 20| = 2
# |30 - 18| = 12
#
# Task:
# Find the largest gap.
#
# Print the value.

largest = float("-inf")

for i in range(1, len(nums)):
    if abs(nums[i] - nums[i-1]) > largest:
        largest = abs(nums[i] - nums[i - 1])

print(largest)

# Problem 5 (Index of the largest gap)

nums = [5, 12, 9, 20, 18, 30]

# Task:
# Find the starting index of the largest gap
# between consecutive numbers.
#
# Example:
# Largest gap is:
# |30 - 18| = 12
#
# Starting index = 4
#
# Print the index.

largest = float("-inf")

for i in range(1, len(nums)):
    if abs(nums[i] - nums[i - 1]) > largest:
        largest = abs(nums[i] - nums[i - 1])
        index = i - 1

print(index)

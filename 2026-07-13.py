# Problem 1 (Largest increasing streak average)

nums = [2, 5, 8, 4, 7, 10, 13, 6]

# An increasing streak is a sequence of
# consecutive numbers where each number
# is larger than the previous one.
#
# Example:
#
# 2, 5, 8        average = 5.0
# 4, 7, 10, 13   average = 8.5
# 6              average = 6.0
#
# Task:
# Find the LARGEST streak average.
#
# Print the average.

streak = 1
total = nums[0]
average = -1
largest_average = float("-inf")

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        streak += 1
        total += nums[i]
    else:
        average = total / streak
        streak = 1
        total = nums[i]
    if average > largest_average:
        largest_average = average

average = total / streak
if average > largest_average:
    largest_average = average

print(largest_average)

# Problem 2 (Smallest increasing streak average)

nums = [3, 6, 9, 2, 4, 1, 5, 8]

# An increasing streak is a sequence of
# consecutive numbers where each number
# is larger than the previous one.
#
# Task:
# Find the SMALLEST streak average.
#
# Print the average.

streak = 1
total = nums[0]
average = -1
smallest = float("inf")

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        streak += 1
        total += nums[i]
    else:
        average = total / streak
        if average < smallest: 
            smallest = average
        streak = 1
        total = nums[i]

average = total / streak
if average < smallest:
    smallest = average

print(smallest)

# Problem 3 (Largest decreasing streak average)

nums = [10, 7, 4, 12, 9, 5, 3, 8]

# A decreasing streak is a sequence of
# consecutive numbers where each number
# is smaller than the previous one.
#
# Example:
#
# 10, 7, 4      average = 7.0
# 12, 9, 5, 3   average = 7.25
# 8             average = 8.0
#
# Task:
# Find the LARGEST streak average.
#
# Print the average.

streak = 1
average = -1
largest = float("-inf")
total = nums[0]

for i in range(1, len(nums)):
    if nums[i] < nums[i-1]:
        streak += 1
        total += nums[i]
    else:
        average = total / streak
        if average > largest:
            largest = average
        streak = 1
        total = nums[i]

average = total / streak
if average > largest:
        largest = average

print(largest)

# Problem 4 (Smallest decreasing streak average)

nums = [15, 12, 8, 10, 6, 4, 9]

# A decreasing streak is a sequence of
# consecutive numbers where each number
# is smaller than the previous one.
#
# Task:
# Find the SMALLEST streak average.
#
# Print the average.

streak = 1
total = nums[0]
average = -1
smallest = float("inf")

for i in range(1, len(nums)):
    if nums[i] < nums[i-1]:
        streak += 1
        total += nums[i]
    else:
        average = total / streak
        if average < smallest:
            smallest = average
        streak = 1
        total = nums[i]

average = total / streak
if average < smallest:
    smallest = average

print(smallest)

# Problem 5 (Starting value of the decreasing streak with the largest average)

nums = [14, 10, 7, 15, 12, 9, 6, 11]

# A decreasing streak is a sequence of
# consecutive numbers where each number
# is smaller than the previous one.
#
# Task:
# Print the STARTING VALUE of the
# decreasing streak that has the
# LARGEST average.
#
# Example:
#
# 14, 10, 7      average = 31/3 ≈ 10.33
# 15, 12, 9, 6   average = 42/4 = 10.5
# 11             average = 11.0
#
# Output:
# 11

streak = 1
total = nums[0]
average = -1
largest = float("-inf")
start = nums[0]
largest_start = nums[0]

for i in range(1, len(nums)):
    if nums[i] < nums[i-1]:
        streak += 1
        total += nums[i]
    else:
        average = total / streak
        if average > largest:
            largest = average
            largest_start = start
        streak = 1
        total = nums[i]
        start = nums[i]

average = total / streak
if average > largest:
    largest = average
    largest_start = start

print(largest_start)

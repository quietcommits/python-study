# Problem 1 (Longest increasing streak with sum at least 20)

nums = [3, 5, 8, 4, 6, 9, 2, 7, 10]

# An increasing streak is a sequence of
# consecutive numbers where each number
# is larger than the previous one.
#
# Task:
# Among increasing streaks whose SUM
# is at least 20,
# find the LONGEST length.
#
# Example:
#
# 3, 5, 8      length = 3, sum = 16  (ignore)
# 4, 6, 9      length = 3, sum = 19  (ignore)
# 2, 7, 10     length = 3, sum = 19  (ignore)
#
# Output:
# 0
#
# (No streak has sum >= 20.)

streak = 1
longest = 0
total = nums[0]

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        streak += 1
        total += nums[i]
    else:
        if total >= 20:
            if streak > longest:
                longest = streak
        streak = 1
        total = nums[i]

if total >= 20:
    if streak > longest:
        longest = streak

print(longest)

# Problem 2 (Largest increasing streak sum with length at least 3)

nums = [2, 5, 8, 4, 6, 9, 12, 3]

# An increasing streak is a sequence of
# consecutive numbers where each number
# is larger than the previous one.
#
# Task:
# Among increasing streaks whose LENGTH
# is at least 3,
# find the LARGEST SUM.
#
# Example:
#
# 2, 5, 8          length = 3, sum = 15
# 4, 6, 9, 12      length = 4, sum = 31
# 3                length = 1 (ignore)
#
# Output:
# 31

streak = 1
total = nums[0]
largest = float("-inf")

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        streak += 1
        total += nums[i]
    else:
        if streak >= 3:
            if total > largest:
                largest = total
        streak = 1
        total = nums[i]

if streak >= 3:
    if total > largest:
        largest = total

print(largest)

# Problem 3 (Smallest decreasing streak average with length at least 2)

nums = [12, 9, 6, 10, 8, 7, 15]

# A decreasing streak is a sequence of
# consecutive numbers where each number
# is smaller than the previous one.
#
# Task:
# Among decreasing streaks whose LENGTH
# is at least 2,
# find the SMALLEST AVERAGE.
#
# Example:
#
# 12, 9, 6      length = 3, average = 9.0
# 10, 8, 7      length = 3, average = 25/3 ≈ 8.33
# 15            length = 1 (ignore)
#
# Output:
# 8.333333333333334

streak = 1
total = nums[0]
smallest = float("inf")

for i in range(1, len(nums)):
    if nums[i] < nums[i-1]:
        streak += 1
        total += nums[i]
    else:
        if streak >= 2:
            average = total / streak
            if average < smallest:
                smallest = average
        streak = 1
        total = nums[i]

if streak >= 2:
    average = total / streak
    if average < smallest:
        smallest = average

print(smallest)

# Problem 4 (Starting value of the increasing streak with the largest sum,
#             where the length is at least 3)

nums = [3, 6, 9, 2, 5, 8, 11, 4]

# An increasing streak is a sequence of
# consecutive numbers where each number
# is larger than the previous one.
#
# Task:
# Among increasing streaks whose LENGTH
# is at least 3,
# print the STARTING VALUE of the streak
# with the LARGEST SUM.
#
# Example:
#
# 3, 6, 9         length = 3, sum = 18
# 2, 5, 8, 11     length = 4, sum = 26
# 4               length = 1 (ignore)
#
# Output:
# 2

streak = 1
total = nums[0]
largest = float("-inf")
largest_value = nums[0]
value = nums[0]

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        streak += 1
        total += nums[i]
    else:
        if streak >= 3:
            if total > largest:
                largest = total
                largest_value = value
        streak = 1
        total = nums[i]
        value = nums[i]

if streak >= 3:
    if total > largest:
        largest = total
        largest_value = value

print(largest_value)

# Problem 5 (Ending index of the decreasing streak with the smallest average,
#             where the length is at least 2)

nums = [15, 12, 8, 14, 10, 7, 5, 11]

# A decreasing streak is a sequence of
# consecutive numbers where each number
# is smaller than the previous one.
#
# Task:
# Among decreasing streaks whose LENGTH
# is at least 2,
# print the ENDING INDEX of the streak
# with the SMALLEST AVERAGE.
#
# Example:
#
# 15, 12, 8      average = 35/3 ≈ 11.67 (ends at index 2)
# 14, 10, 7, 5   average = 9.0          (ends at index 6)
# 11             length = 1 (ignore)
#
# Output:
# 6

streak = 1
total = nums[0]
index = 0
smallest = float("inf")
smallest_index = 0

for i in range(1, len(nums)):
    if nums[i] < nums[i-1]:
        streak += 1
        total += nums[i]
        index = i
    else:
        if streak >= 2:
            average = total / streak
            if average < smallest:
                smallest = average
                smallest_index = index
        streak = 1
        total = nums[i]
        index = i

if streak >= 2:
    average = total / streak
    if average < smallest:
        smallest = average
        smallest_index = index

print(smallest_index)

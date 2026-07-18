# Problem 1 (Longest increasing streak with average at least 8)

nums = [3, 6, 9, 4, 8, 10, 12, 5]

# An increasing streak is a sequence of
# consecutive numbers where each number
# is larger than the previous one.
#
# Task:
# Among increasing streaks whose AVERAGE
# is at least 8,
# find the LONGEST length.
#
# Example:
#
# 3, 6, 9         average = 6.0   (ignore)
# 4, 8, 10, 12    average = 8.5   length = 4
# 5               average = 5.0   (ignore)
#
# Output:
# 4

streak = 1
longest = 0
total = nums[0]

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        streak += 1
        total += nums[i]
    else:
        average = total / streak
        if average >= 8:
            if streak > longest:
                longest = streak
        streak = 1
        total = nums[i]

average = total / streak
if average >= 8:
    if streak > longest:
        longest = streak

print(longest)

# Problem 2 (Largest decreasing streak sum with average at most 10)

nums = [15, 12, 9, 14, 10, 7, 5, 13]

# A decreasing streak is a sequence of
# consecutive numbers where each number
# is smaller than the previous one.
#
# Task:
# Among decreasing streaks whose AVERAGE
# is at most 10,
# find the LARGEST SUM.
#
# Example:
#
# 15, 12, 9       average = 12.0 (ignore)
# 14, 10, 7, 5    average = 9.0  sum = 36
# 13              average = 13.0 (ignore)
#
# Output:
# 36

streak = 1
total = nums[0]
largest = float("-inf")

for i in range(1, len(nums)):
    if nums[i] < nums[i-1]:
        streak += 1
        total += nums[i]
    else:
        average = total / streak
        if average <= 10:
            if total > largest:
                largest = total
        streak = 1
        total = nums[i]

average = total / streak
if average <= 10:
    if total > largest:
        largest = total

print(largest)

# Problem 3 (Starting value of the increasing streak with the largest sum,
#             where length >= 3 and average >= 8)

nums = [3, 7, 10, 2, 8, 10, 12, 5]

# An increasing streak is a sequence of
# consecutive numbers where each number
# is larger than the previous one.
#
# Task:
# Among increasing streaks whose
# LENGTH is at least 3
# AND whose AVERAGE is at least 8,
# print the STARTING VALUE of the streak
# with the LARGEST SUM.
#
# Example:
#
# 3, 7, 10        length=3 average≈6.67 (ignore)
# 2, 8, 10, 12    length=4 average=8.0  sum=32
# 5               ignore
#
# Output:
# 2

streak = 1
total = nums[0]
largest = float("-inf")
value = nums[0]
largest_value = nums[0]

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        streak += 1
        total += nums[i]
    else:
        average = total / streak
        if streak >= 3 and average >= 8:
            if total > largest:
                largest = total
                largest_value = value
        streak = 1
        total = nums[i]
        value = nums[i]

average = total / streak
if streak >= 3 and average >= 8:
    if total > largest:
        largest = total
        largest_value = value

print(largest_value)

# Problem 4 (Ending index of the decreasing streak with the smallest average,
#             where length >= 3 and sum >= 20)

nums = [16, 13, 9, 12, 10, 7, 4, 15]

# A decreasing streak is a sequence of
# consecutive numbers where each number
# is smaller than the previous one.
#
# Task:
# Among decreasing streaks whose
# LENGTH is at least 3
# AND whose SUM is at least 20,
# print the ENDING INDEX of the streak
# with the SMALLEST AVERAGE.
#
# Example:
#
# 16, 13, 9       length=3 sum=38 average≈12.67 (ends at index 2)
# 12, 10, 7, 4    length=4 sum=33 average=8.25  (ends at index 6)
# 15              ignore
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
        average = total / streak
        if streak >= 3 and total >= 20:
            if average < smallest:
                smallest = average
                smallest_index = index
        streak = 1
        total = nums[i]
        index = i

average = total / streak
if streak >= 3 and total >= 20:
    if average < smallest:
        smallest = average
        smallest_index = index   

print(smallest_index)

# Problem 5 (Starting value of the increasing streak with the largest average,
#             where length >= 3 and sum >= 25)

nums = [4, 8, 10, 3, 7, 10, 12, 5]

# An increasing streak is a sequence of
# consecutive numbers where each number
# is larger than the previous one.
#
# Task:
# Among increasing streaks whose
# LENGTH is at least 3
# AND whose SUM is at least 25,
# print the STARTING VALUE of the streak
# with the LARGEST AVERAGE.
#
# Example:
#
# 4, 8, 10        length=3 sum=22 (ignore)
# 3, 7, 10, 12    length=4 sum=32 average=8.0
# 5               ignore
#
# Output:
# 3

streak = 1
total = nums[0]
value = nums[0]
largest = float("-inf")
largest_value = nums[0]

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        streak += 1
        total += nums[i]
    else:
        average = total / streak
        if streak >= 3 and total >= 25:
            if average > largest:
                largest = average
                largest_value = value
        streak = 1
        total = nums[i]
        value = nums[i]

average = total / streak
if streak >= 3 and total >= 25:
    if average > largest:
        largest = average
        largest_value = value

print(largest_value)

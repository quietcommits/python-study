# Problem 1 (Longest increasing streak with sum greater than 20)

nums = [2, 5, 8, 3, 6, 10, 15, 4]

# An increasing streak is a sequence of
# consecutive numbers where each number
# is larger than the previous one.
#
# Task:
# Among increasing streaks whose SUM
# is greater than 20,
# find the LONGEST LENGTH.
#
# Example:
#
# 2, 5, 8       length=3 sum=15    (ignore)
# 3, 6, 10, 15  length=4 sum=34    (count)
# 4             ignore
#
# Output:
# 4

streak = 1
total = nums[0]
longest = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        streak += 1
        total += nums[i]
    else:
        if total > 20:
            if streak > longest:
                longest = streak
        streak = 1
        total = nums[i]

if total > 20:
    if streak > longest:
        longest = streak

print(longest)

# Problem 2 (Largest sum of decreasing streaks
#            with length exactly 3)

nums = [15, 12, 9, 14, 10, 7, 5, 3]

# A decreasing streak is a sequence of
# consecutive numbers where each number
# is smaller than the previous one.
#
# Task:
# Among decreasing streaks whose LENGTH
# is exactly 3,
# find the LARGEST SUM.
#
# Example:
#
# 15, 12, 9      length=3 sum=36
# 14, 10, 7, 5,3 length=5 (ignore)
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
        if streak == 3:
            if total > largest:
                largest = total
        streak = 1
        total = nums[i]

if streak == 3:
    if total > largest:
        largest = total

print(largest)

# Problem 3 (Largest sum of increasing streaks
#            with length exactly 3)

nums = [2, 5, 8, 10, 3, 6, 9, 12]

# An increasing streak is a sequence of
# consecutive numbers where each number
# is larger than the previous one.
#
# Task:
# Find the LARGEST SUM among all
# increasing streaks with LENGTH exactly 3.
#
# Example:
#
# 2, 5, 8, 10      length=4
# 5, 8, 10         length=3 sum=23
# 3, 6, 9, 12      length=4
# 6, 9, 12         length=3 sum=27
#
# Output:
# 27

streak = 1
total = nums[0]
largest = float("-inf")

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        streak += 1
        total += nums[i]
        if streak >= 3:
            window_sum = nums[i] + nums[i-1] + nums[i-2]
            if window_sum > largest:
                largest = window_sum
    else:
        streak = 1
        total = nums[i]

print(largest)

# Problem 4 (Smallest average of decreasing streaks
#            with length exactly 3)

nums = [15, 12, 9, 7, 14, 10, 6, 3]

# A decreasing streak is a sequence of
# consecutive numbers where each number
# is smaller than the previous one.
#
# Task:
# Find the SMALLEST AVERAGE among all
# decreasing streaks with LENGTH exactly 3.
#
# Example:
#
# 15, 12, 9, 7
#
# length=3 windows:
#
# 15,12,9   average = 12
# 12,9,7    average = 9.333...
#
# 14,10,6,3
#
# length=3 windows:
#
# 14,10,6   average = 10
# 10,6,3    average = 6.333...
#
# Output:
# 6.333333333333333

streak = 1
total = nums[0]
smallest = float("inf")

for i in range(1, len(nums)):
    if nums[i] < nums[i-1]:
        streak += 1
        total += nums[i]
        if streak >= 3:
            total = nums[i] + nums[i-1] + nums[i-2]
            average = total / 3
            if average < smallest:
                smallest = average
    else:
        streak = 1
        total = nums[i]

print(smallest)

# Problem 5 (Starting index of increasing streaks
#            with length exactly 3 and largest sum)

nums = [2, 5, 8, 10, 3, 6, 9, 12]

# An increasing streak is a sequence of
# consecutive numbers where each number
# is larger than the previous one.
#
# Task:
# Find the STARTING INDEX of the
# length exactly 3 increasing streak
# with the LARGEST SUM.
#
# Example:
#
# 2,5,8       sum=15 start index=0
# 5,8,10      sum=23 start index=1
# 3,6,9       sum=18 start index=4
# 6,9,12      sum=27 start index=5
#
# Output:
# 5

streak = 1
index = 0
largest = float("-inf")
largest_index = -1

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        streak += 1
        if streak >= 3:
            total = nums[i] + nums[i-1] + nums[i-2]
            if total > largest:
                largest = total
                largest_index = i-2
    else:
        streak = 1

print(largest_index)

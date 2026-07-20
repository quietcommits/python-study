# Problem 1 (Sum of increasing streak sums with length at least 3)

nums = [3, 6, 9, 2, 5, 8, 11, 4]

# An increasing streak is a sequence of
# consecutive numbers where each number
# is larger than the previous one.
#
# Task:
# Find the SUM of the sums of all
# increasing streaks whose LENGTH
# is at least 3.
#
# Example:
#
# 3, 6, 9         sum = 18
# 2, 5, 8, 11     sum = 26
# 4               ignore
#
# Output:
# 44

streak = 1
total = nums[0]
answer = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        streak += 1
        total += nums[i]
    else:
        if streak >= 3:
            answer += total
        streak = 1
        total = nums[i]

if streak >= 3:
    answer += total

print(answer)

# Problem 2 (Sum of decreasing streak averages with length at least 2)

nums = [12, 9, 6, 10, 8, 7, 15]

# A decreasing streak is a sequence of
# consecutive numbers where each number
# is smaller than the previous one.
#
# Task:
# Find the SUM of the averages of all
# decreasing streaks whose LENGTH
# is at least 2.
#
# Example:
#
# 12, 9, 6      average = 9.0
# 10, 8, 7      average = 25/3 ≈ 8.333333333333334
# 15            ignore
#
# Output:
# 17.333333333333336

streak = 1
total = nums[0]
answer = 0

for i in range(1, len(nums)):
    if nums[i] < nums[i-1]:
        streak += 1
        total += nums[i]
    else:
        if streak >= 2:
            average = total / streak
            answer += average
        streak = 1
        total = nums[i]

if streak >= 2:
    average = total / streak
    answer += average

print(answer)

# Problem 3 (Sum of starting values of increasing streaks
#            with sum at least 20)

nums = [3, 6, 9, 2, 5, 8, 11, 4]

# An increasing streak is a sequence of
# consecutive numbers where each number
# is larger than the previous one.
#
# Task:
# Find the SUM of the STARTING VALUES
# of all increasing streaks whose
# SUM is at least 20.
#
# Example:
#
# 3, 6, 9         sum = 18  (ignore)
# 2, 5, 8, 11     sum = 26  (start = 2)
# 4               sum = 4   (ignore)
#
# Output:
# 2

total = nums[0]
value = nums[0]
answer = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        total += nums[i]
    else:
        if total >= 20:
            answer += value
        total = nums[i]
        value = nums[i]

if total >= 20:
    answer += value

print(answer)

# Problem 4 (Sum of ending values of decreasing streaks
#            with average at most 8)

nums = [10, 7, 4, 12, 9, 6, 3, 8]

# A decreasing streak is a sequence of
# consecutive numbers where each number
# is smaller than the previous one.
#
# Task:
# Find the SUM of the ENDING VALUES
# of all decreasing streaks whose
# AVERAGE is at most 8.
#
# Example:
#
# 10, 7, 4       average = 7.0   (end = 4)
# 12, 9, 6, 3    average = 7.5   (end = 3)
# 8              average = 8.0   (end = 8)
#
# Output:
# 15

streak = 1
total = nums[0]
value = nums[0]
answer = 0

for i in range(1, len(nums)):
    if nums[i] < nums[i-1]:
        streak += 1
        total += nums[i]
        value = nums[i]
    else:
        average = total / streak
        if average <= 8:
            answer += value
        streak = 1
        total = nums[i]
        value = nums[i]

average = total / streak
if average <= 8:
    answer += value

print(answer)

# Problem 5 (Count increasing EVEN streaks
#            with length at least 3 and sum at least 25)

nums = [2, 4, 6, 5, 8, 10, 12, 7, 14, 16, 18]

# An increasing EVEN streak is a sequence of
# consecutive EVEN numbers where each number
# is larger than the previous one.
#
# Task:
# Count how many increasing EVEN streaks have:
#
# 1. LENGTH at least 3
# 2. SUM at least 25
#
# Example:
#
# 2, 4, 6       length=3 sum=12   (ignore)
# 8, 10, 12     length=3 sum=30   (count)
# 14, 16, 18    length=3 sum=48   (count)
#
# Output:
# 2

streak = 0
total = 0
count = 0

if nums[0] % 2 == 0:
    streak = 1
    total = nums[0]

for i in range(1, len(nums)):
    if nums[i] % 2 == 0:
        if nums[i] > nums[i-1]:
            streak += 1
            total += nums[i]
        else:
            if streak >= 3 and total >= 25:
                count += 1
            streak = 1
            total = nums[i]
    else:
        if streak >= 3 and total >= 25:
            count += 1
        streak = 0
        total = 0

if streak >= 3 and total >= 25:
    count += 1

print(count)

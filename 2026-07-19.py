# Problem 1 (Count increasing streaks with sum at least 20)

nums = [3, 6, 9, 2, 5, 8, 11, 4]

# An increasing streak is a sequence of
# consecutive numbers where each number
# is larger than the previous one.
#
# Task:
# Count how many increasing streaks
# have a SUM of at least 20.
#
# Example:
#
# 3, 6, 9        sum = 18  (ignore)
# 2, 5, 8, 11    sum = 26  (count)
# 4              sum = 4   (ignore)
#
# Output:
# 1

streak = 1
total = nums[0]
count = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        streak += 1
        total += nums[i]
    else:
        if total >= 20:
            count += 1
        streak = 1
        total = nums[i]

if total >= 20:
    count += 1

print(count)

# Problem 2 (Count decreasing streaks with average at most 8)

nums = [10, 7, 4, 12, 9, 6, 3, 8]

# A decreasing streak is a sequence of
# consecutive numbers where each number
# is smaller than the previous one.
#
# Task:
# Count how many decreasing streaks
# have an AVERAGE of at most 8.
#
# Example:
#
# 10, 7, 4       average = 7.0   (count)
# 12, 9, 6, 3    average = 7.5   (count)
# 8              average = 8.0   (count)
#
# Output:
# 3

streak = 1
total = nums[0]
count = 0

for i in range(1, len(nums)):
    if nums[i] < nums[i-1]:
        streak += 1
        total += nums[i]
    else:
        average = total / streak
        if average <= 8:
            count += 1
        streak = 1
        total = nums[i]

average = total / streak
if average <= 8:
    count += 1

print(count)

# Problem 3 (Count increasing EVEN streaks with length at least 3)

nums = [2, 4, 6, 5, 8, 10, 12, 7, 14, 16]

# An increasing EVEN streak is a sequence of
# consecutive EVEN numbers where each number
# is larger than the previous one.
#
# Task:
# Count how many increasing EVEN streaks
# have a LENGTH of at least 3.
#
# Example:
#
# 2, 4, 6        length = 3  (count)
# 8, 10, 12      length = 3  (count)
# 14, 16         length = 2  (ignore)
#
# Output:
# 2

streak = 0
count = 0

if nums[0] % 2 == 0:
    streak = 1

for i in range(1, len(nums)):
    if nums[i] % 2 == 0:
        if nums[i] > nums[i-1]:
            streak += 1
        else:
            if streak >= 3:
                count += 1
            streak = 1
    else:
        if streak >= 3:
            count += 1
        streak = 0

if streak >= 3:
    count += 1

print(count)

# Problem 4 (Count decreasing ODD streaks with sum at least 15)

nums = [11, 9, 7, 8, 13, 11, 5, 4, 15]

# A decreasing ODD streak is a sequence of
# consecutive ODD numbers where each number
# is smaller than the previous one.
#
# Task:
# Count how many decreasing ODD streaks
# have a SUM of at least 15.
#
# Example:
#
# 11, 9, 7       sum = 27  (count)
# 13, 11, 5      sum = 29  (count)
# 15             sum = 15  (count)
#
# Output:
# 3

count = 0
total = 0
streak = 0


for i in range(len(nums)):
    if nums[i] % 2 == 1:
        if streak > 0 and nums[i] < nums[i-1]:
            total += nums[i]
            streak += 1
        else:
            if total >= 15:
                count += 1
            total = nums[i]
            streak = 1
    else:
        if total >= 15:
            count += 1
        total = 0
        streak = 0

if total >= 15:
    count += 1

print(count)

# Problem 5 (Count increasing streaks
#             with length at least 3 and average at least 7)

nums = [2, 5, 8, 3, 6, 9, 12, 4, 10, 13]

# An increasing streak is a sequence of
# consecutive numbers where each number
# is larger than the previous one.
#
# Task:
# Count how many increasing streaks have:
#
# 1. LENGTH at least 3
# 2. AVERAGE at least 7
#
# Example:
#
# 2, 5, 8          length=3 average=5.0   (ignore)
# 3, 6, 9, 12      length=4 average=7.5   (count)
# 4, 10, 13        length=3 average=9.0   (count)
#
# Output:
# 2

streak = 1
total = nums[0]
count = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        streak += 1
        total += nums[i]
    else:
        average = total / streak
        if streak >= 3 and average >= 7:
            count += 1
        streak = 1
        total = nums[i]

average = total / streak
if streak >= 3 and average >= 7:
    count += 1

print(count)

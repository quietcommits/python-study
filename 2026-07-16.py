# Problem 1 (Largest average of an increasing EVEN streak)

nums = [2, 4, 6, 5, 8, 10, 12, 7]

# An increasing EVEN streak is a sequence of
# consecutive EVEN numbers where each number
# is larger than the previous one.
#
# Task:
# Find the LARGEST AVERAGE among all
# increasing EVEN streaks.
#
# Example:
#
# 2, 4, 6        average = 4.0
# 8, 10, 12      average = 10.0
#
# Print the average.

total = nums[0]
streak = 0
average = -1
largest = float("-inf")

if nums[0] % 2 == 0:
    streak = 1

for i in range(1, len(nums)):
    if nums[i] % 2 == 0:
        if nums[i] > nums[i-1]:
            total += nums[i]
            streak += 1
        else:
            average = total / streak
            if average > largest:
                largest = average
            total = nums[i]
            streak = 1
    else:
        if streak > 0:
            average = total / streak
            if average > largest:
                largest = average
        total = 0
        streak = 0

if streak > 0:
    average = total / streak
    if average > largest:
        largest = average

print(largest)

# Problem 2 (Smallest average of a decreasing ODD streak)

nums = [9, 7, 5, 8, 11, 9, 7, 6]

# A decreasing ODD streak is a sequence of
# consecutive ODD numbers where each number
# is smaller than the previous one.
#
# Task:
# Find the SMALLEST AVERAGE among all
# decreasing ODD streaks.
#
# Example:
#
# 9, 7, 5        average = 7.0
# 11, 9, 7       average = 9.0
#
# Print the average.

streak = 0
smallest = float("inf")
total = 0

if nums[0] % 2 == 1:
    streak = 1
    total = nums[0]

for i in range(1, len(nums)):
    if nums[i] % 2 == 1:
        if nums[i] < nums[i-1]:
            streak += 1
            total += nums[i]
        else:
            if streak > 0:
                average = total / streak
                if average < smallest:
                    smallest = average
            streak = 1
            total = nums[i]
    else:
        if streak > 0:
            average = total / streak
            if average < smallest:
                smallest = average
        streak = 0
        total = 0

if streak > 0:
    average = total / streak
    if average < smallest:
        smallest = average

print(smallest)

# Problem 3 (Starting value of the increasing EVEN streak with the largest average)

nums = [2, 4, 6, 5, 8, 10, 12, 7]

# An increasing EVEN streak is a sequence of
# consecutive EVEN numbers where each number
# is larger than the previous one.
#
# Task:
# Print the STARTING VALUE of the
# increasing EVEN streak that has the
# LARGEST AVERAGE.
#
# Example:
#
# 2, 4, 6        average = 4.0
# 8, 10, 12      average = 10.0
#
# Output:
# 8

streak = 0
total = 0
largest = float("-inf")
value = nums[0]
largest_value = nums[0]

if nums[0] % 2 == 0:
    streak = 1
    total = nums[0]

for i in range(1, len(nums)):
    if nums[i] % 2 == 0:
        if streak == 0:
            value = nums[i]
            streak = 1
            total = nums[i]
        else:
            if nums[i] > nums[i-1]:
                streak += 1
                total += nums[i]
            else:
                average = total / streak
                if average > largest:
                    largest = average
                    largest_value = value
                streak = 1
                total = nums[i]
                value = nums[i]
    else:
        if streak > 0:
            average = total / streak
            if average > largest:
                largest = average
                largest_value = value
        streak = 0 
        total = 0

if streak > 0:
    average = total / streak
    if average > largest:
        largest = average
        largest_value = value

print(largest_value)

# Problem 4 (Ending value of the decreasing ODD streak with the smallest average)

nums = [11, 9, 7, 10, 13, 11, 5, 8]

# A decreasing ODD streak is a sequence of
# consecutive ODD numbers where each number
# is smaller than the previous one.
#
# Task:
# Print the ENDING VALUE of the
# decreasing ODD streak that has the
# SMALLEST AVERAGE.
#
# Example:
#
# 11, 9, 7       average = 9.0   (ends with 7)
# 13, 11, 5      average = 29/3 ≈ 9.67 (ends with 5)
#
# Output:
# 7

streak = 0
total = 0
smallest = float("inf")
value = nums[0]
smallest_value = nums[0]

if nums[0] % 2 == 1:
    streak = 1
    total = nums[0]

for i in range(1, len(nums)):
    if nums[i] % 2 == 1:
        if nums[i] < nums[i-1]:
            streak += 1
            total += nums[i]
            value = nums[i]
        else:
            if streak > 0:
                average = total / streak
                if average < smallest:
                    smallest = average
                    smallest_value = value
            streak = 1
            total = nums[i]
            value = nums[i]
    else:
        if streak > 0:
            average = total / streak
            if average < smallest:
                smallest = average
                smallest_value = value
        streak = 0 
        total = 0

if streak > 0:
    average = total / streak
    if average < smallest:
        smallest = average
        smallest_value = value

print(smallest_value)

# Problem 5 (Starting index of the increasing EVEN streak with the largest average)

nums = [2, 4, 6, 5, 8, 10, 12, 7]

# An increasing EVEN streak is a sequence of
# consecutive EVEN numbers where each number
# is larger than the previous one.
#
# Task:
# Print the STARTING INDEX of the
# increasing EVEN streak that has the
# LARGEST AVERAGE.
#
# Example:
#
# 2, 4, 6        average = 4.0   (starts at index 0)
# 8, 10, 12      average = 10.0  (starts at index 4)
#
# Output:
# 4

streak = 0
total = 0
largest = float("-inf")
index = 0
largest_index = 0

if nums[0] % 2 == 0:
    streak = 1
    total = nums[0]
    index = 0
    largest_index = 0

for i in range(1, len(nums)):
    if nums[i] % 2 == 0:
        if streak == 0:
            streak = 1
            total = nums[i]
            index = i
        else:
            if nums[i] > nums[i-1]:
                streak += 1
                total += nums[i]
            else:
                average = total / streak
                if average > largest:
                    largest = average
                    largest_index = index
                streak = 1
                total = nums[i]
                index = i
    else:
        if streak > 0:
            average = total / streak
            if average > largest:
                largest = average
                largest_index = index
        streak = 0
        total = 0

if streak > 0:
    average = total / streak
    if average > largest:
        largest = average
        largest_index = index

print(largest_index)

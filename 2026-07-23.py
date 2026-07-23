# Problem 1 (Largest sum of every 
#            consecutive 5 numbers)

nums = [4, 7, 2, 9, 5, 8, 3, 6]

# Task:
# Find the LARGEST SUM among every
# consecutive 5 numbers.
#
# Example:
#
# 4,7,2,9,5   sum = 27
# 7,2,9,5,8   sum = 31
# 2,9,5,8,3   sum = 27
# 9,5,8,3,6   sum = 31
#
# Output:
# 31

largest = float("-inf")

for i in range(4, len(nums)):
    total = nums[i] + nums[i-1] + nums[i-2] + nums[i-3] + nums[i-4]
    if total > largest:
        largest = total

print(largest)

# Problem 2 (Smallest average of every consecutive 4 numbers)

nums = [10, 6, 8, 3, 9, 4, 7, 2]

# Task:
# Find the SMALLEST AVERAGE among every
# consecutive 4 numbers.
#
# Example:
#
# 10,6,8,3   average = 27/4 = 6.75
# 6,8,3,9    average = 26/4 = 6.5
# 8,3,9,4    average = 24/4 = 6.0
# 3,9,4,7    average = 23/4 = 5.75
# 9,4,7,2    average = 22/4 = 5.5
#
# Output:
# 5.5

smallest = float("inf")

for i in range(3, len(nums)):
    total = nums[i] + nums[i-1] + nums[i-2] + nums[i-3]
    average = total / 4
    if average < smallest:
        smallest = average

print(smallest)

# Problem 3 (Starting index of the consecutive 5 numbers
#            with the largest average)

nums = [3, 8, 4, 10, 6, 9, 2, 7, 5]

# Task:
# Find the STARTING INDEX of the
# consecutive 5 numbers with the
# LARGEST AVERAGE.
#
# Example:
#
# 3,8,4,10,6   average = 31/5 = 6.2  start index = 0
# 8,4,10,6,9   average = 37/5 = 7.4  start index = 1
# 4,10,6,9,2   average = 31/5 = 6.2  start index = 2
# 10,6,9,2,7   average = 34/5 = 6.8  start index = 3
# 6,9,2,7,5    average = 29/5 = 5.8  start index = 4
#
# Output:
# 1

largest = float("-inf")

for i in range(4, len(nums)):
    total = nums[i] + nums[i-1] + nums[i-2] + nums[i-3] + nums[i-4]
    average = total / 5
    if average > largest:
        largest = average
        largest_index = i-4

print(largest_index)

# Problem 4 (Ending value of the consecutive 4 numbers
#            with the smallest sum, where sum is at least 20)

nums = [9, 5, 8, 3, 7, 2, 6, 4]

# Task:
# Among consecutive 4-number windows
# whose SUM is at least 20,
# find the ENDING VALUE of the window
# with the SMALLEST SUM.
#
# Example:
#
# 9,5,8,3   sum = 25  end = 3
# 5,8,3,7   sum = 23  end = 7
# 8,3,7,2   sum = 20  end = 2
# 3,7,2,6   sum = 18  ignore
# 7,2,6,4   sum = 19  ignore
#
# Output:
# 2

smallest = float("inf")

for i in range(3, len(nums)):
    total = nums[i] + nums[i-1] + nums[i-2] + nums[i-3]
    if total >= 20:
        if total < smallest:
            smallest = total
            smallest_value = nums[i]

print(smallest_value)

# Problem 5 (Count consecutive 5-number windows
#            with average greater than 7
#            and remember the largest sum)

nums = [6, 9, 8, 10, 4, 7, 12, 5, 9]

# Task:
# Count how many consecutive 5-number
# windows have:
#
# 1. AVERAGE greater than 7
#
# Also find the LARGEST SUM among
# those valid windows.
#
# Example:
#
# 6,9,8,10,4
# sum = 37
# average = 7.4  (count)
#
# 9,8,10,4,7
# sum = 38
# average = 7.6  (count)
#
# 8,10,4,7,12
# sum = 41
# average = 8.2  (count)
#
# 10,4,7,12,5
# sum = 38
# average = 7.6  (count)
#
# 4,7,12,5,9
# sum = 37
# average = 7.4  (count)
#
# Output:
# count = 5
# largest sum = 41

count = 0
largest = float("-inf")

for i in range(4, len(nums)):
    total = nums[i] + nums[i-1] + nums[i-2] + nums[i-3] + nums[i-4]
    average = total / 5
    if average > 7:
        count += 1
        if total > largest:
            largest = total

print('count =', count)
print('largest sum =', largest)

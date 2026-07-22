# Problem 1 (Largest sum of every consecutive 4 numbers)

nums = [3, 7, 2, 9, 5, 8, 1]

# Task:
# Find the LARGEST SUM among every
# consecutive 4 numbers.
#
# Example:
#
# 3,7,2,9   sum = 21
# 7,2,9,5   sum = 23
# 2,9,5,8   sum = 24
# 9,5,8,1   sum = 23
#
# Output:
# 24

largest = float("-inf")

for i in range(3, len(nums)):
    total = nums[i] + nums[i-1] + nums[i-2] + nums[i-3]
    if total > largest:
        largest = total

print(largest)

# Problem 2 (Smallest average of every consecutive 5 numbers)

nums = [8, 4, 6, 2, 9, 5, 3, 7]

# Task:
# Find the SMALLEST AVERAGE among every
# consecutive 5 numbers.
#
# Example:
#
# 8,4,6,2,9   average = 5.8
# 4,6,2,9,5   average = 5.2
# 6,2,9,5,3   average = 5.0
# 2,9,5,3,7   average = 5.2
#
# Output:
# 5.0

smallest = float("inf")

for i in range(4, len(nums)):
    total = nums[i] + nums[i-1] + nums[i-2] + nums[i-3] + nums[i-4]
    average = total / 5
    if average < smallest:
        smallest = average

print(smallest)

# Problem 3 (Starting index of the consecutive 4 numbers
#            with the largest sum)

nums = [5, 2, 8, 6, 3, 9, 7]

# Task:
# Find the STARTING INDEX of the
# consecutive 4 numbers with the
# LARGEST SUM.
#
# Example:
#
# 5,2,8,6   sum = 21 (start index = 0)
# 2,8,6,3   sum = 19 (start index = 1)
# 8,6,3,9   sum = 26 (start index = 2)
# 6,3,9,7   sum = 25 (start index = 3)
#
# Output:
# 2

largest = float("-inf")
largest_index = 0

for i in range(3, len(nums)):
    total = nums[i] + nums[i-1] + nums[i-2] + nums[i-3]
    if total > largest:
        largest = total
        largest_index = i-3

print(largest_index)

# Problem 4 (Ending value of the consecutive 3 numbers
#            with the smallest sum)

nums = [9, 4, 7, 2, 6, 1, 8]

# Task:
# Find the ENDING VALUE of the
# consecutive 3 numbers with the
# SMALLEST SUM.
#
# Example:
#
# 9,4,7   sum = 20 (ends with 7)
# 4,7,2   sum = 13 (ends with 2)
# 7,2,6   sum = 15 (ends with 6)
# 2,6,1   sum = 9  (ends with 1)
# 6,1,8   sum = 15 (ends with 8)
#
# Output:
# 1

smallest = float("inf")
smallest_value = nums[0]

for i in range(2, len(nums)):
    total = nums[i] + nums[i-1] + nums[i-2]
    if total < smallest:
        smallest = total
        smallest_value = nums[i]

print(smallest_value)

# Problem 5 (Count consecutive 3-number windows
#            whose average is at least 6)

nums = [5, 8, 7, 2, 9, 6, 4]

# Task:
# Count how many consecutive
# 3-number windows have an
# AVERAGE of at least 6.
#
# Example:
#
# 5,8,7   average = 20/3 ≈ 6.67 (count)
# 8,7,2   average = 17/3 ≈ 5.67
# 7,2,9   average = 18/3 = 6.0  (count)
# 2,9,6   average = 17/3 ≈ 5.67
# 9,6,4   average = 19/3 ≈ 6.33 (count)
#
# Output:
# 3

count = 0

for i in range(2, len(nums)):
    total = nums[i] + nums[i-1] + nums[i-2]
    average = total / 3
    if average >= 6:
        count += 1

print(count)

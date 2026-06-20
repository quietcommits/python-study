# Problem 1 (Count increases)

nums = [3, 7, 4, 8, 10, 6]

# Task:
# Count how many times a number is greater
# than the number immediately before it.
#
# Example:
# 3 -> 7 (increase)
# 7 -> 4 (not)
#
# Print the count.

count = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        count += 1

print(count)

# Problem 2 (Smallest positive difference)

nums = [5, 8, 12, 14, 20]

# Task:
# Find the smallest difference between
# neighboring elements.
#
# Example:
# 8 - 5 = 3
# 12 - 8 = 4
#
# Print the smallest difference.

smallest_diff = float("inf")

for i in range(1, len(nums)):
    if nums[i] - nums[i - 1] < smallest_diff:
        smallest_diff = nums[i] - nums[i - 1]

print(smallest_diff)

# Problem 3 (First repeated value)

nums = [4, 2, 7, 3, 2, 8, 7]

# Task:
# Find the first value that appears
# more than once.
#
# Print the value.

seen = []

for n in nums:
    if n in seen:
        print(n)
        break
    seen.append(n)

# Problem 4 (Longest decreasing streak length)

nums = [9, 7, 5, 6, 4, 3, 2, 8]

# A decreasing streak means each next element
# is smaller than the previous one.
#
# Task:
# Find the length of the longest decreasing streak.
#
# Example:
# 9 -> 7 -> 5 has length 3
#
# Print the length.

streak = 1
longest = 1

for i in range(1, len(nums)):
    if nums[i] < nums[i - 1]:
        streak += 1
    else:
        streak = 1
    if streak > longest:
        longest = streak

print(longest)

# Problem 5 (Index of second largest value)

nums = [12, 5, 18, 9, 21, 15]

# Task:
# Find the index of the second largest value.
#
# Example:
# Largest value = 21
# Second largest value = 18
#
# Print the index of the second largest value.

largest = float("-inf")
second_largest = float("-inf")
largest_index = 0
second_largest_index = 0

for i in range(len(nums)):
    if nums[i] > largest:
        largest = nums[i]
        largest_index = i
    if nums[i] > second_largest and nums[i] < largest:
        second_largest = nums[i]
        second_largest_index = i

print(second_largest_index)

# mistake log

# Problem 5 (Index of second largest value)

nums = [12, 5, 18, 9, 21, 15]

# Task:
# Find the index of the second largest value.
#
# Example:
# Largest value = 21
# Second largest value = 18
#
# Print the index of the second largest value.

largest = float("-inf")
second_largest = float("-inf")

largest_index = -1
second_largest_index = -1

for i in range(len(nums)):
    if nums[i] > largest:
        second_largest = largest
        second_largest_index = largest_index
        largest = nums[i]
        largest_index = i
    elif nums[i] > second_largest:
        second_largest = nums[i]
        second_largest_index = i
    

print(second_largest_index)

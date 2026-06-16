# Problem 1 (count increasing streak segments)

nums = [1, 2, 3, 1, 5, 2, 4, 6]

# An increasing streak segment is a maximal contiguous segment 
# where each next value is strictly greater than the previous value.
#
# Examples:
# [1, 2, 3]
# [1, 5]
# [2, 4, 6]
#
# Task:
# Print the total number of increasing streak segments.

streak = 1
count = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        streak += 1
    else:
        streak = 1
        count += 1

if streak > 1:
    count += 1

print(count)

# Problem 2 (length of each increasing streak)

nums = [3, 4, 5, 1, 2, 7, 8, 0]

# Task:
# Print the length of every increasing streak segment.
# Expected idea:
# 3
# 4 
# 1 
# because the streaks are:
# [3, 4, 5]
# [1, 2, 7, 8]
# [0]

streak = 1

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        streak += 1
    else:
        print(streak)
        streak = 1

print(streak)

# Problem 3 (largest drop between neighbors)

nums = [10, 7, 9, 2, 8, 1]

# Task:
# Find the largest decrease between two adjacenet elements.
# Example:
# 10 -> 7 (drop 3)
# 9 -> 2 (drop 7)
# 8 -> 1 (drop 7)
# Print the largest drop value.

drop = 0
largest = 0

for i in range(1, len(nums)):
    if nums[i] < nums[i - 1]:
        drop = nums[i - 1] - nums[i]
    if drop > largest:
        largest = drop

print(largest)

# Problem 4 (start value and end value of longest streak)

nums = [1, 2, 3, 1, 5, 6, 7, 8, 2]

# Task:
# Find the longest increasing streak.
# Print:
# start value
# end value
# For the example above:
# 1 
# 8
# because the longest streak is:
# [1, 5, 6, 7, 8]

streak = 1
longest = 1
start = 1
end = 1

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        streak += 1
        end = nums[i]
    else:
        streak = 1
    if streak > longest:
        longest = streak

print(start)
print(end)

# Problem 5 (sum of all streak maximums)

nums = [1, 2, 3, 1, 4, 5, 2, 8]

# The increasing streaks are:
# [1, 2, 3]
# [1, 4, 5]
# [2, 8]
# Their maximum values are:
# 3
# 5
# 8
# Task:
# Print the sum of the maximum value from every increasing streak.
# Expected output:
# 16

streak = 1
max = 1
sum = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        streak += 1
        max = nums[i]
    else:
        streak = 1
        sum += max

sum += max

print(sum)

# mistake log

# Problem 1 (count increasing streak segments)

nums = [1, 2, 3, 1, 5, 2, 4, 6]

# An increasing streak segment is a maximal contiguous segment 
# where each next value is strictly greater than the previous value.
#
# Examples:
# [1, 2, 3]
# [1, 5]
# [2, 4, 6]
#
# Task:
# Print the total number of increasing streak segments.

streak = 1
count = 1

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        streak += 1
    else:
        streak = 1
        count += 1

print(count)

# Problem 3 (largest drop between neighbors)]

nums = [10, 7, 9, 2, 8, 1]

# Task:
# Find the largest decrease between two adjacent elements.

# Example:
# 10 -> 7 (drop 3)
# 9 -> 2 (drop 7)
# 8 -> 1 (drop 7)

# Print the largest drop value.

largest = 0

for i in range(1, len(nums)):
    if nums[i] < nums[i - 1]:
        drop = nums[i - 1] - nums[i]
        
        if drop > largest:
            largest = drop

print(largest)

# Problem 4 (start value and end value of longest streak)

nums = [1, 2, 3, 1, 5, 6, 7, 8, 2]

# Task:
# Find the longest increasing streak.
# Print:
# start value
# end value

streak = 1
longest = 1
current_start = nums[0]
current_end = nums[0]

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        streak += 1
        current_end = nums[i]
    else:
        streak = 1
        current_start = nums[i]
        current_end = nums[i]
    if streak > longest:
        longest = streak
        longest_start = current_start
        longest_end = current_end

print(longest_start, longest_end)

# Problem 5 (sum of all streak maximums)

nums = [1, 2, 3, 1, 4, 5, 2, 8]

# The increasing streaks are:
# [1, 2, 3]
# [1, 4, 5]
# [2, 8]
# Ther maximum values are:
# 3 
# 5
# 8
# Task:
# Print the sum of the maximum value from every increasing streak.
# Expected output:
# 16

streak = 1
current_max = nums[0]
total = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        streak += 1
        current_max = nums[i]
    else:
        streak = 1
        total += current_max
        current_max = nums[i]

total += current_max

print(total)

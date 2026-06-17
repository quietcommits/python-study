# Problem 1 (Count local peaks)

nums = [3, 7, 5, 9, 8, 4, 6, 2]

# A local peak is an element that is greater than 
# both its immediate neighbors.

# Examples:
# 7 is a peak because 7 > 3 and 7 > 5
# 9 is a peak because 9 > 5 and 9 > 8

# Task:
# Count how many local peaks exist.
# Print the count.

count = 0

for i in range(1, len(nums) - 1):
    if nums[i - 1] < nums[i] > nums[i + 1]:
        count += 1

print(count)

# Problem 2 (longeste consecutive even streak)

nums = [2, 4, 6, 1, 8, 10, 12, 14, 3, 6]

# Task:
# Find the length of the longest consecutive
# streak of even numbers.

# Print the maximum length.

longest = 0
streak = 0

for n in nums:
    if n % 2 == 0:
        streak += 1
    else:
        streak = 0
    if streak > longest:
        longest = streak

print(longest)

# Problem 3 (largest increase between neighbors)

nums = [5, 2, 9, 3, 11, 7, 15]

# Task:
# Find the largest increase between two
# adjacent elements.

# Example:
# 2 -> 9 (increase 7)
# 3 -> 11 (increase 8)

# Print the largest increase value.

diff = 0
largest = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        diff = nums[i] - nums[i - 1]
    else:
        diff = 0
    if diff > largest:
        largest = diff

print(largest)

# Problem 4 (Print all valley values)

nums = [8, 3, 7, 2, 9, 1, 5]

# A valley is an element that is smaller than 
# both immediate neighbors.

# Task:
# Print all valley values, one per line.

for i in range(1, len(nums)):
    if nums[i - 1] > nums[i] < nums[i + 1]:
        print(nums[i])

# Problem 5 (Start and end of longest increasing streak)

nums = [1, 3, 5, 2, 4, 6, 8, 1, 2]

# An increasing streak means each next element
# is strictly greater than the previous one.

# Task:
# Find the longest increasing streak segment.
# Print its start index and end index

streak = 0
longest = 0
start = 0
end = 0
longest_start = 0
longest_end = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        streak += 1
        end = i
    else:
        streak = 1
        start = i
        end = i
    if streak > longest:
        longest = streak
        longest_start = start
        longest_end = end

print(longest_start, longest_end)

# mistake log

# Problem 4 (Print all valley values)

nums = [8, 3, 7, 2, 9, 1, 5]

# A valley is an element that is smaller than 
# both immediate neighbors.

# Task:
# Print all valley values, one per line.

for i in range(1, len(nums) - 1):
    if nums[i - 1] > nums[i] < nums[i + 1]:
        print(nums[i])

# Problem 5 (Start and end of longest increasing streak)

nums = [1, 3, 5, 2, 4, 6, 8, 1, 2]

# An increasing streak means each next element
# is strictly greater than the previous one.

# Task:
# Find the longest increasing streak segment.
# Print its start index and end index

streak = 1
longest = 1
start = 0
end = 0
longest_start = 0
longest_end = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        streak += 1
        end = i
    else:
        streak = 1
        start = i
        end = i
    if streak > longest:
        longest = streak
        longest_start = start
        longest_end = end

print(longest_start, longest_end)

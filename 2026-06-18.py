# Problem 1 (Count local peaks)

nums = [1, 5, 3, 7, 2, 8, 4]

# A local peak is an element that is greater
# than both its immediate neighbors.
# Example:
# In [1, 5, 3], 5 is a local peak.
# Task:
# Count how many local peaks exist.
# Print the count.

count = 0

for i in range(1, len(nums) - 1):
    if nums[i - 1] < nums[i] > nums[i + 1]:
        count += 1

print(count)

# Problem 2 (longest equal-value streak)

nums = [1, 1, 2, 2, 2, 3, 3, 1]

# Task:
# Find the length of longest streak
# of consecutive identical values.
# Print the length.

streak = 1
longest = 1

for i in range(1, len(nums)):
    if nums[i] == nums[i - 1]:
        streak += 1
    else:
        streak = 1
    if streak > longest:
        longest = streak

print(longest)

# Problem 3 (First repeated value)

nums = [4, 7, 2, 9, 7, 5, 2]

# Task:
# Find the first value that appears more than once while scanning from left to right.
# Print the value.

first = []

for n in nums:
    first.append(n)
    if n in first:
        print(n)
        break

# Problem 4 (Index of largest jump)

nums = [3, 8, 2, 10, 5]

# A jump is the absolute difference between neighboring elements.
# Example: abs(8-3) = 5
# Task:
# Find the index where the largest jump starts.
# For example, if the largest jump is between nums[1] and nums[2], print 1.

jump = 0
largest = 0
start = nums[0]
largest_start = nums[0]

for i in range(1, len(nums)):
    jump = nums[i] - nums[i - 1]
    start = nums[i - 1]
    if jump > largest:
        largest = jump
        largest_start = start

print(largest_start)

# Problem 5 (Most frequent value)

nums = [3, 1, 2, 3, 2, 3, 1, 2, 3]

# Task:
# Find the value that appears most often.
# Print the value.
# You may assume there is only one answer.

count_value = nums[0]
count = 1
largest = 1
largest_value = nums[0]

for n in nums:
    count += 1
    count_value = n
    if count > largest:
        largest = count
        largest_value = count_value

print(largest_value)

# mistake log

# Problem 3 (First repeated value)

nums = [4, 7, 2, 9, 7, 5, 2]

# Task:
# Find the first value that appears more than once while scanning from left to right.
# Print the value.

seen = []

for n in nums:
    if n in seen:
        print(n)
        break

    seen.append(n)

# Problem 4 (Index of largest jump)

nums = [3, 8, 2, 10, 5]

# A jump is the absolute difference between neighboring elements.
# Example: abs(8-3) = 5
# Task:
# Find the index where the largest jump starts.
# For example, if the largest jump is between nums[1] and nums[2], print 1.

largest = 0
largest_index = 0

for i in range(1, len(nums)):
    jump = abs(nums[i] - nums[i - 1])
    
    if jump > largest:
        largest = jump
        largest_index = i - 1

print(largest_index)

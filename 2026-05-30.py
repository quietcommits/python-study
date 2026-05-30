# Problem 1 (track state changes)

nums = [3, 3, 5, 5, 5, 2, 2, 7]

# Count how many times the value changes
# compared to the previous element.

count = 0

for i in range(1, len(nums)):
    if nums[i] != nums[i - 1]:
        count += 1

print(count)

# Problem 2 (direction tracking)

nums = [1, 3, 5, 4, 2, 6, 8]

# Count how many times the direction changes.
#
# increasing - > decreasing
# decreasing -> increasing

count = 0
prev_direction = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        direction = 1
    elif nums[i] < nums[i - 1]:
        direction = -1
    else:
        direction = 0

    if prev_direction != 0 and direction != prev_direction:
        count += 1

    prev_direction = direction

print(count)

# Problem 3 (longest increasing streak length)

nums = [1, 2, 3, 1, 2, 3, 4, 1]

# Find the longest increasing streak length.
# 
# A streak continues when the current number
# is greater than the previous number.

count = 1
longest_streak = 1

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        count += 1
    else:
        count = 1

    if count > longest_streak:
        longest_streak = count

print(longest_streak)

# mistake log

# Problem 2 (direction tracking)

nums = [1, 3, 5, 4, 2, 6, 8]

# Count how many times the direction changes.
#
# increasing - > decreasing
# decreasing -> increasing

prev_direction = 0
count = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        direction = 1
    elif nums[i] < nums[i - 1]:
        direction = -1
    else:
        direction = 0

    if prev_direction != 0 and direction != prev_direction:
        count += 1

    prev_direction = direction

print(count)

# Problem 3 (longest increasing streak length)

nums = [1, 2, 3, 1, 2, 3, 4, 1]

# Find the longest increasing streak length.
# 
# A streak continues when the current number
# is greater than the previous number.

streak = 1
longest_streak = 1

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        streak += 1
    else:
        streak = 1

    if streak > longest_streak:
        longest_streak = streak

print(longest_streak)

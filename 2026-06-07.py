# Problem 1 (count direction changes)

nums = [2, 5, 8, 6, 3, 7, 9, 4]

# Directioin rules:
#
# current > previous -> UP
# current < previous -> DOWN
#
# Count how many times
# the direction changes.
#
# Examples:
# UP -> DOWN = 1
# DOWN -> UP = 1
# 
# Print the answer.

prev_direction = None
count = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        direction = "UP"
    else:
        direction = "DOWN"
    if prev_direction is not None and direction != prev_direction:
        count += 1
    prev_direction = direction

print(count)

# Problem 2 (longest UP streak)

nums = [1, 3, 5, 7, 4, 6, 8, 10, 2]

# An UP streak continues when:
# 
# current > previous
# 
# Find the length of the 
# longest UP streak.
# 
# Example:
# 1 -> 3 -> 5 -> 7
# length = 4
#
# Print the answer.

streak = 1
longest = 1

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        streak += 1
    else:
        streak = 1
    if streak > longest:
        longest = streak

print(longest)

# Problem 3 (count streak endings)

nums = [2, 4, 6, 1, 8, 10, 3, 12, 14]

# Count how many even_number
# streaks exist.
# 
# Examples:
# 
# [2, 4, 6] -> 1 streak
# [8, 10] -> 1 streak
# [12, 14] -> 1 streak
# 
# Print the answer.

count = 0

for i in range(1, len(nums)):
    if nums[i] % 2 == 1 and nums[i - 1] % 2 == 0:
        count += 1

if nums[i] % 2 == 0:
        count += 1

print(count)

# Problem 4 (peak detection)

nums = [1, 4, 2, 6, 3, 8, 5]

# Count how many times:
#
# previous < current > next
# 
# occurs.
# 
# Print the answer.

count = 0

for i in range(1, len(nums) - 1):
    if nums[i - 1] < nums[i] > nums[i + 1]:
        count += 1

print(count)

# Problem 5 (direction sequence)

nums = [1, 4, 7, 5, 2, 6, 8, 3]

# Direction rules:
# 
# current > previous -> UP
# current < previous -> DOWN
# 
# Count how many times 
# the sequence changes direction
#
# Example:
# 
# UP -> DOWN = 1
# DOWN -> UP = 1
# 
# Print the answer.

prev_direction = None
count = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        direction = "UP"
    else:
        direction = "DOWN"
    if prev_direction is not None and direction != prev_direction:
        count += 1
    prev_direction = direction

print(count)

# optimisation log

# Problem 3

if nums[i] % 2 ==0:
    count += 1

# to

if nums[-1] % 2 == 0:
    count += 1

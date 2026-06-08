# Problem 1 (count direction changes)

nums = [2, 5, 8, 6, 3, 7, 9, 4]

# Direction rules:
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

# Problem 2 (count peaks)

nums = [1, 4, 2, 6, 8, 3, 7, 5]

# A peak means:
# 
# previous < current > next
#
# Count how many peaks exist.
# 
# Print the answer.

peak = 0

for i in range(1, len(nums) - 1):
    if nums[i - 1] < nums[i] > nums[i + 1]:
        peak += 1

print(peak)

# Problem 3 (longeset UP streak)

nums = [1, 3, 5, 7, 2, 4, 6, 9, 10]

# An UP streak continues when:
# 
# current > previous
# 
# Find the length of the 
# longest UP streak.
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

# Problem 4 (count streak endings)

nums = [2, 4, 6, 1, 8, 10, 3, 12]

# Count how many even-number
# streaks exist.
# 
# Examples:
# 
# [2, 4, 6] -> 1 streak
# [8, 10] -> 1 streak
# [12] -> 1 streak
# 
# Print the answer.

count = 0

for i in range(1, len(nums)):
    if nums[i] % 2 == 1 and nums[i - 1] % 2 == 0:
        count += 1

if nums[-1] % 2 == 0:
    count += 1

print(count)

# Problem 5 (UP/DOWN transition tracking)

nums = [1, 3, 5, 4, 2, 6, 8, 7]

# Direction rules:
# 
# current > previous -> UP
# current < previous -> DOWN
#
# Count:
# 
# 1. UP -> DOWN transitions
# 2. DOWN -> UP transitions
# 
# Print both counts

prev_direction = None
up_to_down = 0
down_to_up = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        direction = "UP"
    else:
        direction = "DOWN"
    if prev_direction == "UP" and direction == "DOWN":
        up_to_down += 1
    if prev_direction == "DOWN" and direction == "UP":
        down_to_up += 1 
    prev_direction = direction

print(up_to_down, down_to_up)

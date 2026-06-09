# Problem 1 (count local valleys)

nums = [7, 3, 6, 2, 5, 1, 8]

# Count how many times:
#
# previous > current < next
# 
# In other words,
# the current number is smaller
# than both neighbors.
#
# Example:
# 7, 3, 6 -> count
#
# Print the answer.

count = 0

for i in range(1, len(nums) - 1):
    if nums[i - 1] > nums[i] < nums[i + 1]:
        count += 1

print(count)

# Problem 2 (longest dereasing streak)

nums = [9, 7, 5, 6, 4, 3, 2, 8]

# Find the length of the longest
# decreasing streak.
#
# A streak continues when:
# 
# current < previous
# 
# Print the answer.

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

# Problem 3 (count streak endings)

nums = [2, 4, 6, 1, 8, 10, 3, 12, 14]

# Count how many even-number streaks ends.
# 
# Examples:
# 
# [2, 4, 6] ends at 1
# [8, 10] ends at 3
# 
# Answer = 2
# 
# Print the answer.

count = 0

for i in range(1, len(nums)):
    if nums[i] % 2 == 1 and nums[i - 1] % 2 == 0:
        count += 1
    
print(count)

# Problem 4 (direction change tracking)

nums = [1, 5, 8, 4, 2, 6, 9, 7]

# Direction rules:
# 
# current > previous -> UP
# current < previous -> DOWN
# 
# Count separately:
# 
# 1. UP -> DOWN
# 2. DOWN -> UP
# 
# Print both answers.

prev_direction = None
up_to_down = 0
down_to_up = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        direction = "UP"
    else:
        direction = "DOWN"
    if prev_direction is not None and prev_direction == "UP" and direction == "DOWN":
        up_to_down += 1
    if prev_direction is not None and prev_direction == "DOWN" and direction == "UP":
        down_to_up += 1
    prev_direction = direction

print(up_to_down, down_to_up)

# Problem 5 (peak and valley count)

nums = [1, 5, 2, 7, 3, 8, 4]

# Count:
# 
# Peaks:
# previous < current > next
# 
# Valleys:
# previous > current < next
#
# Print both counts.

peak = 0
valley = 0

for i in range(1, len(nums) - 1):
    if nums[i - 1] < nums[i] > nums[i + 1]:
        peak += 1
    if nums[i - 1] > nums[i] < nums[i + 1]:
        valley += 1

print(peak, valley)

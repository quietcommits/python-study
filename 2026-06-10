# Problem 1 (count odd streak endings)

nums = [1, 3, 5, 2, 7, 9, 4, 11, 13, 15, 6]

# Count how many odd-number streaks end.
#
# Examples:
#
# [1, 3, 5] ends at 2
# [7, 9] ends at 4
# [11, 13, 15] ends at 6
#
# Answer = 3
#
# Print the answer.

count = 0

for i in range(1, len(nums)):
    if nums[i] % 2 == 0 and nums[i - 1] % 2 == 1:
        count += 1

print(count)

# Problem 2 (count local valleys)

nums = [7, 3, 5, 2, 6, 1, 8, 4]

# Count how many times:
#
# previous > current < next
# 
# In other words,
# the current number is smaller
# than both neighbors.
#
# Examples:
#
# 7, 3, 5 -> count
# 5, 2, 6 -> count
#
# Print the answer.

count = 0

for i in range(1, len(nums) - 1):
    if nums[i - 1] > nums[i] < nums[i + 1]:
        count += 1

print(count)

# Problem 3 (longest increasing streak)

nums = [1, 3, 5, 2, 4, 6, 8, 1, 2]

# Find the length of the longest streak
# where each number is larger
# than the previous one.
#
# Example:
# 
# 2, 4, 6, 8
#
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

# Problem 4 (count direction changes)

nums = [2, 5, 8, 6, 3, 7, 9, 4, 1]

# Direction rules:
# 
# current > previous -> UP
# current < previous -> DOWN
#
# Count how many times
# the direction changes.
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
    if prev_direction is not None and prev_direction != direction:
        count += 1
    prev_direction = direction

print(count)

# problem 5 (count streaks with length >= 3)

nums = [2, 4, 6, 1, 8, 10, 3, 12, 14, 16, 5]

# Count how many even-number streaks
# have length 3 or greater.
# 
# Examples:
# 
# [2, 4, 6] -> count
# [8, 10] -> do not count
# [12, 14, 16] -> count
#
# Answer = 2
# 
# Print the answer.

streak = 0
count = 0

for n in nums:
    if n % 2 == 0:
        streak += 1
    else:
        if streak >= 3:
            count += 1
        streak = 0

if streak >= 3:
    count += 1

print(count)

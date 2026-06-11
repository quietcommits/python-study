# Problem 1 (longest increasing streak)

nums = [1, 3, 5, 2, 4, 6, 8, 1, 2]

# Count the length of the 
# longest increasing streak.
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

# Problem 2 (count peak points)

nums = [1, 4, 2, 5, 7, 3, 6, 1]

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

# Problem 3 (longest even streak)

nums = [2, 4, 6, 1, 8, 10, 12, 3, 14]

# Find the length of the
# longest even-number streak.
#
# Example:
#
# 8, 10, 12
#
# length = 3
# 
# Print the answer.

streak = 0
longest = 0

for n in nums:
    if n % 2 == 0:
        streak += 1
    else:
        streak = 0
    if streak > longest:
        longest = streak

print(longest)

# Problem 4 (count trend reversals)

nums = [1, 3, 5, 4, 2, 6, 8, 7, 9]

# Direction rules:
# 
# current > previous -> UP
# current < previous -> DOWN
#
# Count how many times
# the direction changes.
#
# Print the answer.

prev_direction = None
count = 0

for i in range(1, len(nums)):
    if nums[i - 1] < nums[i]:
        direction = "UP"
    else:
        direction = "DOWN"
    if prev_direction is not None and prev_direction != direction:
        count += 1
    prev_direction = direction

print(count)

# Problem 5 (count valley points)

nums = [5, 2, 4, 1, 6, 3, 7, 2]

# A valley means:
# 
# previous > current < next
# 
# Count how many valleys exist.
# 
# Print the answer.

valley = 0

for i in range(1, len(nums) - 1):
    if nums[i - 1] > nums[i] < nums[i + 1]:
        valley += 1

print(valley)

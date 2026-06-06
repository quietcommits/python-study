# Problem 1 (count local minima)

nums = [5, 2, 4, 1, 7, 3, 8]

# Count how many times:
#
# previous > current < next
# 
# Example:
# 5, 2, 4 -> count
# Print the answer.

count = 0

for i in range(1, len(nums) - 1):
    if nums[i - 1] > nums[i] < nums[i + 1]:
        count += 1

print(count)

# Problem 2 (alternating parity tracking)

nums = [2, 5, 8, 3, 6, 7, 4]

# Count how many adjacent pairs
# alternate between even and odd.
#
# Examples:
# 2 -> 5 (count)
# 5 -> 8 (count)
# 
# Print the answer.

count = 0

for i in range(len(nums) - 1):
    if nums[i] % 2 == 0 and nums[i + 1] % 2 == 1:
        count += 1
    elif nums[i] % 2 == 1 and nums[i + 1] % 2 == 0:
        count += 1

print(count)

# Problem 3 (streak reset counting)

nums = [1, 2, 3, 1, 2, 5, 1, 4]

# An increasing streak continues when:
#
# current > previous
# 
# Count how many times
# an increasing streak ends.
#
# Example:
# 1, 2, 3, 1
# streak ends at 3
# Print the answer.

streak = 1
reset = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        streak += 1
    else:
        streak = 1
        reset += 1

print(reset)

# Problem 4 (peak and valley difference)

nums = [5, 2, 8, 1, 9, 3]

# Find:
#
# largest number - smallest number
# 
# Print the answer.
# 
# Do not use max() or min().

largest = float("-inf")
smallest = float("inf")

for n in nums:
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n

print(largest - smallest)

# Problem 5 (direction sequence)

nums = [1, 4, 7, 5, 2, 6, 8, 3]

# Direction rules:
#
# current > previous -> UP
# current < previous -> DOWN
#
# Count how many times
# the sequence changes direction.
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

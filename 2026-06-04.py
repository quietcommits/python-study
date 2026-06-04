# Problem 1 (count increasing streaks)

nums = [1, 2, 3, 1, 5, 6, 2, 4]

# Count how many increasing streaks exist.
#
# Examples:
# [1, 2, 3] -> 1 streak
# [1, 5, 6] -> 1 streak
# [2, 4] -> 1 streak
# 
# print the answer.

count = 1

for i in range(1, len(nums)):
    if nums[i] <= nums[i - 1]:
        count += 1

print(count)

# Problem 2 (longest decreasing streak)

nums = [9, 7, 5, 8, 6, 4, 2, 10]

# Find the length of the longest
# decreasing streak.
# A streak continues when
# current < previous.
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

# Problem 3 (count direction changes)

nums = [1, 3, 5, 4, 2, 6, 8, 7]

# Direction rules:
# current > previous -> "UP"
# current < previous -> "DOWN"
# 
# Count how many times
# the direction changes.
# 
# Examples:
# UP -> DOWN = 1 change
# DOWN -> UP = 1 change
# 
# Print the answer.

direction = 0
prev_direction = 0
change = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        direction = "UP"
    if nums[i] < nums[i - 1]:
        direction = "DOWN"
    if prev_direction != 0 and direction != prev_direction:
        change += 1
    prev_direction = direction

print(change)

# Problem 3 (count direction changes)

nums = [1, 3, 5, 4, 2, 6, 8, 7]

# Direction rules:
# current > previous -> "UP"
# current < previous -> "DOWN"
# 
# Count how many times
# the direction changes.
# 
# Examples:
# UP -> DOWN = 1 change
# DOWN -> UP = 1 change
# 
# Print the answer.

prev_direction = None
change = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        direction = "UP"
    else:
        direction = "DOWN"
    if prev_direction is not None and direction != prev_direction:
        change += 1
    prev_direction = direction

print(change)

# Problem 4 (longest increasing streak)

nums = [1, 2, 3, 1, 2, 3, 4, 2]

# A streak continues when 
# current > previous.
# 
# Find the length of the 
# longest increasing streak.
#
# Example idea:
# 1 -> 2 -> 3 = 3-length streak
# 1 -> 2 -> 3 -> 4 = 4-length streak
# 
# Print the longest streak length

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

# Problem 5 (multiple conditions counting)

nums = [4, 11, 18, 7, 20, 15, 2]

# Count how many numbers are:
#
# 1. even
# 2. greater than 10
# 3. both even AND greater than 10
#
# Print all three counts.

even = 0
greater = 0
both = 0

for n in nums:
    if n % 2 == 0:
        even += 1
    if n > 10:
        greater += 1
    if n % 2 == 0 and n > 10:
        both += 1

print("even:", even, "\ngreater than 10:", greater, "\nboth even and greater than 10:", both)

# Problem 6 (count streak endings)

nums = [2, 4, 6, 1, 8, 10, 3, 12]

# Count how many even_number
# streaks exist.
# 
# A streak is a continuous block of even numbers.
# 
# Examples:
# [2, 4, 6] -> 1 streak
# [8, 10] -> 1 streak
# [12] -> 1 strek
# 
# Print the answer.

count = 0

for i in range(len(nums)):
    if nums[i] % 2 == 0:
        if i == 0 or nums[i - 1] % 2 == 1:
            count += 1

print(count)

# Problem 7 (UP/DOWN transition tracking)

nums = [1, 3, 5, 4, 2, 6, 8, 7]

# Direction rules:
# current > previous -> "UP"
# current < previous -> "DOWN"
#
# Count:
# 1. UP -> DOWN transitions
# 2. DOWN -> UP transitions
# 
# Print both counts.

prev_direction = None
up_to_down_transition = 0
down_to_up_transition = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        direction = "UP"
    else:
        direction = "DOWN"

    if prev_direction is not None:
        if prev_direction == "UP" and  direction == "DOWN":
            up_to_down_transition += 1
        elif prev_direction == "DOWN" and direction == "UP":
            down_to_up_transition += 1
    
    prev_direction = direction

print(up_to_down_transition, down_to_up_transition)

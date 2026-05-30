# Problem 1 (compare with previous value)

nums = [5, 8, 8, 3, 10, 7]

# Starting from the SECOND element:
#
# If current > previous:
#     print("UP")
#
# If current < previous:
#     print("DOWN")
#
# Otherwise:
#     print("SAME")

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        print("UP")
    elif nums[i] < nums[i - 1]:
        print("DOWN")
    else:
        print("SAME")

# Problem 2 (count positive changes)

nums = [5, 8, 8, 3, 10, 7]

# Count how many times:
#
# current > previous
# 
# Print the final count.

count = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        count += 1

print(count)

# Problem 3 (track previous direction)

nums = [1, 3, 5, 4, 2, 6, 8]

# Direction rules:
# current > previous -> "UP"
# current < previous -> "DOWN"
#
# Count how many times 
# the direction changes.
#
# Print the final count.

count = 0
prev_direction = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        direction = 1
    elif nums[i] < nums[i - 1]:
        direction = -1
    else:
        direction = 0
    
    if prev_direction != 0 and prev_direction != direction:
        count += 1

    prev_direction = direction

print(count)

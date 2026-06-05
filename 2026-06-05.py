# Problem 1 (state tracking - odd/even transitions)

nums = [2, 4, 7, 9, 12, 14, 3, 8]

# Count how many times the sequence changes:
# 
# EVEN -> ODD
# ODD -> EVEN
#
# Examples:
# 4 -> 7 = EVEN -> ODD
# 9 -> 12 = ODD -> EVEN
# 
# Print both counts.

change_to_odd = 0
change_to_even = 0

for i in range(1, len(nums)):
    if nums[i] % 2 == 1 and nums[i - 1] % 2 == 0:
        change_to_odd += 1
    if nums[i] % 2 == 0 and nums[i - 1] % 2 == 1:
        change_to_even += 1

print(change_to_odd, change_to_even)

# Problem 2 (three-value pattern detection)

nums = [1, 3, 2, 5, 7, 4, 6, 8, 3]

# Count how many times this pattern appears:
# 
# previous < current > next
# 
# In other words,
# the current number is bigger
# than both neighbors.
#
# Example:
# 1, 3, 2 -> count
#
# Print the answer.

count = 0

for i in range(1, len(nums) - 1):
    if nums[i - 1] < nums[i] > nums[i + 1]:
        count += 1

print(count)

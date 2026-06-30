# Problem 5 (Largest local peak)

nums = [6, 14, 9, 18, 11, 20, 8]

# A local peak is larger than both neighbors.
#
# Task:
# Find the largest local peak.
#
# Print:
# 1. The value
# 2. Its index

largest = float("-inf")
index = 0

for i in range(1, len(nums) - 1):
    if nums[i-1] < nums[i] > nums[i+1]:
        if nums[i] > largest:
            largest = nums[i]
            index = i

print(largest, index)

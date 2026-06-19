# Problem 1 (Count local peaks)

nums = [3, 8, 5, 10, 7, 9, 2]

# A local peak is an element that is greater
# than both its immediate neighbors.

# Example:
# In [3, 8, 5], 8 is a local peak because
# 8 > 3 and 8 > 5.

# Task:
# Count how many local peaks exist in the list.
# Print the count.

count = 0

for i in range(1, len(nums) - 1):
    if nums[i - 1] < nums[i] > nums[i + 1]:
        count += 1

print(count)

# Problem 2 (Count local valleys)

nums = [8, 3, 7, 2, 9, 1, 5]

# A local valley is an element that is smaller
# than both its immediate neighbors.

# Example:
# In [8, 3, 7], 3 is a local valley because
# 3 < 8 and 3 < 7.

# Task:
# Count how many local valleys exist in the list.
# Print the count.

count = 0

for i in range(1, len(nums) - 1):
    if nums[i - 1] > nums[i] < nums[i + 1]:
        count += 1

print(count)

# Problem 3 (Index of first local peak)

nums = [4, 9, 5, 8, 3, 7, 2]

# A local peak is an element that is greater
# than both immediate neighbors.

# Task:
# Find the index of the FIRST local peak.
# Print the index.
#
# If no local peak exists, print -1.

peak_index = -1

for i in range(1, len(nums) - 1):
    if nums[i-1] < nums[i] > nums[i+1]:
        peak_index = i
        break

print(peak_index)

nums = [5, 4, 3, 7, 2, 8]

# An increasing pair means:
# nums[i] < nums[i + 1]

# Task:
# Find the index where the FIRST increasing pair starts.
#
# Example:
# If nums[2] < nums[3],
# print 2.
#
# If no increasing pair exists,
# print -1.

increasing_index = -1

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        increasing_index = i - 1
        break

print(increasing_index)

# Problem 5 (First drop larger than 5)

nums = [12, 10, 8, 20, 13, 11, 4]

# A drop is:
# nums[i] - nums[i + 1]

# Task:
# Find the FIRST index i such that
# the drop from nums[i] to nums[i+1]
# is greater than 5.
#
# Print i.
#
# If no such drop exists,
# print -1.

drop_index = -1

for i in range(1, len(nums)):
    if nums[i - 1] - nums[i] > 5:
        drop_index = i - 1
        break

print(drop_index)

# Problem 6 (Index of largest drop)

nums = [15, 9, 12, 5, 3, 10]

# A drop is:
# nums[i] - nums[i + 1]

# Task:
# Find the index i where the largest drop starts.
#
# Example:
# 12 -> 5 has a drop of 7,
# so print 2.
#
# Print the index of the largest drop.

largest_drop = 0
largest_drop_index = 0

for i in range(1, len(nums)):
    if nums[i - 1] - nums[i] > largest_drop:
        largest_drop = nums[i - 1] - nums[i]
        largest_drop_index = i - 1

print(largest_drop_index)

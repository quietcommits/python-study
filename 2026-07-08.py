# Problem 1 (Largest even record high)

nums = [8, 13, 12, 17, 20, 19, 24]

# A record high is larger than every number before it.
#
# Task:
# Find the largest EVEN record high.
#
# Print the value.
#
# You may assume there is at least one even record high.

largest = nums[0]

if nums[0] % 2 == 0:
    largest_even = nums[0]
else:
    largest_even = float("-inf")

for i in range(1, len(nums)):
    if nums[i] > largest:
        largest = nums[i]
        if nums[i] % 2 == 0:
            largest_even = nums[i]

print(largest_even)

# Problem 2 (Cound odd record highs)

nums = [7, 12, 15, 14, 18, 21, 20]

# A record high is larger than every number before it.
#
# Task:
# Count how many ODD record highs exist.
#
# Print the count.

largest = nums[0]
count = 0

if nums[0] % 2 == 1:
    count += 1

for i in range(1, len(nums)):
    if nums[i] > largest:
        largest = nums[i]
        if nums[i] % 2 == 1:
            count += 1

print(count)

# Problem 3 (Sum of even record highs)

nums = [6, 11, 14, 13, 18, 17, 22]

# A record high is larger than every number before it.
#
# Task:
# Find the sum of all EVEN record highs.
#
# Print the total.

largest = nums[0]
total = 0

if nums[0] % 2 == 0:
    total += nums[0]

for i in range(1, len(nums)):
    if nums[i] > largest:
        largest = nums[i]
        if nums[i] % 2 == 0:
            total += nums[i]

print(total)

# Problem 4 (Smallest odd record high)

nums = [9, 14, 17, 16, 21, 20, 25]

# A record high is larger than every number before it.
#
# Task:
# Find the SMALLEST odd record high.
#
# Print the value.

largest = nums[0]

if nums[0] % 2 == 1:
    smallest_odd = nums[0]
else:
    smallest_odd = float("inf")

for i in range(1, len(nums)):
    if nums[i] > largest:
        largest = nums[i]
        if nums[i] % 2 == 1:
            if nums[i] < smallest_odd:
                smallest_odd = nums[i]

print(smallest_odd)

# Problem 5 (Count even record lows)

nums = [20, 18, 19, 16, 17, 12, 15, 10]

# A record low is smaller than every number before it.
#
# Task:
# Count how many EVEN record lows exist.
#
# Print the count.

smallest = nums[0]
count = 0

if nums[0] % 2 == 0:
    smallest_even = nums[0]
    count += 1
else:
    smallest_even = float("inf")

for i in range(1, len(nums)):
    if nums[i] < smallest:
        smallest = nums[i]
        if nums[i] % 2 == 0:
            smallest_even = nums[i]
            count += 1

print(count)

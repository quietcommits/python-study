# Problem 1 (early exit + condition check)

nums = [4, 1, 8, 2, 7, 3, 9]

# Find the FIRST number in the list that is greater than 6.
# Do NOT use max().
# As soon as you find it, print it and stop the loop immediately.

for n in nums:
    if n > 6:
        print(n)
        break

# Problem 2 (track maximum + index update)

nums = [3, 5, 2, 9, 1, 9, 4]

# Find the largest number in the list.
# Do NOT use max().
# When ever you update the largest vallue, print:
# "updated max:", value, "at index', index"
# At the end, print the final largest number.

largest = nums[0]
largest_index = 0

for i, n in enumerate(nums):
    if n > largest:
        largest = n
        largest_index = i
        print("updated max:", largest, "at index", largest_index)

print(largest)

# Problem 3 (track previous value + trend detection)

nums = [1, 3, 3, 2, 5, 4, 4, 6]

# For each number starting from the SECOND element:
# Compare it with the previous number.
# If current > previous -> print "UP"
# If current < previous -> print "DOWN"
# If current == previous -> print "FLAT"
# You MUST use a varaible called prev to store previous value.
# Do NOT use enumerate for this one.

prev = nums[0]

for i in range(1, len(nums)):
    if nums[i] > prev:
        print("UP")
    elif nums[i] < prev:
        print("DOWN")
    else:
        print("FLAT")

    prev = nums[i]

# optimisation log

# Problem 2 (track maximum + index update)

nums = [3, 5, 2, 9, 1, 9, 4]

# Find the largest number in the list.
# Do NOT use max().
# When ever you update the largest vallue, print:
# "updated max:", value, "at index", index"
# At the end, print the final largest number.


value = nums[0]
index = 0

for i, n in enumerate(nums):
    if n > value:
        value = n
        index = i
        print("updated max:", value, "at index", index)

print(value)

# Problem 3 (track previous value + trend detection)

nums = [1, 3, 3, 2, 5, 4, 4, 6]

# For each number starting from the SECOND element:
# Compare it with the previous number.
# If current > previous -> print "UP"
# If current < previous -> print "DOWN"
# If current == previous -> print "FLAT"
# You MUST use a varaible called prev to store previous value.
# Do NOT use enumerate for this one.

prev = nums[0]

for i in range(1, len(nums)):
    if nums[i] > prev:
        print("UP")
    elif nums[i] < prev:
        print("DOWN")
    else:
        print("FLAT")
    prev = nums[i]

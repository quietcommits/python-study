# Problem 1 (Smallest odd number)

nums = [14, 7, 20, 9, 11, 18, 5]

# Task:
# Find the smallest odd number.
#
# Print the value.
#
# You may assume there is at least one odd number.

smallest = float("inf")

for n in nums:
    if n % 2 == 1:
        if n < smallest:
            smallest = n

print(smallest)

# Problem 2 (Count numbers larger than the average)

nums = [8, 12, 15, 5, 10]

# The average is:
# (8 + 12 + 15 + 5 + 10) / 5 = 10
#
# Task:
# Count how many numbers are larger
# than the average.
#
# Print the count.

total = 0
count = 0

for n in nums:
    total += n

average = total / len(nums)

for n in nums:
    if n > average:
        count += 1

print(count)

# Problem 3 (Closest number to 20)

nums = [12, 27, 18, 23, 16, 21]

# Task:
# Find the number that is closest to 20.
#
# Print the value.
#
# You may assume there is only one correct answer.

smallest = float("inf")
closest = nums[0]

for n in nums:
    if abs(20-n) < smallest:
        smallest = abs(20-n)
        closest = n

print(closest)

# Problem 4 (Farthest number from zero)

nums = [-8, 3, -15, 10, 6, -2]

# Task:
# Find the number that is farthest from zero.
#
# Print the value.
#
# Example:
# abs(-15) = 15
# abs(10) = 10
#
# So the answer is -15.

largest = float("-inf")
farthest = nums[0]

for n in nums:
    if abs(n) > largest:
        largest = abs(n-0)
        farthest = n

print(farthest)

# Problem 5 (Index of the largest number)

nums = [11, 27, 19, 35, 8, 22]

# Task:
# Find the index of the largest number.
#
# Print the index.

largest = float("-inf")
index = 0

for i in range(len(nums)):
    if nums[i] > largest:
        largest = nums[i]
        index = i

print(index)

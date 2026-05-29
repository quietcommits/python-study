# Problem 1 (find maximum value without max)

nums = [3, 7, 2, 9, 5, 1]

# Find the largest number in the list.
# Do NOT use max().
# Print the result.

largest = float("-inf")

for n in nums:
    if n > largest:
        largest = n

print(largest)

# Problem 2 (even number count)

nums = [4, 7, 2, 9, 12, 5, 8]

# Count how many even numbers are in the list.
# Print the result.

count = 0

for n in nums:
    if n % 2 == 0:
        count += 1

print(count)

# Problem 3 (sum of elements)

nums = [5, 3, 8, 2, 7]

# Find the sum of all numbers in the list.
# Do NOT use sum().
# Print the result.

total = 0

for n in nums:
    total += n

print(total)

# Problem 4 (find minimum value without min)

nums = [8, 3, 11, 2, 7, 5]

# Find the smallest number in the list.
# Do NOT use min().
# Print the result.

smallest = float("inf")

for n in nums:
    if n < smallest:
        smallest = n

print(smallest)

# Problem 5 (find both largest and smallest)

nums = [1, 9, 2, 11, 7, 3]

# Find BOTH the largest and smallest numbers.
# Do NOT use max() or min().
# Print both results.

largest = float("-inf")
smallest = float("inf")

for n in nums:
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n

print(largest, smallest)

# Problem 6 (find first even number)

nums = [7, 5, 9, 4, 2, 8]

# Find the FIRST even number in the list.
# Print the result.

for n in nums:
    if n % 2 == 0:
        print(n)
        break

# Problem 7 (find index of largest number)

nums = [4, 12, 7, 3, 15, 9]

# Find the INDEX of the largest number.
# Do NOT use max() or index().
# Print the index.

largest = nums[0]
largest_index = 0

for i in range(1, len(nums)):
    if nums[i] > largest:
        largest = nums[i]
        largest_index = i

print(largest_index)

# Problem 8 (first number greater than 10 and its index)

nums = [3, 6, 8, 2, 15, 7, 11]

# Find the FIRST number greater than 10.
# Print its value AND its index

for i in range(len(nums)):
    if nums[i] > 10:
        print(nums[i], i)
        break

# Problem 9 (count + condition mix)

nums = [5, 12, 7, 18, 3, 10, 21]

# Count how many numbers are greater than 10.
# Print the result.

count = 0

for n in nums:
    if n > 10:
        count += 1

print(count)

# Problem 10 (sum of numbers greater than 10)

nums = [3, 12, 7, 18, 3, 10, 21]

# Find the SUM of numbers greater than 10.
# Priint the result.

result = 0

for n in nums:
    if n > 10:
        result += n

print(result)

# Problem 11 (replace values conditionally)

nums = [3, 12, 7, 18, 3, 10, 21]

# Replace all numbers greater than 10 with 0.
# Print the modified list.

new = []

for n in nums:
    if n > 10:
        new.append(0)
    else:
        new.append(n)

print(new)

# Problem 12 (in-place update with index)

nums = [3, 12, 7, 18, 3, 10, 21]

# Replace all numbers greater than 10 with 0.
# BUT modify the original list directly (no new list).
# Print nums.

for i in range(len(nums)):
    if nums[i] > 10:
        nums[i] = 0

print(nums)

# Problem 13 (second largest number without sorting)

nums = [5, 1, 9, 3, 9, 7, 2]

# Find the SECOND largest number in the list.
# Do NOT use sort(), max(), or any built-in helpers.
# Print the result.

largest = float("-inf")
second_largest = float("-inf")

for n in nums:
    if n > largest:
        second_largest = largest
        largest = n
    elif n > second_largest:
        second_largest = n

print(second_largest)

# Problem 14 (count numbers above average)

nums = [4, 8, 2, 10, 6]

# Step 1: Find the average of the list
# Step 2: Count how many numbers are above the average
# Do NOT use sum() for final solution (you can compute manually)

total = 0
count = 0

for n in nums:
    total += n 

average = total / len(nums)

for n in nums:
    if n > average:
        count += 1

print(count)

# Problem 15 (running count with condition change)

nums = [3, 5, 2, 8, 6, 4, 9]

# Count how many times a number is greater than the previous number
# (compare current element with previous element)

count = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        count += 1

print(count)

## Problem 16 (track increasing streak length)

nums = [1, 2, 3, 1, 2, 3, 4, 1]

# Find the longest increasing streak length
# (consecutive increasing sequence)

current = 1
best = 1

for i in range(1, len(nums)):
    if nums[i] > nums [i - 1]:
        current += 1
    else:
        current = 1

    if current > best:
        best = current 

print(best)

## Problem 17 (count up-down transitions)

nums = [1, 3, 2, 4, 3, 5]

# Count how many times the sequence changes direction
# (increasing → decreasing OR decreasing → increasing)

prev_direction = 0
count = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        direction = 1
    elif nums[i] < nums[i - 1]:
        direction = -1
    else:
        continue

    if prev_direction != 0 and direction != prev_direction:
        count += 1

    prev_direction = direction

print(count)

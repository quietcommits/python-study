# Problem 1 (Second largest number)

nums = [8, 15, 3, 21, 14, 19]

# Task:
# Find the second largest number.
#
# Print the value.
#
# You may assume all numbers are different.

largest = float("-inf")
second_largest = float("-inf")

for n in nums:
    if n > largest:
        second_largest = largest
        largest = n
    elif n > second_largest:
        second_largest = n

print(second_largest)

# Problem 2 (Second smallest number)

nums = [12, 5, 18, 2, 9, 7]

# Task:
# Find the second smallest number.
#
# Print the value.
#
# You may assume all numbers are different.

smallest = float("inf")
second_smallest = float("inf")

for n in nums:
    if n < smallest:
        second_smallest = smallest
        smallest = n
    elif n < second_smallest:
        second_smallest = n

print(second_smallest)

# Problem 3 (Difference between largest and smallest)

nums = [14, 6, 22, 9, 17, 3]

# Task:
# Find the difference between the largest
# and the smallest number.
#
# Print the difference.

largest = float("-inf")
smallest = float("inf")

for n in nums:
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n

print(largest - smallest)

# Problem 4 (Largest even number)

nums = [11, 24, 7, 18, 31, 42, 9]

# Task:
# Find the largest even number.
#
# Print the value.
#
# You may assume there is at least one even number.

largest = float("-inf")

for n in nums:
    if n % 2 == 0:
        if n > largest:
            largest = n

print(largest)

# Problem 5 (Count numbers between two values)

nums = [5, 12, 8, 21, 17, 9, 14, 3]

# Task:
# Count how many numbers are
# between 10 and 20 inclusive.
#
# (10 and 20 are included.)
#
# Print the count.

count = 0

for n in nums:
    if 10 <= n <= 20:
        count += 1

print(count)

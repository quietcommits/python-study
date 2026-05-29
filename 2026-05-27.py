# Problem 1 (running maximum + first match)

nums = [3, 5, 2, 8, 6, 9, 1]

# Find the FIRST number that is greater than all previous numbers.
# (Do not count the first number.)
# Print the result.

max_so_far = nums[0]

for n in nums[1:]:
    if n > max_so_far:
        print(n)
        break

# Problem 2 (count + condition tracking)

nums = [4, 1, 7, 3, 7, 8, 2, 8]

# Count how many numbers are greater than all previous numbers.
# Print the count.

count = 1

max_so_far = nums[0]

for n in nums[1:]:
    if n > max_so_far:
        max_so_far = n
        count += 1

print(count)

# Problem 3 (two-pass thinking without extra list)

nums = [5, 1, 8, 3, 8, 2, 7]

# Find the largest number.
# Then count how many times it appears
# Print the count

largest = float("-inf")

for n in nums:
    if n > largest:
        largest = n

count = 0

for n in nums:
    if n == largest:
        count += 1

print(count)

# Problem 4 (index tracking)

nums = [4, 2, 9, 1, 7]

# Find the index of the largest number.
# Print the index.
# Do not use max() or index().

largest = nums[0]
largest_index = 0

for i in range(1, len(nums)):
    if nums[i] > largest:
        largest = nums[i]
        largest_index = i

print(largest_index)


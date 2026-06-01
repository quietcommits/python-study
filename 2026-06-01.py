# Problem 1 (counting with multiple conidtions)

nums = [3, 8, 5, 12, 7, 20, 9]

# Count:
# 1. How many numbers are even?
# 2. How many numbers are greater than 10?
# 
# Print both counts.

even = 0

greater_than_10 = 0

for n in nums:
    if n % 2 == 0:
        even += 1
    if n > 10:
        greater_than_10 += 1

print("even:", even, "\ngreater_than_10:", greater_than_10)

# Problem 2 (conditions overlapping)

nums = [4, 7, 12, 15, 20, 3, 18]

# Count how many numbers are:
#
# 1. even
# 2. greater than 10
# 3. both even AND greater than 10
# 
# Print all three counts.

even = 0
greater_than_10 = 0
even_and_greater_than_10 = 0

for n in nums:
    if n % 2 == 0:
        even += 1
    if n > 10:
        greater_than_10 += 1
    if n % 2 == 0 and n > 10:
        even_and_greater_than_10 += 1

print("even:", even, "\ngreater_than_10:", greater_than_10, "\nboth:", even_and_greater_than_10)


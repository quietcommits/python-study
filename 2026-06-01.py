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

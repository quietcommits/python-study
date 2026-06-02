# Problem 1 (longest even streak)

nums = [2, 4, 6, 1, 8, 10, 12, 3]

# Find the length of the longest
# consecutive even-number streak.
#
# Print the answer.

even = 0
longest = 0

for n in nums:
    if n % 2 == 0:
        even += 1
    if n % 2 == 1:
        even = 0
    if even > longest:
        longest = even

print(longest)

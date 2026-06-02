# Problem 1 (count streak endings)

nums = [2, 4, 6, 1, 8, 10, 3, 12]

# Count how many even-number streaks exist.
#
# Examples:
# [2, 4, 6] -> 1 streak
# [8, 10] -> 1 streak
# [12] -> 1 streak
#
# Print the answer.

streak = 0
count = 0

for n in nums:
    if n % 2 == 0:
        streak += 1
    if n % 2 == 1 and streak > 0:
        streak = 0
        count += 1

if streak > 0:
    count += 1 

print(count)

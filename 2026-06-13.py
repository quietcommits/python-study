# Problem 1 (count increasing streak endings)

nums = [1, 2, 3, 1, 4, 5, 2, 7, 8, 9, 1]

# Count how many increasing streaks end.
#
# Examples:
#
# [1, 2, 3] ends at 1
# [4, 5] ends at 2
# [7, 8, 9] ends at 1
# 
# Answer = 3
#
# Print the answer

streak = 1
count = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        streak += 1
    else:
        if streak > 1:
            count += 1
        streak = 1

print(count)

# Problem 2 (longest odd streak)

nums = [1, 3, 5, 2, 7, 9, 11, 4, 13, 15]

# Find the length of the 
# longest odd-number streak.
#
# Example:
#
# [7, 9, 11]
# 
# length = 3
#
# Print the answer.

streak = 0
longest = 0

for n in nums:
    if n % 2 == 1:
        streak += 1
    else:
        streak = 0
    if streak > longest:
        longest = streak

print(longest)

# Problem 3 (count streaks length >= 2)

nums = [2, 4, 1, 6, 8, 3, 10, 12, 14]

# Count how many even-number streaks
# have length 2 or greater.
#
# Examples:
# 
# [2, 4]
# [6, 8]
# [10, 12, 14]
#
# Answer = 3
#
# Print the answer.

streak = 0
count = 0

for n in nums:
    if n % 2 == 0:
        streak += 1
    else:
        if streak >= 2:
            count += 1
        streak = 0

if streak >= 2:
    count += 1

print(count)

# Problem 4 (largest streak sum)

nums = [2, 4, 6, 1, 8, 10, 3, 5, 7, 9]

# Find the largest sum among
# all odd-number streaks.
#
# Example:
# 
# [3, 5, 7, 9]
# 
# sum = 24
#
# Print the answer.

current_sum = 0
largest = 0

for n in nums:
    if n % 2 == 1:
        current_sum += n
    else:
        current_sum = 0
    if current_sum > largest:
        largest = current_sum

print(largest)

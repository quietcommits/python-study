# Problem 1 (count increasing streaks)

nums = [1, 2, 3, 1, 4, 5, 2, 7, 8, 9, 1]

# Count how many increasing streaks exist.
#
# Examples:
#
# [1, 2, 3]
# [1, 4, 5]
# [2, 7, 8, 9]
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

if streak > 1:
    count += 1

print(count)

# Problem 2 (longest odd streak)

nums = [1, 3, 5, 2, 7, 9, 11, 4, 13]

# Find the length of the
# longest odd-number streak.
#
# Examples:
#
# [1, 3, 5] -> length 3
# [7, 9, 11] -> length 3
# [13] -> length 1
# 
# Answer = 3
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

# Problem 3 (sum of longest increasing streak)

nums = [1, 2, 3, 1, 4, 5, 6, 2]

# Find the increasing streak
# with the greatest length.
# 
# That streak is:
# 
# [1, 4, 5, 6]
# 
# Sum its values.
# 
# Answer = 16
# 
# Print the answer.

streak_len = 1
streak_sum = nums[0]

longest_len = 1
longest_sum = nums[0]

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        streak_len += 1
        streak_sum += nums[i]
    else:
        streak_len = 1
        streak_sum = nums[i]
    if streak_len > longest_len:
        longest_len = streak_len
        longest_sum = streak_sum

print(longest_sum)

# Problem 4 (count streaks length >= 2)

nums = [2, 4, 1, 6, 8, 3, 10, 12, 14]

# Count how many even-number streaks
# have length 2 or greater.
# 
# Examples:
# 
# [2, 4] -> count
# [6, 8] -> count
# [10, 12, 14] -> count
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

# Problem 5 (longest increasing streak ending value)

nums = [1, 2, 3, 1, 4, 5, 6, 2, 7]

# Find the longest increasing streak.
# 
# [1, 4, 5, 6]
# 
# Print the last value
# of that streak.
#
# Answer = 6

streak = 1
longest = 1
last = nums[1]

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        streak += 1
    else:
        streak = 1
    if streak > longest:
        longest = streak
        last = nums[i]

print(last)

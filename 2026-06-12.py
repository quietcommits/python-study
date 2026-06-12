# Problem 1 (count increasing streaks)

nums = [1, 3, 5, 2, 4, 6, 1, 7]

# Count how many increasing streaks exist.
#
# Examples:
#
# [1, 3, 5]
# [2, 4, 6]
# [1, 7]
#
# Answer = 3
# 
# Print the answer.

streak = 1
count = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        streak += 1
    else:
        if streak > 1:
            count += 1
        streak = 1

if nums[-1] > nums[-2]:
    count += 1

print(count)

# Problem 2 (longest odd streak)

nums = [1, 3, 5, 2, 7, 9, 11, 4, 13]

# Find the length of the 
# longest consecutive odd-number streak.
# 
# Examples:
#
# [1, 3, 5] -> length 3
# [7, 9, 11] -> length 3
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

# Problem 3 (count streaks length >= 3)

nums = [2, 4, 6, 1, 8, 10, 12, 3, 14]

# Count how many even-number streaks
# have length 3 or greater.
#
# Examples:
#
# [2, 4, 6] -> count
# [8, 10, 12] -> count
#
# Answer = 2
# 
# Print the answer.

streak = 0
count = 0

for n in nums:
    if n % 2 == 0:
        streak += 1
    else:
        if streak >= 3:
            count += 1
        streak = 0

if streak >= 3:
    count += 1

print(count)

# Problem 4 (largest streak sum)

nums = [1, 3, 5, 2, 4, 6, 8, 1]

# Find the largest sum among
# the increasing streaks.
#
# Examples:
# 
# [1, 3, 5] -> sum = 9
# [2, 4, 6, 8] -> sum = 20
# 
# Print the answer.

current_sum = nums[0]
largest = nums[0]

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        current_sum += nums[i]
    else:
        current_sum = nums[i]
    if current_sum > largest:
        largest = current_sum

print(largest)



# Problem 5 (streak ending count)

nums = [2, 4, 6, 1, 8, 10, 3, 12, 14, 16, 5]

# Count how many even-number streaks end.
#
# Examples:
#
# [2, 4, 6] ends at 1
# [8, 10] ends at 3
# [12, 14, 16 ends at 5]
#
# Answer = 3
# 
# Print the answer.

count = 0

for i in range(1, len(nums)):
    if nums[i] % 2 == 1 and nums[i - 1] % 2 == 0:
        count += 1

print(count)

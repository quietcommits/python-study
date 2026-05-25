# Problem 1 (loops + condition)

nums = [2, 5, 8, 3, 10, 7]

# Print only even numbers that are greater than 5.

for n in nums:
    if n % 2 == 0 and n > 5:
        print(n)

# Problem 2 (list building)

nums = [1, 2, 3, 4, 5]

# Create a new list that contains each number multiplied by 3.
# Print the result.

results = []

for n in nums:
    results.append(n * 3)

print(results)

# Problem 3 (strings + condition)

words = ["apple", "hi", "banana", "cat", "grape"]

# Print only words that have 5 or more characters.

for n in words:
    if len(n) >= 5:
        print(n)

# Problem 4 (nested condition)

nums = [2, 5, 8, 11, 14, 17, 20]

# Print numbers that are:
# - even
# - and greater than 10

for n in nums:
    if n % 2 == 0 and n > 10:
        print(n)

# Problem 5 (basic filtering)

nums = [4, 9, 12, 7, 18, 3, 20]

# Print only numbers that are divisible by 3.

for n in nums:
    if n % 3 == 0:
        print(n)

# Problem 6 (accumulation - product)

nums = [1, 2, 3, 4, 5, 6, 7]

# Calculate the product of all numbers in the list.
# Print the result.

results = 1

for n in nums:
    results = results * n

print(results)

# Problem 7 (string filtering)

words = ["apple", "banana", "hi", "grape", "cat"]

# Create a new list that contains only words that end with the letter "e".
# Print the result.

results = []

for w in words:
    if w.endswith("e"):
        results.append(w)

print(results)

# Problem 8 (multiple conditions in list filtering)

nums = [3, 6, 9, 12, 15, 18, 20, 22]

# Create a new list that contains only numbers that are:
# - divisible by 3
# - greater than 10

# Print the result. 

results = []

for n in nums:
    if n % 3 == 0 and n > 10:
        results.append(n)

print(results)

# Problem 9 (counting items in a list)

words = ["apple", "banana", "kiwi", "grape", "pear", "plum"]

# Count how many words have 5 or more characters.
# Print the result. 

count = 0

for w in words:
    if len(w) >= 5:
        count += 1

print(count)

# Problem 10 (sum + condition)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Calculate the sum of only the odd numbers.
# Print the result. 

total = 0 

for n in nums:
     if n % 2 == 1: 
         total += n

print(total)

# Problem 11 (find maximum value manually)

nums = [3, 7, 2, 9, 4, 12, 5]

# Find the largest number in the list WITHOUT using max() function.
# Print the result. 

largest = nums[0]

for n in nums: 
    if n > largest:
        largest = n

print(largest)

# Problem 12 (find longest word without built-in functions)

words = ["apple", "banana", "kiwi", "grape", "pear"]

# Find the longest word in the list WITHOUT using the max() or sorting.
# Print the result. 

longest = words[0]

for w in words:
    if len(w) > len(longest):
        longest = w

print(longest)

# Problem 13 (find second largest number without sorting or max)

nums = [1, 5, 2, 9, 3, 8, 4]

# Find the second largest number in the list WITHOUT using sorting or max().
# Print the result. 

largest = float('-inf')
second_largest = float('-inf')

for n in nums:
    if n > largest:
        second_largest = largest
        largest = n
    elif n > second_largest:
        second_largest = n

print(second_largest)

# Problem 14 (count words containing a specific character)

words = ["apple", "banana", "kiwi", "grape", "pear", "plum"]

# Count how many words contain the letter "a".
# Print the result.

count = 0

for w in words:
    if "a" in w:
        count += 1

print(count)

# Problem 15 (calculate average using sum and count)

nums = [2, 4, 6, 8, 10, 12, 14]

# Find the average (mena) of all numbers in the list.
# Print the result. 

total = 0
count = len(nums)

for n in nums:
    total += n

print(total / count)

# Problem 16 (filter and transform list values)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create a new list that contains:
# - only even numbers
# - and each of them multiplied by 2

# Print the result.

new = []

for n in nums:
    if n % 2 == 0:
        new.append(n * 2)

print(new)

# Problem 17 (count filtered values with multiple conditions)

nums = [2, 3, 4, 5, 6]

# Count how many numbers are:
# - even
# - and greater than 3 

# Print the result. 

count = 0

for n in nums:
    if n % 2 == 0 and n > 3:
        count += 1

print(count)

# Problem 18 (conditional transformation of list values)

nums = [1, 2, 3, 4, 5, 6, 7]

# Create a new list where:
# - odd numbers stay the same
# - even numbers are multiplied by 10

# Print the result.

results = []

for n in nums:
    if n % 2 == 1:
        results.append(n)
    elif n % 2 == 0:
        results.append(n * 10)

print(results)

# Problem 19 (difference between max and min values)

nums = [3, 1, 4, 1, 6, 9, 2]

# Find the difference between:
# - the maximum number
# - and the minimum number

# Print the result.

maximum_number = float("-inf")
minimum_number = float("inf")

for n in nums:
    if n > maximum_number:
        maximum_number = n
    if n < minimum_number:
        minimum_number = n

print(maximum_number - minimum_number)

# Problem 20 (sum with the multiple conditions and exclusion)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Calculate the sum of numbers that are:
# - divisible by 3 
# - but NOT divisible by 2 

# Print the result.

total = 0

for n in nums:
    if n % 3 == 0 and n % 2 != 0:
        total += n

print(total)

# Problem 21 (count using OR conditions)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Find how many numbers are: 
# - divislbe by 2
# - OR divisible by 3

# Print the result.

count = 0

for n in nums:
    if n % 2 == 0 or n % 3 == 0:
        count += 1

print(count)

# Problem 22 (conditional value mapping in a list)

nums = [2, 5, 1, 9, 6, 3, 7]

# Build a new list where:
# - numbers greater than 5 stay the same
# - numbers 5 or below become 0 

# Print the result.

result = []

for n in nums:
    if n > 5:
        result.append(n)
    else:
        result.append(0)

print(result)

# Problem 23 (square values then sum)

nums = [1, 2, 3, 4, 5, 6]

# Calculate the sum of squares of all numbers in the list.
# (Each number should be squared first, them summed)

# Print the result.

total = 0

for n in nums:
    total += n * n

print(total)

# Problem 24 (conditional mapping with multiple rules)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create a new list where:
# - numbers divisible by 3 become "FIZZ"
# - numbers divisible by 5 become "BUZZ"
# - otherwise keep the number as it is

# Print the result.

results = []

for n in nums: 
    if n % 3 == 0:
        results.append("FIZZ")
    elif n % 5 == 0:
        results.append("BUZZ")
    else:
        results.append(n)

print(results)

# Problem 25 (find index of maximum value)

nums = [3, 1, 4, 1, 5, 9, 2]

# Find the index of the maximum number in the list (Not the value, but the position).
# Print the result.

max_value = nums[0]
max_index = 0

for i in range(len(nums)): 
    if nums[i] > max_value:
        max_value = nums[i]
        max_index = i

print(max_index)

# mistake log

# Problem 25 (find index of maximum value)

nums = [3, 1, 4, 1, 5, 9, 2]

# Find the index of the maximum number in the list (Not the value, but the position).
# Print the result.

maximum_number = nums[0]
max_index = 0

for i in range(len(nums)):
    if nums[i] > maximum_number:
        maximum_number = nums[i]
        max_index = i

print(max_index)

# Problem 25 (find index of maximum value)

nums = [3, 1, 4, 1, 5, 9, 2]

# Find the index of the maximum number in the list (Not the value, but the position).
# Print the result.

largest_number = nums[0]
largest_index = 0

for i in range(len(nums)):
    if nums[i] > largest_number:
        largest_number = nums[i]
        largest_index = i

print(largest_index)

# Problem 13 (find second largest number without sorting or max)

nums = [1, 5, 2, 9, 3, 8, 4]

# Find the second largest number in the list WITHOUT using sorting or max().
# Print the result. 

largest = float("-inf")
second_largest = float("-inf")

for n in nums:
    if n > largest:
        second_largest = largest
        largest = n
    elif n > second_largest and n != largest:
        second_largest = n

print(second_largest)

# optimisation log

# Problem 23 (square values then sum)

nums = [1, 2, 3, 4, 5, 6]

# Calculate the sum of squares of all numbers in the list.
# (Each number should be squared first, them summed)

# Print the result.

total = 0

for n in nums:
    total += n * n

print(total)

"""
Session 1 

Problem 1: Longest Increasing Streak

Description:
Given a list of integers, return the length of the
longest consecutive increasing streak.

Example:
Input:
[1, 2, 3, 2, 4, 5, 6, 1]

Output:
4
"""

def longest_increasing_streak(numbers):
    streak = 1
    longest = 1
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i-1]:
            streak += 1
        else:
            streak = 1
        if streak > longest:
            longest = streak
    return longest

print(longest_increasing_streak([1, 2, 3, 2, 4, 5, 6, 1]))

"""
Session 1

Problem 2: Count Transactions Above Average

Description:
Given a list of transaction amounts, return the number
of transactions that are greater than the average amount.

Example:

Input:
[100, 200, 300, 400, 500]

Output:
2

Explanation:
Average = 300

Transactions above average:
400, 500
"""

def count_transactions_above_average(transactions):
    total = 0
    for i in range(len(transactions)):
        total += transactions[i]
    average = total / len(transactions)
    count = 0
    for i in range(len(transactions)):
        if transactions[i] > average:
            count += 1
    return count

print(count_transactions_above_average([100, 200, 300, 400, 500]))

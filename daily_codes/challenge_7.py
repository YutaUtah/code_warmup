"""
Problem:

Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

Examples:

Input: [1, 3, 5, 6], 5

Output: 2

Input: [1, 3, 5, 6], 2

Output: 1

Input: [1, 3, 5, 6], 0

Output: 0

** ** ** ** ** ** *

SOLUTION: https: // repl.it / @ morningalgo / SearchInsertPosition

** ** ** ** ** ** *

Asked
by: Amazon

Difficulty
level: Easy
"""


def search_insert(nums, target):
    left, right = 0, len(nums) - 1
    # left is 0 right is 3
    while left <= right:
        mid = (left + right) // 2
        mid is 1
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


print(search_insert([1,3,5,6], 5)) #2
print(search_insert([1,3,5,6], 2)) #1
print(search_insert([1,3,5,6], 0)) #0



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

target = 5
list = [1, 3, 5, 6]
count = 0



def searchInsert(nums, target):
    l , r = 0, len(nums)-1
    while l <= r:
        mid=(l+r)//2
        if nums[mid]== target:
            return mid
        if nums[mid] < target:
            l = mid+1
        else:
            r = mid-1
    return l

print(searchInsert([1,3,5,6], 5)) #2
print(searchInsert([1,3,5,6], 2)) #1
print(searchInsert([1,3,5,6], 0)) #0


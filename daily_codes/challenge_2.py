"""
8/12/2020
Problem:

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of
which the sum ≥ s. If there isn't one, return 0 instead.



Examples:

Input: s = 7, nums = [2,3,1,2,4,3]

Output: 2

Explanation: the subarray [4,3] has the minimal length under the problem constraint.



*************

SOLUTION: https://repl.it/@morningalgo/MinSubArraySum

*************
"""
#window
s = 7
nums = [2,3,1,2,4,3]
left_point = 0
right_point = 0
sum = 0
arr = []
while right_point < len(nums):
    sum += nums[right_point]
    while sum >= 7:
        arr.append(right_point-left_point+1)
        # subtract the number on the left and move the left pointer by 1 to the left sides
        sum -= nums[left_point]
        left_point += 1
    right_point += 1

print(arr)


# solutions
def minSubArrayLen(s, nums):
    total = left = right = 0
    res = len(nums) + 1
    while right < len(nums):
        total += nums[right]
        while total >= s:
            res = min(res, right-left+1)
            total -= nums[left]
            left += 1
        right += 1
    return res if res <= len(nums) else 0

print(minSubArrayLen(7, [2,3,1,2,4,3]))


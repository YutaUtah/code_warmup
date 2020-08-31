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
#todo go back
s = 7
nums = [2,3,1,2,4,3]

answer = []
for idx in range(len(nums)):
    for point in range(1, len(nums)-idx):
        sum = nums[idx] + nums[idx+point]
        if sum >= s:
            answer.append([nums[idx], nums[idx+point]])

print(answer)


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


"""
Problem:

Your are given an array of positive integers nums.
Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k



Examples:

Input: nums = [10, 5, 2, 6], k = 100

Output: 8

Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]

Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.



*************

SOLUTION: https://repl.it/@morningalgo/SubarrayProduct
https://leetcode.com/problems/subarray-product-less-than-k/solution/
https://www.youtube.com/watch?v=SxtxCSfSGlo
*************
"""

nums = [10, 5, 2, 6]
k = 100
left_point = 0
right_point  = 0
current = 1
answer = 0

while right_point < len(nums):
    current *= nums[right_point]
    while current >= k:
        current /= nums[left_point]
        left_point += 1
        pass

    answer += right_point - left_point + 1
    right_point += 1


print(answer)



## solutions
def numSubarrayProductLessThanK(nums, k):
    if k <= 1: return 0
    left = 0
    ans = 0
    cur = 1
    for right, val in enumerate(nums):
        cur *= val
        while cur >= k:
            cur /= nums[left]
            left += 1
        ans += right - left + 1
    return ans

print(numSubarrayProductLessThanK([10,5,2,6], 100))
"""
8/10/2020
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of
the non-zero elements.

Examples:

Input: [0,1,0,3,12]

Output: [1,3,12,0,0]
"""

arr = [0,1,0,3,12]

for i in range(len(arr)):
    if arr[i] == 0:
        del arr[i]
        arr.append(0)

print(arr)

"""
solution
"""

def moveZeroes(nums):
  zero = 0
  for i in range(len(nums)):
      if nums[i] != 0:
          nums[i], nums[zero] = nums[zero], nums[i]
          zero += 1

nums = [0,1,0,3,12]
moveZeroes(nums)
print(nums)
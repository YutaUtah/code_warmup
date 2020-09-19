"""
Problem:

Given a 2D array of 1’s and 0’s, where 1’s represent land and 0’s represent water.
Count the perimeter of island.

Examples:

Input:

[[0, 1, 0, 0],

 [1, 1, 0, 0]]

Output: 8

Explanation:

The perimeter of the top land is 3.
The perimeter of the bottom left land is 3.
The perimeter of the bottom right land is 2. The total perimeter is 3 + 3 + 2 = 8

** ** ** ** ** ** *

SOLUTION: https: // repl.it / @ morningalgo / IslandPermieter

** ** ** ** ** ** *

Asked by: Facebook

Difficulty level: Easy
"""

array = [[0, 1, 0, 0],
         [1, 1, 0, 0]]

count = 0
for arr in array:
    arr[count]


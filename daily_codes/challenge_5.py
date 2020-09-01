"""
Problem:

Balanced strings are those who have equal quantity of 'L' and 'R' characters.
Given a balanced string s split it in the maximum amount of balanced strings.
Return the maximum amount of splitted balanced strings.


Examples:

Input: s = "RLRRLLRLRL"

Output: 4

Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.


Input: s = "RLLLLRRRLR"

Output: 3

Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.


Input: s = "LLLLRRRR"

Output: 1

Explanation: s can be split into "LLLLRRRR".


Input: s = "RLRRRLLRLL"

Output: 2

Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'



*************
SOLUTION: https://repl.it/@morningalgo/BalancedString
*************

Asked by: Apple

Difficulty level: Easy
"""



s = "RLLLLRRRLR"


def balanced_string(s, R_count=0, count=0):
    for letter in s:
        if letter == 'R':
            R_count += 1
        elif letter == 'L':
            R_count -= 1
        if R_count == 0:
            count += 1
    return count

print(balanced_string(s))
"""
Problem:

We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example,
if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B
after some number of shifts on A.



Examples:

Example 1:

Input: A = 'abcde', B = 'cdeab'

Output: true



Example 2:

Input: A = 'abcde', B = 'abced'

Output: false

*************

SOLUTION: https://repl.it/@morningalgo/RotateString

*************


"""
A = 'abcde'
B = 'abced'


def rotateString(A, B):
    if len(A) != len(B):
        return False
    if len(A) == 0:
        return True

    for s in range(len(A)):
        for i in range(len(A)):
            if all(A[(s + i) % len(A)] == B[i]):
                return True
    return False

a =rotateString(A,B)
print(a)
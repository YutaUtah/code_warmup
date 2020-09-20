"""
Problem:

Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.


Examples:

Input: "leetcodeisacommunityforcoders"

Output: "ltcdscmmntyfrcdrs"


Input: "aeiou"

Output: ""

*************

SOLUTION: https://repl.it/@morningalgo/RemoveVowel

*************

Asked by: Amazon
Difficulty level: Easy
"""

def remove_vowel(String):
    vowel = set('aeiou')
    for char in String:
        if char in vowel:
            String = String.replace(char, "")

    return String



print(remove_vowel("leetcodeisacommunityforcoders"))
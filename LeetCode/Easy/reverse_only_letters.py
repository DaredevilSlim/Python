#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given a string s, reverse the string according to the following rules:
# All the characters that are not English letters remain in the same position.
# All the English letters (lowercase or uppercase) should be reversed.
# Return s after reversing it.
# Example 1:
# Input: s = 'ab-cd'
# Output: 'dc-ba'
# Example 2:
# Input: s = 'a-bC-dEf-ghIj'
# Output: 'j-Ih-gfE-dCba'
# Example 3:
# Input: s = 'Test1ng-Leet=code-Q!'
# Output: 'Qedo1ct-eeLg=ntse-T!'
# Constraints:
# 1 <= s.length <= 100
# s consists of characters with ASCII values in the range [33, 122].
# s does not contain '\'' or '\\'.
def reverse_only_letters(s: str) -> str:
    ss = [i for i in s if i.isalpha()][::-1]
    new_string = ''
    i = 0
    j = 0
    while i < len(s):
        if s[i].isalpha():
            new_string += ss[j]
            j += 1
        else:
            new_string += s[i]
        i += 1
    return new_string


print(reverse_only_letters('ab-cd'))  # 'dc-ba'
print(reverse_only_letters('a-bC-dEf-ghIj'))  # 'j-Ih-gfE-dCba'
print(reverse_only_letters('Test1ng-Leet=code-Q!'))  # 'Qedo1ct-eeLg=ntse-T!'

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
# Example 1:
# Input: s = "hello"
# Output: "holle"
# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"
# Constraints:
# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.
def reverse_vowels(s: str) -> str:
    vowels = ''.join(i for i in s if i.lower() in 'aeiou')[::-1]
    if len(vowels) <= 1:
        return s
    new_s = ''
    i = 0
    j = 0
    while i < len(vowels):
        if s[j].lower() in 'aeiou':
            new_s += vowels[i]
            i += 1
        else:
            new_s += s[j]
        j += 1
    else:
        new_s += s[j:]
    return new_s


print(reverse_vowels('hello'))  # 'holle'
print(reverse_vowels('leetcode'))  # 'leotcede'
print(reverse_vowels(' '))  # ' '
print(reverse_vowels('a.'))  # 'a.'
print(reverse_vowels('race car'))  # 'race car'
print(reverse_vowels('race a car'))  # 'raca e car'

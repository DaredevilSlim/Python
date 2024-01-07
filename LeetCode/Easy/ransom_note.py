#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given two strings ransom_note and magazine, return true if ransom_note can be constructed by using the letters from
# magazine and false otherwise.
# Each letter in magazine can only be used once in ransom_note.
# Example 1:
# Input: ransom_note = "a", magazine = "b"
# Output: false
# Example 2:
# Input: ransom_note = "aa", magazine = "ab"
# Output: false
# Example 3:
# Input: ransom_note = "aa", magazine = "aab"
# Output: true
# Constraints:
# 1 <= ransom_note.length, magazine.length <= 105
# ransom_note and magazine consist of lowercase English letters.
def can_construct(ransom_note: str, magazine: str) -> bool:
    dict_ransom = dict()
    dict_magazine = dict()
    for i in ransom_note:
        if i not in dict_ransom:
            dict_ransom[i] = 1
        else:
            dict_ransom[i] += 1
    for j in magazine:
        if j not in dict_magazine:
            dict_magazine[j] = 1
        else:
            dict_magazine[j] += 1
    for k in dict_ransom:
        if k in dict_magazine:
            if dict_ransom[k] > dict_magazine[k]:
                return False
        else:
            return False
    return True


print(can_construct('a', 'b'))  # False
print(can_construct('aa', 'ab'))  # False
print(can_construct('aa', 'aab'))  # True

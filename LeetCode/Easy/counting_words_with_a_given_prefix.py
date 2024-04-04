#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# You are given an array of strings words and a string pref.
# Return the number of strings in words that contain pref as a prefix.
# A prefix of a string s is any leading contiguous substring of s.
# Example 1:
# Input: words = ['pay', 'attention', 'practice', 'attend'], pref = 'at'
# Output: 2
# Explanation: The 2 strings that contain 'at' as a prefix are: 'attention' and 'attend'.
# Example 2:
# Input: words = ['leetcode', 'win', 'loops', 'success'], pref = 'code'
# Output: 0
# Explanation: There are no strings that contain 'code' as a prefix.
# Constraints:
# 1 <= words.length <= 100
# 1 <= words[i].length, pref.length <= 100
# words[i] and pref consist of lowercase English letters.
def prefix_count(words: list[str], pref: str) -> int:
    count = 0
    len_pref = len(pref)
    for i in sorted(words):
        if pref[0] == i[0]:
            if pref == i[:len_pref]:
                count += 1
    return count


print(prefix_count(['pay', 'attention', 'practice', 'attend'], 'at'))  # 2
print(prefix_count(['leetcode', 'win', 'loops', 'success'], 'code'))  # 0

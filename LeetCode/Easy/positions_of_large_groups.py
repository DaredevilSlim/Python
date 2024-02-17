#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# In a string s of lowercase letters, these letters form consecutive groups of the same character.
# For example, a string like s = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z", and "yy".
# A group is identified by an interval [start, end], where start and end denote the start and end indices (inclusive) of
# the group. In the above example, "xxxx" has the interval [3,6].
# A group is considered large if it has 3 or more characters.
# Return the intervals of every large group sorted in increasing order by start index.
# Example 1:
# Input: s = "abbxxxxzzy"
# Output: [[3,6]]
# Explanation: "xxxx" is the only large group with start index 3 and end index 6.
# Example 2:
# Input: s = "abc"
# Output: []
# Explanation: We have groups "a", "b", and "c", none of which are large groups.
# Example 3:
# Input: s = "abcdddeeeeaabbbcd"
# Output: [[3,5],[6,9],[12,14]]
# Explanation: The large groups are "ddd", "eeee", and "bbb".
# Constraints:
# 1 <= s.length <= 1000
# s contains lowercase English letters only.
def large_group_positions(s: str) -> list[list[int]]:
    i = 1
    s_list = list()
    t_list = [0, 0]
    while i < len(s):
        if s[i-1] == s[i]:
            t_list[1] = i
        else:
            t_list[1] = i-1
            if t_list[1] - t_list[0] >= 2:
                s_list.append(t_list)
            t_list = [i, i+1]
        i += 1
    return s_list


print(large_group_positions('abbxxxxzzy'))  # [[3, 6]]
print(large_group_positions('abc'))  # []
print(large_group_positions('abcdddeeeeaabbbcd'))  # [[3, 5], [6, 9], [12, 14]]
print(large_group_positions('aaa'))  # [0, 2]

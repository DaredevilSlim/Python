#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given a string s and a character c that occurs in s, return an array of integers answer where
# answer.length == s.length and answer[i] is the distance from index i to the closest occurrence of character c in s.
# The distance between two indices i and j is abs(i - j), where abs is the absolute value function.
# Example 1:
# Input: s = "loveleetcode", c = "e"
# Output: [3,2,1,0,1,0,0,1,2,2,1,0]
# Explanation: The character 'e' appears at indices 3, 5, 6, and 11 (0-indexed).
# The closest occurrence of 'e' for index 0 is at index 3, so the distance is abs(0 - 3) = 3.
# The closest occurrence of 'e' for index 1 is at index 3, so the distance is abs(1 - 3) = 2.
# For index 4, there is a tie between the 'e' at index 3 and the 'e' at index 5, but the distance is still the same:
# abs(4 - 3) == abs(4 - 5) = 1.
# The closest occurrence of 'e' for index 8 is at index 6, so the distance is abs(8 - 6) = 2.
# Example 2:
# Input: s = "aaab", c = "b"
# Output: [3,2,1,0]
# Constraints:
# 1 <= s.length <= 104
# s[i] and c are lowercase English letters.
# It is guaranteed that c occurs at least once in s.
def shortest_to_char(s: str, c: str) -> list[int]:
    result_list = list()
    temp_list = list()
    begin = 0
    for i in s:
        if i == c:
            result_list += temp_list[::-1] + [0]
            begin = 0
            temp_list = []
        else:
            temp_list += [begin + 1]
            begin += 1
    result_list += temp_list
    i = 1
    while i < len(result_list):
        if result_list[i - 1] < result_list[i]:
            result_list[i] = result_list[i-1] + 1
        i += 1
    return result_list


print(shortest_to_char('loveleetcode', 'e'))  # [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
print(shortest_to_char('aaab', 'b'))  # [3, 2, 1, 0]
print(shortest_to_char('baaaaaaaab', 'b'))  # [0, 1, 2, 3, 4, 4, 3, 2, 1, 0]
print(shortest_to_char('baaaaaaab', 'b'))  # [0, 1, 2, 3, 4, 3, 2, 1, 0]
print(shortest_to_char('aaba', 'b'))  # [2, 1, 0, 1]
print(shortest_to_char('aaaabbaaaa', 'b'))  # [4, 3, 2, 1, 0, 0, 1, 2, 3, 4]
print(shortest_to_char('aaaabaaa', 'b'))  # [4, 3, 2, 1, 0, 1, 2, 3]

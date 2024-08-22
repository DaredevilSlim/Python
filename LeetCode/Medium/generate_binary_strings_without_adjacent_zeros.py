#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# You are given a positive integer n.
# A binary string x is valid if all substrings of x of length 2 contain at least one '1'.
# Return all valid strings with length n, in any order.
# Example 1:
# Input: n = 3
# Output: ['010', '011', '101', '110', '111']
# Explanation:
# The valid strings of length 3 are: '010', '011', '101', '110', and '111'.
# Example 2:
# Input: n = 1
# Output: ['0', '1']
# Explanation:
# The valid strings of length 1 are: '0' and '1'.
# Constraints: 1 <= n <= 18
def valid_strings(n: int) -> list[str]:
    n_list = []
    i = 0
    while len(bin(i)) <= n + 2:
        elem = f'{i:0>{n}b}'
        if '00' not in elem:
            n_list.append(elem)
        i += 1
    return n_list



print(valid_strings(3))  # ['010', '011', '101', '110', '111']
print(valid_strings(1))  # ['0', '1']

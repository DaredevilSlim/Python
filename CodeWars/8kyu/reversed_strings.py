#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Complete the solution so that it reverses the string passed into it.
# 'world'  =>  'dlrow'
# 'word'   =>  'drow'
def solution(string: str) -> str:
    return string[::-1]


print(solution('world'))  # 'dlrow'
print(solution('word'))  # 'drow'

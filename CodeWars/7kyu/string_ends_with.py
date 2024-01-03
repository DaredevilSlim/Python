#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d
# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also
# a string).
# Examples:
# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false
def solution(string, ending):
    return ending in string[-len(ending):]


print(solution("samurai", "ai"))  # True
print(solution("ninja", "ja"))  # True
print(solution("sensei", "i"))  # True
print(solution("abc", "abc"))  # True
print(solution("abcabc", "bc"))  # True
print(solution("fails", "ails"))  # True
print(solution( "sumo", "omo"))  # False
print(solution("samurai", "ra"))  # False
print(solution("abc", "abcd"))  # False
print(solution("ails", "fails"))  # False
print(solution("this", "fails"))  # False
print(solution("spam", "eggs"))  # False

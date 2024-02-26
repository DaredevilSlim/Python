#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed,
# and the character will be typed 1 or more times.
# You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with
# some characters (possibly none) being long pressed.
# Example 1:
# Input: name = "alex", typed = "aaleex"
# Output: true
# Explanation: 'a' and 'e' in 'alex' were long pressed.
# Example 2:
# Input: name = "saeed", typed = "ssaaedd"
# Output: false
# Explanation: 'e' must have been pressed twice, but it was not in the typed output.
# Constraints:
# 1 <= name.length, typed.length <= 1000
# name and typed consist of only lowercase English letters.
def is_long_pressed_name(name: str, typed: str) -> bool:
    def split_string(string: str) -> list:
        ind = 1
        result = [[string[0]]]
        while ind < len(string):
            if result[-1][-1] == string[ind]:
                result[-1].append(string[ind])
            else:
                result.append([string[ind]])
            ind += 1
        return result

    if name == typed:
        return True
    if len(name) == len(typed):
        return False
    name = split_string(name)
    typed = split_string(typed)
    if len(name) != len(typed):
        return False
    for i, j in zip(name, typed):
        if i[0] != j[0] or len(i) > len(j):
            return False
    return True


print(is_long_pressed_name("alex", "aaleex"))  # True
print(is_long_pressed_name("laiden", "laiden"))  # True
print(is_long_pressed_name('saeed', 'ssaaedd'))  # False
print(is_long_pressed_name('rick', 'kric'))  # False
print(is_long_pressed_name('alex', 'aaleexa'))  # False

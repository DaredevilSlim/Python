#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# You need to count how many non-empty lines a given text has.
# An empty line is a line without symbols or the one that contains only spaces.
# Input: A text (str).
# Output: An integer (int).
def non_empty_lines(text: str) -> int:
    # return len(set(text.replace(' ', '').split('\n'))) - 1
    return len(list(filter(None, text.replace(' ', '').split('\n'))))


print(non_empty_lines("one simple line\n"))  # 1
print(non_empty_lines(""))  # 0
print(non_empty_lines("\nonly one line\n            "))  # 1
print(non_empty_lines(
    "\nLorem ipsum dolor sit amet,\n\nconsectetur adipiscing elit\nNam odio nisi, aliquam\n            "))  # 3

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# You are given a word in which letters can be in different cases. Your task is to check whether the case was used
# correctly in the line. If everything is correct - return True, if there are errors - return False.
# Examples of the correct use of cases:
# All characters in the string are in uppercase. For example, "CHECKIO";
# None of the characters are in uppercase. For example, "checkio";
# Only the first character is in uppercase. For example, "Checkio".
# Input: String (str).
# Output: Logic value (bool).
def correct_capital(line: str) -> bool:
    return line[0].isupper() and line[1:].islower() or line.isupper() or line.islower()


print(correct_capital("Checkio"))  # True
print(correct_capital("CheCkio"))  # False
print(correct_capital("CHECKIO"))  # True

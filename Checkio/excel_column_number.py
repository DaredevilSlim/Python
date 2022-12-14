#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given a string that represents the column title as appears in an Excel sheet, return its corresponding column number.
# But how does the Excel column numbering actually work? Well, the column number is like decimal number, but with base
# (radix) 26 and "digits" A-Z. Read more about number bases. Let's look at the exact numbers:
# Excel   Decimal
#     A   1
#    ..
#     Z   26
# The 1-"digit" numbers have ended. 2-"digits" numbers start from double first "digit" and go to double last one:
# Excel   Decimal
#     A   1
#    ..
#     Z   26
#    AA   27
#    ..
#    AZ   52
#    BA   53
#    ..
#    BZ   78
#    CA   79
#    ..
#    ..
#    ZZ   702
# Now it's turn for 3-"digit" numbers...
# Input: String.
# Output: Integer.
# Precondition: Non empty, only upper case, only English letters
def column_number(name: str) -> int:
    elements = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12,
                'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23,
                'X': 24, 'Y': 25, 'Z': 26}
    result = 0
    name = name[::-1]
    for i in range(len(name)):
        result += elements[name[i]] * 26 ** i
    return result


print(column_number("A"))        # 1
print(column_number("Z"))        # 26
print(column_number("AB"))       # 28
print(column_number("ZY"))       # 701
print(column_number("FXSHRXW"))  # 2147483647

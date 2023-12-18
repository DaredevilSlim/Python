#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# You need to determine whether the given integer (in base 10) is a palindrome or not in base B. Base (or radix) is
# written as subscript text. A number is a palindrome if it reads the same in both directions, for example 12110 is a
# palindrome, and 12210 is not. If the integerB is a palindrome, return True, if not, return False. Read more about
# number bases.
# The most common base is decimal. To convert an integer10 to another base you need to divide it by base and take
# reminders until the number becomes equal zero. Let's look at the following example - convert integer 610 into the
# binary form 62.
# Integer	Quotient	Reminder	Normal	Reversed
# 6	3	0	0	0
# 3	1	1	10	01
# 1	0	1	110	011
# 0
# Since reversed 011 is not equal normal 110 - 62 is not a palindrome.
# To return back to the decimal form, start from zero, multiply by base and add reminders. For 62)  # 110 it's
# (((0*2) + 1)*2 + 1)*2 + 0 = 6.
# Input: Given integer and base B (integer).
# Output: Bool.
# Preconditions:
# number >= 0;
# number is integer;
# B >= 2;
# B is integer.
def int_palindrome(number: int, B: int) -> bool:
    s = ''
    while number:
        s += str(number % B)[::-1] if (number // B) != 0 else str(number % B)
        number //= B
    return s == s[::-1]


print(int_palindrome(4545, 100))  # True
print(int_palindrome(3148, 16))  # True
print(int_palindrome(6, 2))  # False
print(int_palindrome(34, 2))  # False
print(int_palindrome(455, 2))  # True
print(int_palindrome(1441, 10))  # True
print(int_palindrome(1442, 10))  # False
print(int_palindrome(1413, 16))  # True
print(int_palindrome(2056, 16))  # True

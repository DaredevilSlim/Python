#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Check if the given year is leap year. A year is a leap year if it is divisible by 4, except for end-of-century years
# which must be divisible by 400. This means that the year 2000 was a leap year, although 1900 was not.
# Input: Integer (int).
# Output: Logic value (bool).
# How it’s used: this function can be used in calendars, scheduling applications, or any system which deals with yearly
# data.
# Precondition:
# 1 <= year <= 105
def is_leap_year(year: int) -> bool:
    return True if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else False


print(is_leap_year(2000))  # True
print(is_leap_year(1900))  # False
print(is_leap_year(2004))  # True
print(is_leap_year(2100))  # False
print(is_leap_year(2020))  # True
print(is_leap_year(2021))  # False
print(is_leap_year(1600))  # True
print(is_leap_year(1700))  # False
print(is_leap_year(1800))  # False
print(is_leap_year(2400))  # True

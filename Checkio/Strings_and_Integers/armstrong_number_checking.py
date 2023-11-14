#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# In number theory, an Armstrong number (after Michael F. Armstrong) or narcissistic number in a given number base (10
# for this mission) is a number that is the sum of its own digits each raised to the power of the number of digits. For
# example, 153 is an Armstrong number because 13 + 53 + 33)  # 153.
# Input: Integer (int).
# Output: Logic value (bool).
# How it’s used: this function can be employed in mathematical puzzles, encryption algorithms, and educational tools.
def is_armstrong(num: int) -> bool:
    return True if sum(int(i) ** len(str(num)) for i in str(num)) == num else False


print(is_armstrong(153))  # True
print(is_armstrong(370))  # True
print(is_armstrong(947))  # False
print(is_armstrong(371))  # True
print(is_armstrong(407))  # True
print(is_armstrong(163))  # False
print(is_armstrong(100))  # False
print(is_armstrong(8208))  # True
print(is_armstrong(930))  # False
print(is_armstrong(4))  # True

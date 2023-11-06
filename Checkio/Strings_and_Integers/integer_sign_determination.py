#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Identify whether a given integer is positive, negative, or zero and return a respective string: "positive", "negative"
# or "zero".
# Input: Integer (int).
# Output: String (str).
# How it’s used: understanding the sign of a number can be useful in financial software, scientific simulations, and
# many algorithms to determine subsequent logic.
# Precondition:
# num ∈ Z.
def determine_sign(num: int) -> str:
    return 'zero' if num == 0 else 'positive' if num > 0 else 'negative'


print(determine_sign(5))  # "positive"
print(determine_sign(0))  # "zero"
print(determine_sign(-10))  # "negative"
print(determine_sign(1))  # "positive"
print(determine_sign(-1))  # "negative"
print(determine_sign(999))  # "positive"
print(determine_sign(-1000))  # "negative"
print(determine_sign(123456789))  # "positive"
print(determine_sign(-987654321))  # "negative"
print(determine_sign(2))  # "positive"

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://www.codewars.com/kata/555a67db74814aa4ee0001b5
# In this Kata we are passing a number (n) into a function.
# Your code will determine if the number passed is even (or not).
# The function needs to return either a true or false.
# Numbers may be positive or negative, integers or floats.
# Floats with decimal part non equal to zero are considered UNeven for this kata.
def is_even(n: int or float) -> bool:
    return n % 2 == 0


print(is_even(0))  # True
print(is_even(0.5))  # False
print(is_even(1))  # False
print(is_even(2))  # True
print(is_even(-4))  # True
print(is_even(15))  # False
print(is_even(20))  # True
print(is_even(220))  # True
print(is_even(222222221))  # False
print(is_even(500000000))  # True

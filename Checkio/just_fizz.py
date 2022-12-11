#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This is a simplified version of Fizz Buzz mission.
# You should write a function that will receive a positive integer and return: "Fizz" if the number is divisible
# by 3 (3, 6, 9 ...) otherwise convert the given number to a string (2 -> "2").
# Input: An integer.
# Output: String.
def checkio(num: int) -> str:
    return "Fizz" if num % 3 == 0 else str(num)


print(checkio(15))  # "Fizz"
print(checkio(6))   # "Fizz"
print(checkio(10))  # "10"
print(checkio(7))   # "7"

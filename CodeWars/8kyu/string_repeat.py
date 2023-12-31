#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Write a function that accepts an integer n and a string s as parameters, and returns a string of s repeated exactly n
# times.
# Examples (input -> output)
# 6, "I"     -> "IIIIII"
# 5, "Hello" -> "HelloHelloHelloHelloHello"
def repeat_str(repeat, string):
    return repeat * string


print(repeat_str(4, 'a'), 'aaaa')  # aaaa aaaa
print(repeat_str(3, 'hello '), 'hello hello hello ')  # hello hello hello  hello hello hello
print(repeat_str(2, 'abc'), 'abcabc')  # abcabc abcabc

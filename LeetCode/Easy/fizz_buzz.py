#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given an integer n, return a string array answer (1-indexed) where:
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.
# Example 1:
# Input: n = 3
# Output: ["1","2","Fizz"]
# Example 2:
# Input: n = 5
# Output: ["1","2","Fizz","4","Buzz"]
# Example 3:
# Input: n = 15
# Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
def fizz_buzz(n: int) -> list[str]:
    list_n = list()
    for i in range(1, n + 1):
        if i % 3 == 0 == i % 5:
            s = 'FizzBuzz'
        elif i % 3 == 0:
            s = 'Fizz'
        elif i % 5 == 0:
            s = 'Buzz'
        else:
            s = f'{i}'
        list_n.append(s)
    return list_n


print(fizz_buzz(3))  # ['1', '2', 'Fizz']
print(fizz_buzz(5))  # ['1', '2', 'Fizz', '4', 'Buzz']
print(fizz_buzz(15))  # ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8',
# 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']

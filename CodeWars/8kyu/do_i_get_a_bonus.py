#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://www.codewars.com/kata/56f6ad906b88de513f000d96
# It's bonus time in the big city! The fatcats are rubbing their paws in anticipation... but who is going to make the
# most money?
# Build a function that takes in two arguments (salary, bonus). Salary will be an integer, and bonus a boolean.
# If bonus is true, the salary should be multiplied by 10. If bonus is false, the fatcat did not make enough money and
# must receive only his stated salary.
# Return the total figure the individual will receive as a string prefixed with "£" (= "\u00A3", JS, Go, Java, Scala,
# and Julia), "$" (C#, C++, Dart, Ruby, Clojure, Elixir, PHP, Python, Haskell, and Lua) or "¥" (Rust).
def bonus_time(salary: int, bonus: bool) -> str:
    return f'${salary * 10 if bonus else salary}'


print(bonus_time(10000, True))  # '$100000'
print(bonus_time(25000, True))  # '$250000'
print(bonus_time(10000, False))  # '$10000'
print(bonus_time(60000, False))  # '$60000'
print(bonus_time(2, True))  # '$20'
print(bonus_time(78, False))  # '$78'
print(bonus_time(67890, True))  # '$678900'

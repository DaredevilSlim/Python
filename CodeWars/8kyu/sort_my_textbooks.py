#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://www.codewars.com/kata/5a07e5b7ffe75fd049000051
# HELP! Jason can't find his textbook! It is two days before the test date, and Jason's textbooks are all out of order!
# Help him sort a list (ArrayList in java) full of textbooks by subject, so he can study before the test.
# The sorting should NOT be case sensitive
def sorter(textbooks: list) -> list:
    return sorted(textbooks, key=(lambda x: x.lower()))


print(sorter(['Algebra', 'History', 'Geometry', 'English']))  # ['Algebra', 'English', 'Geometry', 'History'],
print(sorter(['Algebra', 'history', 'Geometry', 'english']))  # ['Algebra', 'english', 'Geometry', 'history'],
print(sorter(['Alg#bra', '$istory', 'Geom^try', '**english']))  # ['$istory', '**english', 'Alg#bra', 'Geom^try']

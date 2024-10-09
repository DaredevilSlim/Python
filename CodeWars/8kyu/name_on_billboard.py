#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://www.codewars.com/kata/570e8ec4127ad143660001fd
# You can print your name on a billboard ad. Find out how much it will cost you. Each character has a default price of
# £30, but that can be different if you are given 2 parameters instead of 1 (allways 2 for Java).
# You can not use multiplier "*" operator.
# If your name would be Jeong-Ho Aristotelis, ad would cost £600. 20 leters * 30 = 600 (Space counts as a character).
def billboard(name: str, price=30) -> int:
    return sum(price for letter in name)


print(billboard('Jeong-Ho Aristotelis', ))  # 600
print(billboard('Abishai Charalampos', ))  # 570,
print(billboard('Idwal Augustin', ))  # 420,
print(billboard('Hadufuns John', 20))  # 260,
print(billboard('Zoroaster Donnchadh', ))  # 570,
print(billboard('Claude Miljenko', ))  # 450,
print(billboard('Werner Vigi', 15))  # 165,
print(billboard('Anani Fridumar', ))  # 420,
print(billboard('Paolo Oli', ))  # 270,
print(billboard('Hjalmar Liupold',40))  # 600,
print(billboard('Simon Eadwulf', ))  # 390

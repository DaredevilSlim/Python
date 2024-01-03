#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://www.codewars.com/kata/57b58827d2a31c57720012e8
# In this kata you will have to write a function that takes litres and price_per_litre (in dollar) as arguments.
# Purchases of 2 or more litres get a discount of 5 cents per litre, purchases of 4 or more litres get a discount of 10
# cents per litre, and so on every two litres, up to a maximum discount of 25 cents per litre. But total discount per
# litre cannot be more than 25 cents. Return the total cost rounded to 2 decimal places. Also you can guess that there
# will not be negative or non-numeric inputs.
# Note
# 1 Dollar = 100 Cents
def fuel_price(litres, price_per_litre):
    full_price = litres * price_per_litre * 100
    if 2 >= litres < 4:
        discount = litres * 5
    elif 4 >= litres < 6:
        discount = litres * 10
    elif 6 >= litres < 8:
        discount = litres * 15
    elif 8 >= litres < 10:
        discount = litres * 20
    else:
        discount = litres * 25
    return (full_price - discount) / 100


print(fuel_price(10, 21.5))  # 212.5
print(fuel_price(40, 10))  # 390
print(fuel_price(15, 5.83))  # 83.7

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://www.codewars.com/kata/568d0dd208ee69389d000016
# After a hard quarter in the office you decide to get some rest on a vacation. So you will book a flight for you and
# your girlfriend and try to leave all the mess behind you.
# You will need a rental car in order for you to get around in your vacation. The manager of the car rental makes you
# some good offers.
# Every day you rent the car costs $40. If you rent the car for 7 or more days, you get $50 off your total.
# Alternatively, if you rent the car for 3 or more days, you get $20 off your total.
# Write a code that gives out the total amount for different days(d).
def rental_car_cost(d: int()) -> int():
    return 40 * d - (50 if d >= 7 else 20 if d >= 3 else 0)


print(rental_car_cost(1))  # 40
print(rental_car_cost(4))  # 140
print(rental_car_cost(7))  # 230
print(rental_car_cost(8))  # 270

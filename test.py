#!/usr/bin/env python3
# -*- coding: utf-8 -*-

numbers = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
           10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16:'sixteen',
           17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
           50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: ' hundred'}


def checkio(number):
    if number < 20:
        return numbers[number]
    elif number < 100:
        n_mod = number % 10
        return numbers[number] if n_mod == 0 else numbers[number - n_mod] + ' ' + checkio(n_mod)
    hundred = numbers[number // 100] + numbers[100]
    n_mod = number % 100
    return hundred if n_mod == 0 else hundred + ' ' + checkio(n_mod)


print(checkio(4))  # == 'four', '1st example'
print(checkio(12))  # == 'twelve', '3rd example'
print(checkio(40))  # == 'forty', '6th example'
print(checkio(44))  # == 'forty four', '6th example'
print(checkio(133))  # == 'one hundred thirty-three', '2nd example'
print(checkio(100))  # == 'one hundred one', '4th example'
print(checkio(999))  # == 'one hundred one', '4th example'

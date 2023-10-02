#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# You are given a string of different characters (letters, digits and other symbols). The goal is to "extract" the
# number from the string: concatenate only digits, number sign and "." (if present) and return the result in number
# format. If no number can be extracted (no digits in the given string) - return None. Read preconditions below for some
# additional rules.
# Expected behavior:
# take into consideration the LAST number sign before the FIRST digit;
# take into consideration the FIRST dot in the string (It's guaranteed, that it goes after at least one digit or has at
# least one digit after). If there is a dot, return as float, otherwise - integer.
# Input: String (str).
# Output: Integer (int), float (float) or None.
def reveal_num(line: str) -> int | float | None:
    sign = ''
    result = ''
    for i in range(len(line)):
        if line[i] in '-+' and not result:
            sign += line[i]
        elif line[i].isdigit() or line[i] == '.' and '.' not in result:
            result = line[i] if result == '0' else result + line[i]
    return eval(sign[-1] + result if sign else result) if result else None


print(reveal_num("F0(t}"))  # 0
print(reveal_num("Utc&g"))  # None
print(reveal_num("-aB%|_-+2ADS.12+3.ADS1.2"))  # 2.12312
print(reveal_num("-aB%|_+-2ADS.12+3.ADS1.2"))  # -2.12312
print(reveal_num("zV№1}3;o.vEf``C.WqTY0"))  # 13.0
print(reveal_num("!3B'j=(}89JQ6aWvN*%5@uy.r)B<?pZ.!545ZD^KF9Sx@gqfa*"))  # 38965.5459
print(reveal_num('^B4-zq93GEM--4S}yi5d'))  # 49345
print(reveal_num('v-Iu*B&9viteApr=0k}='))  # -90
print(reveal_num('!#iHL}wcI?KR=X!gF0d&S-1zj&LgJ!`tzbn#mEPV7mL&R2f)W'))  # 172

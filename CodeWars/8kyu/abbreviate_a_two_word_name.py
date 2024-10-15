#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3
# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
# The output should be two capital letters with a dot separating them.
# It should look like this:
# Sam Harris => S.H
# patrick feeney => P.F
def abbrev_name(name: str) -> str:
    return '.'.join(i[0].upper() for i in name.split())


print(abbrev_name("Sam Harris"))  # "S.H"
print(abbrev_name("patrick feenan"))  # "P.F"
print(abbrev_name("Evan C"))  # "E.C"
print(abbrev_name("P Favuzzi"))  # "P.F"
print(abbrev_name("David Mendieta"))  # "D.M"

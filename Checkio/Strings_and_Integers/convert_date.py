#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime

# This function should take a date string in the format dd/mm/yyyy and convert it to the format yyyy-mm-dd. If the input
# is not in the correct format, the function should return an error message "Error: Invalid date.".
# Input: String (str).
# Output: String (str).
# How it’s used:
# in databases, while migrating data from one system to another with different date format requirements;
# in date picker UI components, where user input might be in a different format;
# in reporting tools to standardize date formats across different data sources.
# Preconditions:
# the input should be a string: date ∈ string;
# the input should match the pattern: dd/mm/yyyy, where 01 ≤ dd ≤ 31, 01 ≤ mm ≤ 12, and 1900 ≤ yyyy ≤ 2100.


def convert_date(date: str) -> str:
    try:
        day, month, year = date.split('/')
        date = datetime.date(int(year), int(month), int(day))
    except ValueError as ve:
        date = 'Error: Invalid date.'
    return str(date)


print(convert_date("25/12/2021"))  # "2021-12-25"
print(convert_date("01/01/2000"))  # "2000-01-01"
print(convert_date("15/06/1995"))  # "1995-06-15"
print(convert_date("29/02/2020"))  # "2020-02-29"
print(convert_date("10/10/2010"))  # "2010-10-10"
print(convert_date("31/05/1985"))  # "1985-05-31"
print(convert_date("07/08/1960"))  # "1960-08-07"
print(convert_date("02/09/1999"))  # "1999-09-02"
print(convert_date("30/04/1975"))  # "1975-04-30"
print(convert_date("29/02/2019"))  # "Error: Invalid date."
print(convert_date("30/04/1975/1"))  # "Error: Invalid date."

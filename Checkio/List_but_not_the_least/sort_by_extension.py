#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# You are given a sequence of files as strings. You need to sort this the sequence by the file extension. The files with
# the same extension (or without one) should be sorted by name.
# Some possible cases:
# Filename cannot be an empty string;
# Sorting order: files without name, files without extension, files with name and extension;
# Filename .config or config. is all name with an empty extension;
# Filename like str1.str2.str3 has an extension str3 and a name str1.str2;
# Filename like .str1.str2 has an extension str2 and a name .str1.
# Input: List of strings (str).
# Output: List of strings (str).

def sort_by_ext(files: list[str]) -> list[str]:
    return sorted(files, key=sort_key)


def sort_key(file) -> tuple[str, str]:
    name, ext = file.rsplit('.', 1)
    return (ext, name) if name else ('', ext)


print(sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']))       # ['.aa', '.bat', '1.bat', '1.cad'])
print(sort_by_ext(['1.cad', '1.bat', '1.aa']))              # ['1.aa', '1.bat', '1.cad']
print(sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']))       # ['.aa', '.bat', '1.bat', '1.cad']
print(sort_by_ext(['1.cad', '1.', '1.aa']))                 # ['1.', '1.aa', '1.cad']
print(sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']))  # ['1.aa' '1.bat' '1.cad' '1.aa.doc']
print(sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']))   # ['1.aa' '1.bat' '1.cad' '.aa.doc']
print(sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']))     # ['1.aa', '1.bat', '2.bat', '1.cad']
print(sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']))      # ['.bat', '1.aa', '1.bat', '1.cad']

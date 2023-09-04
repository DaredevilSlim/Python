#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This mission is inspired by the following Brian Bilston's facebook post:
# Split a given text into multiline one with "\n", where each line includes number of words equal to the current
# Fibonacci number.
# Here are some clarifications:
# Fibonacci sequence starts from 0, 1, but the result string should include only non-empty lines;
# in case, there are not enough words for current line - complement to proper length with "_";
# punctuation marks are considered as a part of a previous or next word.
# Let's look at the schematic example ("w" for a word):
# "w w w w w w w w" -> '''w
#                         w
#                         w w
#                         w w w
#                         w _ _ _ _'''
# Input: A string (str).
# Output: A string (str).
def fibo_poem(text: str) -> str:
    # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
    if not text:
        return text
    text = list(map(str, text.split()))
    l = len(text)
    if l == 1:
        return text[0]
    f = [1, 1]
    a = 0
    b = 1
    c = 2
    while c < l:
        d = f[a] + f[b]
        f.append(d)
        a += 1
        b += 1
        c += d
    '''n = list([text[0]])
    e = 0
    g = f[e]
    for i in range(1, len(text)):
        if i == g:
            n += '\n' + text[i]
            e += 1
            g += f[e]
        else:
            n += ' ' + text[i]'''
    return x


print(fibo_poem(""))  # ""
print(fibo_poem("Django framework"))  # "Django\nframework"
print(fibo_poem("Zen of Python"))  # "Zen\nof\nPython _"
print(
    (fibo_poem(
        "There are three kinds of lies: Lies, damned lies, and the benchmarks."
    ))
)  # "There\nare\nthree kinds\nof lies: Lies,\ndamned lies, and the benchmarks."

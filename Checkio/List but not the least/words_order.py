#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# You have a text and a sequence of words. You need to check if the words in sequence appear in the same order as in the
# given text.
# Cases you should expect while solving this challenge:
# a word from the sequence is not in the text - your function should return False;
# any word can appear more than once in a text - use only the first one;
# two words in the given sequence are the same - your function should return False;
# the condition is case sensitive, which means 'hi' and 'Hi' are two different words;
# the text includes only English letters and spaces.
# Input: Two arguments. The first one is a given text as a string (str), the second is list of words as strings (str).
# Output: Logic value (bool).
def words_order(text: str, words: list) -> bool:
    text = list(map(str, text.split()))
    if len(words) != len(set(words)):
        return False
    for i in words:
        if i in text:
            text = text[text.index(i):]
        else:
            return False
    return True


print(words_order("hi world im here", ["country", "world"]))                            # False
print(words_order("hi world im here", ["wo", "rld"]))                                   # False
print(words_order("", ["world", "here"]))                                               # False
print(words_order("hi world im here", ["here", "world"]))                               # False
print(words_order("hi world im here", ["world", "here", "hi"]))                         # False
print(words_order("hi world im here", ["world", "hi", "here"]))                         # False
print(words_order("hi world world im here", ["world", "world"]))                        # False
print(words_order("hi world im here", ["world", "world"]))                              # False
print(words_order("hi world world im here hi world world im here", ["world", "here"]))  # True
print(words_order("hi world im here", ["world", "here"]))                               # True
print(words_order("hi world im here", ["world"]))                                       # True
print(words_order("hi world im here", ["world", "im", "here"]))                         # True

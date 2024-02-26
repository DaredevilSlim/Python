#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# "I Love you soooooo much! You are the best!!"
# Sometimes your friends want to express their feelings in a message, and sometimes a key with a letter gets stuck on
# the keyboard. In both cases we will get a "long-pressed letter" and the letter will then be printed more than once.
# You are given two strings. The first string is the original text message. The second string is a printed message,
# which may contain several (or possibly none) long-pressed letters. It may happen that the message was written in a
# hurry, so do not forget to check that all the letters match those in the original. Return True if the printed message
# matches the original one, taking into account possible long keystrokes. Or False if there are errors or no
# long-pressed letters.
# Input: String (str).
# Output: Logic value (bool).
# Preconditions:
# "text" and "typed" consist of only lowercase English letters and symbols "'/?!.,;
# 1 <= len(text), len(typed) <= 1000.
def long_pressed(text: str, typed: str) -> bool:
    if text == typed:
        return False
    a = False
    for i, j in zip(text.split(), typed.split()):
        if set(i) == set(j):
            for k in set(i):
                if i.count(k) <= j.count(k):
                    a = True
                else:
                    return False
        else:
            return False
    return a


print(long_pressed("alex", "aaleex"))                                        # True
print(long_pressed("welcome to checkio", "weeeelcome to cccheckio"))         # True
print(long_pressed("there is an error here", "there is an errorrr hereaa"))  # False
print(long_pressed("hi, my name is...", "hi, my name is..."))                # False
print(long_pressed('welcome boss!', 'welcooome bos!!'))                      # False

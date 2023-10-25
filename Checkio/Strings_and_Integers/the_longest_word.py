#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This function should take a string without punctuation marks as an input and return the longest word in the string. If
# there are multiple words of the same length, return the first one that appears.
# Input: String (str).
# Output: String (str).
# How it’s used:
# in natural language processing tasks, like text analysis;
# in search algorithms, to find key words or tags in a text.
# Preconditions:
# sentence ∈ string;
# length(sentence) >= 0.
def longest_word(sentence: str) -> str:
    a = ''
    b = 0
    for i in sentence.split():
        if len(i) > b:
            a = i
            b = len(i)
    return a


print(longest_word("hello world"))  # "hello"
print(longest_word("openai gpt-4"))  # "openai"
print(longest_word("this is a sentence"))  # "sentence"
print(longest_word("the quick brown fox"))  # "quick"
print(longest_word("jumped over the lazy dog"))  # "jumped"
print(longest_word("typescript is great"))  # "typescript"
print(longest_word("the answer is 42"))  # "answer"
print(longest_word("to be or not to be"))  # "not"
print(longest_word("that is the question"))  # "question"
print(longest_word(""))  # ""
print(longest_word(" "))  # ""

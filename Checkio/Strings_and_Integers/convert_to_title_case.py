#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Your function should take a string as an input and convert all the first letters of the words in the string to
# uppercase, making the string a title case (other letters must be in lowercase).
# Input: Original string (str).
# Output: Converted string (str).
# How it’s used:
# for text processing and data normalization tasks;
# for rendering text in UI in a standard title case format.
# Preconditions:
# sentence ∈ string;
# length(sentence) >= 0.
def to_title_case(sentence: str) -> str:
    return ' '.join(i.title() for i in sentence.split())


print(to_title_case("hello world"))  # "Hello World"
print(to_title_case("openai gpt-4"))  # "Openai Gpt-4"
print(to_title_case("this is a title"))  # "This Is A Title"
print(to_title_case("THE QUICK BROWN FOX"))  # "The Quick Brown Fox"
print(to_title_case("JUMPs ovER a LAZy dog"))  # "Jumps Over A Lazy Dog"
print(to_title_case("typescript is great"))  # "Typescript Is Great"
print(to_title_case("the answer is 42"))  # "The Answer Is 42"
print(to_title_case("to be or not to be"))  # "To Be Or Not To Be"
print(to_title_case("that is the question"))  # "That Is The Question"
print(to_title_case(""))  # ""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This function should take three strings as input: the main text, the target substring, and the replacement substring.
# It should return a new string where all occurrences of the target substring within the main text are replaced with the
# replacement substring.
# Input: Three strings (str).
# Output: String (str).
# How it’s used:
# in text editors for find-and-replace functionality;
# in data transformation tools to standardize or clean data;
# in website template systems to replace placeholders with actual content.
def replace_all(main_text: str, target: str, repl: str) -> str:
    return main_text.replace(target, repl)


print(replace_all("hello world", "world", "TypeScript"))  # "hello TypeScript"
print(replace_all("hello world world", "world", "TypeScript"))  # "hello TypeScript TypeScript"
print(replace_all("TypeScript is fun", "fun", "awesome"))  # "TypeScript is awesome"
print(replace_all("aaa", "a", "b"))  # "bbb"
print(replace_all("replace all the all", "all", "some"))  # "replace some the some"
print(replace_all("nothing to replace", "something", "nothing"))  # "nothing to replace"
print(replace_all("same same same", "same", "same"))  # "same same same"
print(replace_all("123 123", "123", "321"))  # "321 321"
print(replace_all("OpenAI", "AI", "Source"))  # "OpenSource"
print(replace_all("", "anything", "nothing"))  # ""

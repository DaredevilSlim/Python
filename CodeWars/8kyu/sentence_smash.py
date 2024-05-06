#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Sentence Smash
# Write a function that takes an array of words and smashes them together into a sentence and returns the sentence.
# You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. Be careful,
# there shouldn't be a space at the beginning or the end of the sentence!
def smash(words: list) -> str:
    return ' '.join(words)


print(smash(['hello', 'world']))  # 'hello world'
print(smash(['hello', 'amazing', 'world']))  # 'hello amazing world'
print(smash(['this', 'is', 'a', 'really', 'long', 'sentence']))  # 'this is a really long sentence'

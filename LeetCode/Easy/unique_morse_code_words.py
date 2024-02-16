#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as
# follows:
# 'a' maps to '.-',
# 'b' maps to '-...',
# 'c' maps to '-.-.', and so on.
# For convenience, the full table for the 26 letters of the English alphabet is given below:
# ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...',
# '-','..-','...-','.--','-..-','-.--','--..']
# Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.
# For example, 'cab' can be written as '-.-..--...', which is the concatenation of '-.-.', '.-', and '-...'. We will
# call such a concatenation the transformation of a word.
# Return the number of different transformations among all words we have.
# Example 1:
# Input: words = ['gin','zen','gig','msg']
# Output: 2
# Explanation: The transformation of each word is:
# 'gin' -> '--...-.'
# 'zen' -> '--...-.'
# 'gig' -> '--...--.'
# 'msg' -> '--...--.'
# There are 2 different transformations: '--...-.' and '--...--.'.
# Example 2:
# Input: words = ['a']
# Output: 1
# Constraints:
# 1 <= words.length <= 100
# 1 <= words[i].length <= 12
# words[i] consists of lowercase English letters.
def unique_morse_representations(words: list[str]) -> int:
    morse = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
             'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
             'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
             'y': '-.--', 'z': '--..', ' ': ' '}
    return len(set(''.join(map(lambda x: morse[x], ' '.join(words))).split()))


print(unique_morse_representations(['gin', 'zen', 'gig', 'msg']))  # 2
print(unique_morse_representations(['a']))  # 1

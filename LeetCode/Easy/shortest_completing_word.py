#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given a string licensePlate and an array of strings words, find the shortest completing word in words.
# A completing word is a word that contains all the letters in licensePlate. Ignore numbers and spaces in licensePlate,
# and treat letters as case insensitive. If a letter appears more than once in licensePlate, then it must appear in the
# word the same number of times or more.
# For example, if licensePlate = 'aBc 12c', then it contains letters 'a', 'b' (ignoring case), and 'c' twice. Possible
# completing words are 'abccdef', 'caaacab', and 'cbca'.
# Return the shortest completing word in words. It is guaranteed an answer exists. If there are multiple shortest
# completing words, return the first one that occurs in words.
# Example 1:
# Input: licensePlate = '1s3 PSt', words = ['step','steps','stripe','stepple']
# Output: 'steps'
# Explanation: licensePlate contains letters 's', 'p', 's' (ignoring case), and 't'.
# 'step' contains 't' and 'p', but only contains 1 's'.
# 'steps' contains 't', 'p', and both 's' characters.
# 'stripe' is missing an 's'.
# 'stepple' is missing an 's'.
# Since 'steps' is the only word containing all the letters, that is the answer.
# Example 2:
# Input: licensePlate = '1s3 456', words = ['looks','pest','stew','show']
# Output: 'pest'
# Explanation: licensePlate only contains the letter 's'. All the words contain 's', but among these 'pest', 'stew', and
# 'show' are shortest. The answer is 'pest' because it is the word that appears earliest of the 3.
# Constraints:
# 1 <= licensePlate.length <= 7
# licensePlate contains digits, letters (uppercase or lowercase), or space ' '.
# 1 <= words.length <= 1000
# 1 <= word.length <= 15
# word consists of lower case English letters.
def shortest_completing_word(license_plate: str, words: list[str]) -> str:
    lp = [i.lower() for i in license_plate if i.isalpha()]
    result = list()
    for i in range(len(words)):
        if set(words[i]).issuperset(lp):
            temp = words[i]
            for j in lp:
                temp = temp.replace(j, '', 1)
            len_temp = len(temp)
            count_replace = len(words[i]) - len_temp
            result.append([words[i], count_replace, len_temp, i])
    return sorted(result, key=lambda elem: (elem[1], -elem[2], -elem[3]))[-1][0]


print(shortest_completing_word('1s3 PSt', ['step', 'steps', 'stripe', 'stepple']))  # 'steps'
print(shortest_completing_word('1s3 456', ['looks', 'pest', 'stew', 'show']))  # 'pest'
print(shortest_completing_word('Ah71752', ['suggest', 'letter', 'of', 'husband', 'easy',
                                           'education', 'drug', 'prevent', 'writer', 'old']))  # 'husband'

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not
# banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.
# The words in paragraph are case-insensitive and the answer should be returned in lowercase.
# Example 1:
# Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
# Output: "ball"
# Explanation:
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"),
# and that "hit" isn't the answer even though it occurs more because it is banned.
# Example 2:
# Input: paragraph = "a.", banned = []
# Output: "a"
# Constraints:
# 1 <= paragraph.length <= 1000
# paragraph consists of English letters, space ' ', or one of the symbols: "!?',;.".
# 0 <= banned.length <= 100
# 1 <= banned[i].length <= 10
# banned[i] consists of only lowercase English letters.
def most_common_word(paragraph: str, banned: list[str]) -> str:
    for i in ['!', '?', '\'', ';', ',', '.', '  ']:
        paragraph = paragraph.replace(i, ' ')
    dict_paragraph = dict()
    for word in paragraph.lower().split():
        if word not in banned:
            if word in dict_paragraph:
                dict_paragraph[word] += 1
            else:
                dict_paragraph[word] = 1
    if len(dict_paragraph) == 1:
        return list(dict_paragraph.keys())[0]
    return max(dict_paragraph, key=dict_paragraph.get)


print(most_common_word('Bob hit a ball, the hit BALL flew far after it was hit.', ['hit']))  # ball
print(most_common_word('a.', ['']))  # ball
print(most_common_word('a, a, a, a, b,b,b,c, c', ['a']))  # b
print(most_common_word('Bob. hIt, baLl', ["bob", "hit"]))  # ball

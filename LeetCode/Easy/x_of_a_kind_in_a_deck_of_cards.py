#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# You are given an integer array deck where deck[i] represents the number written on the ith card.
# Partition the cards into one or more groups such that:
# Each group has exactly x cards where x > 1, and
# All the cards in one group have the same integer written on them.
# Return true if such partition is possible, or false otherwise.
# Example 1:
# Input: deck = [1, 2, 3, 4, 4, 3, 2, 1]
# Output: true
# Explanation: Possible partition [1, 1], [2, 2], [3, 3], [4, 4].
# Example 2:
# Input: deck = [1, 1, 1, 2, 2, 2, 3, 3]
# Output: false
# Explanation: No possible partition.
# Constraints:
# 1 <= deck.length <= 104
# 0 <= deck[i] < 104
def has_groups_size_x(deck: list[int]) -> bool:
    deck_dict = dict.fromkeys(set(deck), 0)
    for i in deck:
        deck_dict[i] += 1
    values = deck_dict.values()
    result = dict.fromkeys([7, 5, 3, 2], 0)
    for i in result:
        for j in values:
            if j % i != 0:
                result[i] += 1
                break
    result = result.values()
    return 0 in result


print(has_groups_size_x([1, 2, 3, 4, 4, 3, 2, 1]))  # True
print(has_groups_size_x([1, 1, 2, 2, 2, 2]))  # True
print(has_groups_size_x([1, 1]))  # True
print(has_groups_size_x([1, 1, 1, 1, 2, 2, 2, 2, 2, 2]))  # True
print(has_groups_size_x([0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3]))  # True
print(has_groups_size_x([0, 0, 0, 0, 0, 1, 1, 1, 1, 1]))  # True
print(has_groups_size_x([1, 1, 1, 2, 2, 2, 3, 3]))  # False
print(has_groups_size_x([1]))  # False

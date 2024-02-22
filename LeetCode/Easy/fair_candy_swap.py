#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Alice and Bob have a different total number of candies. You are given two integer arrays aliceSizes and bobSizes where
# aliceSizes[i] is the number of candies of the ith box of candy that Alice has and bobSizes[j] is the number of candies
# of the jth box of candy that Bob has.
# Since they are friends, they would like to exchange one candy box each so that after the exchange, they both have the
# same total amount of candy. The total amount of candy a person has is the sum of the number of candies in each box
# they have.
# Return an integer array answer where answer[0] is the number of candies in the box that Alice must exchange, and
# answer[1] is the number of candies in the box that Bob must exchange. If there are multiple answers, you may return
# any one of them. It is guaranteed that at least one answer exists.
# Example 1:
# Input: aliceSizes = [1,1], bobSizes = [2,2]
# Output: [1,2]
# Example 2:
# Input: aliceSizes = [1,2], bobSizes = [2,3]
# Output: [1,2]
# Example 3:
# Input: aliceSizes = [2], bobSizes = [1,3]
# Output: [2,3]
# Constraints:
# 1 <= aliceSizes.length, bobSizes.length <= 104
# 1 <= aliceSizes[i], bobSizes[j] <= 105
# Alice and Bob have a different total number of candies.
# There will be at least one valid answer for the given input.
def fair_candy_swap(alice_sizes: list[int], bob_sizes: list[int]) -> list[int]:
    sum_a = sum(alice_sizes)
    sum_b = sum(bob_sizes)
    a = sorted(set(alice_sizes))
    b = sorted(set(bob_sizes))
    i = 0
    j = 0
    while sum_a - a[i] + b[j] != sum_b - b[j] + a[i]:
        if sum_a - a[i] + b[j] > sum_b - b[j] + a[i]:
            i += 1
        else:
            j += 1
    return [a[i], b[j]]


print(fair_candy_swap([1, 1], [2, 2]))  # [1, 2]
print(fair_candy_swap([1, 2], [2, 3]))  # [1, 2]
print(fair_candy_swap([2], [1, 3]))  # [2, 3]
print(fair_candy_swap([1, 2, 5], [2, 4]))  # [5, 4]

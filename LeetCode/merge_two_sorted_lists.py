#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two
# lists.
# Return the head of the merged linked list.
# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:
# Input: list1 = [], list2 = []
# Output: []
# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]
# Constraints:
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.
class ListNode:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return f'[{self.value}]->[{self.next}]'

    def add(self, value):
        self.head = ListNode(value, self.head)

    def len(self):
        result = 0
        current = self.head
        while current is not None:
            result += 1
            current = current.next
        return result


def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:
    # while list_node1 is not None and list_node2 is not None:
    #    if list_node1 == list_node2:
    list3 = ListNode()
    n = len(list1)
    m = len(list2)
    print(list1, list2, n, m)


print(merge_two_lists(ListNode([1, 2, 4]), ListNode([1, 3, 4])))  # [1, 1, 2, 3, 4, 4]
print(merge_two_lists([], []))  # []
print(merge_two_lists([], [0]))  # [0]

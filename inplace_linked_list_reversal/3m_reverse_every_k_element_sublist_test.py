"""
Reverse every K-element Sub-list (medium)

Given the head of a LinkedList and a number ‘k’, reverse every
‘k’ sized sub-list starting from the head. If, in the end, you
are left with a sub-list with less than ‘k’ elements, reverse it too.

LeetCode solution:
https://leetcode.com/problems/reverse-nodes-in-k-group/solutions/11491/succinct-iterative-python-o-n-time-o-1-space/?orderBy=most_votes&languageTags=python
"""

from __future__ import annotations

import pytest


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __eq__(self, other) -> bool:
        while self and other and self.value == other.value:
            self = self.next
            other = other.next
        if not self and not other:
            return True
        return False


def reverse_every_k_elements(head: Node, k: int):
    if k == 0 or k == 1:
        return head

    dummy = Node(0, head)
    prev, curr = dummy, dummy.next

    i = 0
    while curr is not None and curr.next is not None:
        if i == k - 1:
            i = 0
            prev = curr
            curr = curr.next
            continue

        temp = curr.next
        curr.next = temp.next
        temp.next = prev.next
        prev.next = temp
        i += 1

    return dummy.next


def reverse(head, end=None):
    curr = head
    prev = end

    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev


@pytest.mark.parametrize(
    "head, k, expected",
    [
        (
            Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8)))))))),
            3,
            Node(3, Node(2, Node(1, Node(6, Node(5, Node(4, Node(8, Node(7)))))))),
        ),
    ],
)
def test_reverse_sub_list(head, k, expected):
    assert reverse_every_k_elements(head, k) == expected

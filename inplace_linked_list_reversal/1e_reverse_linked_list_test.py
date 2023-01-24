"""
Problem Statement
Given the head of a Singly LinkedList, reverse the LinkedList.
Write a function to return the new head of the reversed LinkedList.
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


def reverse(head):
    prev, curr = None, head

    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev


@pytest.mark.parametrize(
    "head, expected",
    [
        (
            Node(2, Node(4, Node(6, Node(8, Node(10))))),
            Node(10, Node(8, Node(6, Node(4, Node(2))))),
        ),
    ],
)
def test_grokking(head, expected):
    assert reverse(head) == expected

"""
Rotate a LinkedList (medium)

Given the head of a Singly LinkedList and a number ‘k’, rotate the
LinkedList to the right by ‘k’ nodes

Great LeetCode solution:
https://leetcode.com/problems/rotate-list/solutions/348197/96-faster-simple-python-solution-with-explanation/?orderBy=most_votes&languageTags=python3
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


def rotate(head, rotations: int) -> Node:
    if rotations < 1:
        return head

    len = 1
    last = head
    while last.next is not None:
        last = last.next
        len += 1
    while rotations > len:
        rotations -= len + 1

    i = 0
    end = head
    while i + 1 < rotations:
        end = end.next
        i += 1

    temp = end.next
    end.next = None
    last.next = head

    return temp


@pytest.mark.parametrize(
    "head, rotations, expected",
    [
        (
            Node(1, Node(2, Node(3, Node(4, Node(5, Node(6)))))),
            3,
            Node(4, Node(5, Node(6, Node(1, Node(2, Node(3)))))),
        ),
        (
            Node(1, Node(2, Node(3, Node(4, Node(5))))),
            8,
            Node(3, Node(4, Node(5, Node(1, Node(2))))),
        ),
    ],
)
def test_rotate(head, rotations, expected):
    assert rotate(head, rotations) == expected

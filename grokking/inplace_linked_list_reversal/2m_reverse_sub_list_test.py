"""
Reverse a Sub-list (medium)

Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse
the LinkedList from position ‘p’ to ‘q’.
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


# elegant leetcode solution
def reverse_sub_list_leetcode(head: Node, left: int, right: int) -> Node:
    dummy = Node(0)
    dummy.next = head

    prev = dummy
    curr = dummy.next

    # find the position
    for _ in range(1, left):
        curr = curr.next  # type: ignore
        prev = prev.next  # type: ignore

    # reverse
    for _ in range(right - left):
        # we use curr.next as we should start from prev.next
        temp = curr.next  # type: ignore
        curr.next = temp.next  # type: ignore

        temp.next = prev.next  # type: ignore
        prev.next = temp  # type: ignore

    return dummy.next


# my code
def reverse_sub_list_custom(head: Node, p: int, q: int):
    slow, i = head, 0
    start_prev, end = None, None
    while (start_prev is None or end is None) and slow is not None:
        if i + 2 == p:
            start_prev = slow
        if i + 1 == q:
            end = slow
        i += 1
        slow = slow.next

    temp = end.next  # type: ignore
    end.next = None  # type: ignore
    reversed_sublist_head = reverse(start_prev.next, temp)  # type: ignore
    start_prev.next = reversed_sublist_head  # type: ignore

    return start_prev


def reverse(head, end=None):
    curr = head
    prev = end

    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev


# @pytest.mark.parametrize(
#     "head, p, q, expected",
#     [
#         (
#             Node(1, Node(2, Node(3, Node(4, Node(5))))),
#             2,
#             4,
#             Node(1, Node(4, Node(3, Node(2, Node(5))))),
#         ),
#     ],
# )
# def test_grokking(head, p, q, expected):
#     assert reverse_sub_list_leetcode(head, p, q) == expected
#     assert reverse_sub_list_custom(head, p, q) == expected


@pytest.mark.parametrize(
    "head, p, q, expected",
    [
        (
            Node(1, Node(2, Node(3, Node(4, Node(5))))),
            2,
            4,
            Node(1, Node(4, Node(3, Node(2, Node(5))))),
        ),
        (Node(5), 1, 1, Node(5)),
    ],
)
def test_leetcode(head, p, q, expected):
    assert reverse_sub_list_leetcode(head, p, q) == expected

"""
Reverse alternating K-element Sub-list (medium) #

Given the head of a LinkedList and a number ‘k’, reverse every alternating
‘k’ sized sub-list starting from the head. If, in the end, you are left
with a sub-list with less than ‘k’ elements, reverse it too.
"""

from __future__ import annotations

import copy

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


# my code
def reverse_alternate_k_elements(head: Node, k: int) -> Node:
    if k < 2:
        return head

    dummy = Node(0, head)
    prev, curr = dummy, dummy.next

    i, j = 0, 0  # moves, groups passed
    while curr is not None and curr.next is not None:
        # proceed to next group
        if i == k + 1:
            i = 0
            j += 1

        if j % 2 == 0:
            # reverse
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
            i += 2  # when reversing, already passed 2 elements
        else:
            # go to the next one
            prev, curr = curr, curr.next

        i += 1

    return dummy.next  # type: ignore


def reverse_alternate_k_elements_grokking(head, k):
    if k <= 1 or head is None:
        return head

    current, previous = head, None
    while True:
        last_node_of_previous_part = previous
        # after reversing the LinkedList 'current' will become the last node of the sub-list
        last_node_of_sub_list = current
        next = None  # will be used to temporarily store the next node

        # reverse 'k' nodes
        i = 0
        while current is not None and i < k:
            next = current.next
            current.next = previous
            previous = current
            current = next
            i += 1

        # connect with the previous part
        if last_node_of_previous_part is not None:
            last_node_of_previous_part.next = previous
        else:
            head = previous

        # connect with the next part
        last_node_of_sub_list.next = current

        # skip 'k' nodes
        i = 0
        while current is not None and i < k:
            previous = current
            current = current.next
            i += 1

        if current is None:
            break
    return head


@pytest.mark.parametrize(
    "head, k, expected",
    [
        (
            Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8)))))))),
            2,
            Node(2, Node(1, Node(3, Node(4, Node(6, Node(5, Node(7, Node(8)))))))),
        ),
    ],
)
def test_reverse_alternate_k_elements(head, k, expected):
    assert reverse_alternate_k_elements(copy.deepcopy(head), k) == expected
    assert reverse_alternate_k_elements_grokking(copy.deepcopy(head), k) == expected

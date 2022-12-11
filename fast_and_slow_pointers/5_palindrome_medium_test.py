"""
Given the head of a Singly LinkedList, write a method to check
if the LinkedList is a palindrome or not.

Your algorithm should use constant space and the input LinkedList
should be in the original form once the algorithm is finished.
The algorithm should have O(N) time complexity where ‘N’ is
the number of nodes in the LinkedList.
"""

from collections import defaultdict
from typing import Optional


class Node:
    def __init__(self, value, next: Optional["Node"] = None):
        self.value = value
        self.next = next


def is_palindromic_linked_list(head: Optional[Node]):
    ...


def is_palindromic_circular_linked_list(head: Optional[Node]):
    if head is None:
        return False

    tail = None
    fast = slow = head
    value_freq_map, matched, list_len = defaultdict(int), 0, 0
    while slow is not None:
        list_len += 1

        if fast.next is None:
            """
            linked list is even, meaning it could have a palindrome
            we make it circular to continue comparing values
            """
            tail = fast
            fast.next = head
        elif fast is None or fast.next.next:
            """
            means this linked list is odd, so it could not be a palindrome
            """
            return False

        value_freq_map[slow.value] += 1
        if value_freq_map[slow.value] == 2:
            matched += 1
        if value_freq_map[fast.value] == 2:
            matched += 1

        slow = slow.next
        fast = fast.next.next

    return matched == list_len


def test():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)
    assert is_palindromic_linked_list(head) is True

    head.next.next.next.next.next = Node(2)
    assert is_palindromic_linked_list(head) is False

    assert is_palindromic_linked_list(None) is True
    assert is_palindromic_linked_list(Node(1)) is True

"""
Given the head of a Singly LinkedList, write a method to check
if the LinkedList is a palindrome or not.

Your algorithm should use constant space and the input LinkedList
should be in the original form once the algorithm is finished.
The algorithm should have O(N) time complexity where ‘N’ is
the number of nodes in the LinkedList.
"""

from typing import Optional


class Node:
    def __init__(self, value, next: Optional["Node"] = None):
        self.value = value
        self.next = next


def is_palindromic_linked_list(head: Optional["Node"]):
    if head is None or head.next is None:
        return True

    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next  # type: ignore
        fast = fast.next.next

    head_second_half = reverse(slow)
    copy_head_second_half = head_second_half
    while head is not None and head_second_half is not None:
        if head.value != head_second_half.value:
            break  # for the second half to reverse at the end of the function
        head = head.next
        head_second_half = head_second_half.next

    reverse(copy_head_second_half)

    if head is None or head_second_half is None:
        return True

    return False


def reverse(head):
    prev = None
    while head is not None:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev


def test_odd():
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


def test_even():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(4)
    head.next.next.next = Node(2)
    assert is_palindromic_linked_list(head) is True

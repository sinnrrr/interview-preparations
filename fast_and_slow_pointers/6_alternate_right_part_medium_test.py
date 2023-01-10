"""
Problem Challenge 2
Rearrange a LinkedList (medium)

Given the head of a Singly LinkedList, write a method to modify the LinkedList
such that the nodes from the second half of the LinkedList are inserted
alternately to the nodes from the first half in reverse order.

So if the LinkedList has nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null, your method
should return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.

Your algorithm should not use any extra space and the input LinkedList should
be modified in-place.

Example 1:
Input: 2 -> 4 -> 6 -> 8 -> 10 -> 12 -> null
Output: 2 -> 12 -> 4 -> 10 -> 6 -> 8 -> null

Example 2:
Input: 2 -> 4 -> 6 -> 8 -> 10 -> null
Output: 2 -> 10 -> 4 -> 8 -> 6 -> null
"""


from typing import Optional


class ListNode:
    def __init__(self, value, next: Optional["ListNode"] = None):
        self.val = value
        self.next = next

    def to_array(self):
        temp = self
        arr = []
        while temp is not None:
            arr.append(temp.val)
            temp = temp.next

        return arr


def reorder(head):
    if head is None:
        return head

    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    curr_p2 = reverse(slow)
    curr_p1, next_p1 = head, None
    while curr_p2 is not None:
        next_p1 = curr_p1.next
        next_p2 = curr_p2.next
        if curr_p2 == curr_p1.next:
            break
        curr_p1.next = curr_p2
        curr_p1.next.next = next_p1  # type: ignore
        curr_p1 = next_p1
        curr_p2 = next_p2

    return head.to_array()


def reverse(head):
    prev = None
    while head is not None:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev


def test_even():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    assert reorder(head) == [1, 4, 2, 3]


def test_odd():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    assert reorder(head) == [1, 5, 2, 4, 3]

"""
Given the head of a Singly LinkedList that contains a cycle, write a function
to find the starting node of the cycle.
"""
from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end="")
            temp = temp.next
        print()


def find_cycle_start(head):
    fast = slow = head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return _find_cycle_start(head, fast)

    return None


def _find_cycle_start(head, meet_point):
    p1 = head
    p2 = meet_point

    while p1 != p2:
        if p1 == meet_point:
            return None
        p1 = p1.next
        p2 = p2.next

    return p1


def test():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)

    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    assert find_cycle_start(head) == 3

    head.next.next.next.next.next.next = head.next.next.next
    assert find_cycle_start(head) == 4

    head.next.next.next.next.next.next = head
    assert find_cycle_start(head) == 1

"""
Given the head of a Singly LinkedList, write a function to determine if the
LinkedList has a cycle in it or not.
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def has_cycle(head):
    slow = fast = head

    """
    Checking if next is not empty to have a next next element.
    First condition checks if that element is empty on the next iteration.
    """
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
    return False


def test():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    assert not has_cycle(head)

    head.next.next.next.next.next.next = head.next.next
    assert has_cycle(head)

    head.next.next.next.next.next.next = head.next.next.next
    assert has_cycle(head)

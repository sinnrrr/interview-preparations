from typing import Optional

import pytest


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_linked_list(ll):
    if ll is None:
        return

    print(ll.val)
    print_linked_list(ll.next)


def compare_lists(l1: ListNode, l2: ListNode) -> bool:
    l1_temp = l1
    l2_temp = l2

    while l1_temp is not None and l2_temp is not None:
        if l1_temp.val != l2_temp.val:
            return False
        l1_temp = l1_temp.next
        l2_temp = l2_temp.next

    if l1_temp is not None or l2_temp is not None:
        return False

    return True

def reverse_list(head):
        prev = None
        current = head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev


class RecursiveSolution:

    def addTwoNumbers(self, l1: Optional[ListNode],
                      l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None or l2 is None:
            return None

        l3 = ListNode()

        def recurse(acc: ListNode, l1: ListNode, l2: ListNode, excess=0):
            excess, acc.val = divmod(l1.val + l2.val + excess, 10)

            if l1.next is None and l2.next is None:
                if excess != 0:
                    acc.next = ListNode(excess)

                return

            acc.next = ListNode()

            recurse(acc.next, l1.next or ListNode(), l2.next or ListNode(),
                    excess)

        recurse(l3, l1, l2)

        return l3


class IterativeSolution:

    def addTwoNumbers(self, l1: Optional[ListNode],
                      l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        header = temp = ListNode()
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            carry, val = divmod(carry, 10)
            temp.next = ListNode(val)  # type: ignore
            temp = temp.next

        # just not to make obscure loop conditions
        # we don't handle first element and just returning
        # next one, because this is where loop starts to output results
        return header.next


class DoublePointerSolution:

    def addTwoNumbers(self, l1: Optional[ListNode],
                      l2: Optional[ListNode]) -> Optional[ListNode]:


Solution = DoublePointerSolution


@pytest.mark.parametrize(
    "arr1,arr2,expected",
    [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
    ],
)
def test_solution(arr1, arr2, expected):

    def fulfill(arr, acc: ListNode):
        acc.val = arr[0]
        arr.pop(0)

        if len(arr) == 0:
            return

        if acc.next is None:
            acc.next = ListNode()

        fulfill(arr, acc.next)

    l1, l2, l_expected = ListNode(), ListNode(), ListNode()
    fulfill(arr1, l1)
    fulfill(arr2, l2)
    fulfill(expected, l_expected)

    l3 = Solution().addTwoNumbers(l1, l2)
    if l3 is None:
        raise ValueError("One of the provided linked lists are empty")

    print_linked_list(l3)

    assert compare_lists(l3, l_expected)

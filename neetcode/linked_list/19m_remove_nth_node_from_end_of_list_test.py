from typing import Optional

import pytest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other) -> bool:
        while self and other and self.val == other.val:
            self = self.next
            other = other.next
        if not self and not other:
            return True
        return False


class Solution:
    # def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    #     count = 0
    #     curr = head
    #     while curr:
    #         curr = curr.next
    #         count += 1

    #     count -= n
    #     prev = head
    #     while count:
    #         count -= 1
    #         prev = prev.next
    #     prev.next = prev.next.next
    #     return head

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left, right = dummy, head
        while n > 0 and right:
            right = right.next
            n -= 1
        while right:
            right = right.next
            left = left.next
        left.next = left.next.next
        return dummy.next


@pytest.mark.parametrize(
    "head, n, expected",
    [
        (
            ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))),
            2,
            ListNode(1, ListNode(2, ListNode(3, ListNode(5)))),
        ),
        (
            ListNode(1),
            1,
            None,
        ),
    ],
)
def test_solution(head, n, expected):
    Solution().removeNthFromEnd(head, n)

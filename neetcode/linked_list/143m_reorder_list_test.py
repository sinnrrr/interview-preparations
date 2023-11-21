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
    # def reorderList(self, head) -> None:
    #     prev_end, curr_end = None, head
    #     while curr_end.next:
    #         prev_end = curr_end
    #         curr_end = curr_end.next

    #     curr_start = head
    #     while curr_start.val != curr_end.val:
    #         # save new state
    #         next_start = curr_start.next.next
    #         temp = curr_start.next
    #         # modifications
    #         curr_end.next = next_start
    #         curr_start.next = curr_end
    #         # update state
    #         curr_end = temp
    #         prev_end.next = curr_end
    #         curr_start = next_start

    def reorderList(self, head) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2


@pytest.mark.parametrize(
    "head, expected",
    [
        (
            ListNode(1, ListNode(2, ListNode(3, ListNode(4)))),
            ListNode(1, ListNode(4, ListNode(2, ListNode(3)))),
        )
        # (
        #     ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))),
        #     ListNode(1, ListNode(4, ListNode(2, ListNode(3)))),
        # )
    ],
)
def test_reverse_sub_list(head, expected):
    Solution().reorderList(head)
    assert head == expected

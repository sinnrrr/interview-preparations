from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or k == 1:
            return head

        dummy = ListNode(0, head)
        prev, curr = dummy, dummy.next

        i = 0
        while curr is not None and curr.next is not None:
            if i == k - 1:
                i = 0
                prev = curr
                curr = curr.next
                continue

            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
            i += 1

        return dummy.next

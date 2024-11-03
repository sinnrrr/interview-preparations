from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        flat_list = []
        for node in lists:
            if not node:
                continue
            curr = node
            while curr:
                flat_list.append(curr)
                curr = curr.next

        flat_list.sort(key=lambda node: node.val)

        dummy = ListNode(0)
        prev = dummy
        for curr in flat_list:
            prev.next = curr
            prev = curr

        return dummy.next


def test():
    node = Solution().mergeKLists(
        [
            ListNode(1, ListNode(4, ListNode(5))),
            ListNode(1, ListNode(3, ListNode(4))),
            ListNode(2, ListNode(6)),
        ]
    )

    vals = []
    curr = node
    while curr:
        vals.append(curr.val)
        curr = curr.next

    assert vals == [1, 1, 2, 3, 4, 4, 5, 6]

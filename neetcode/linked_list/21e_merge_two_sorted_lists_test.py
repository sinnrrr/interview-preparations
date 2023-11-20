from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val < list2.val:
            master = dummy = list1
            slave = list2
        else:
            master = dummy = list2
            slave = list1

        while slave:
            master_next = master.next
            if master.val <= slave.val and (
                master_next is None or master_next.val >= slave.val
            ):
                master.next = slave
                saved_slave_next = slave.next
                slave.next = master_next
                slave = saved_slave_next
                master = master.next
            else:
                master = master.next

        return dummy

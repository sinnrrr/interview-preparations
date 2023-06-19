"""
Connect All Level Order Siblings (medium)

Given a binary tree, connect each node with its level order successor.
The last node of each level should point to the first node of the next level.
"""


from collections import deque
from typing import Optional

import pytest


class TreeNode:
    def __init__(self, val, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def sequence(self) -> list[int]:
        """
        add only left nodes every time and iterate whole level
        """
        ans = []
        curr = self
        while curr:
            ans.append(curr.val)
            curr = curr.next
        return ans


def connect_all_siblings(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None

    queue = deque([root])
    while queue:
        curr = queue.popleft()
        if curr.left is not None:
            queue.append(curr.left)
        if curr.right is not None:
            queue.append(curr.right)

        if len(queue) == 0:
            break
        curr.next = queue[0]
    return root


@pytest.mark.parametrize(
    "root, expected",
    [
        (
            TreeNode(
                1,
                left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)),
                right=TreeNode(3, left=TreeNode(6), right=TreeNode(7)),
            ),
            [1, 2, 3, 4, 5, 6, 7],
        ),
        (
            TreeNode(
                12,
                left=TreeNode(7, left=TreeNode(9)),
                right=TreeNode(1, left=TreeNode(10), right=TreeNode(5)),
            ),
            [12, 7, 1, 9, 10, 5],
        ),
    ],
)
def test_connect_all_siblings(root, expected):
    connect_all_siblings(root)
    assert root.sequence() == expected

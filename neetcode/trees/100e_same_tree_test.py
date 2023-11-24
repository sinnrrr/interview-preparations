from collections import deque
from typing import Optional

import pytest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, __value: object) -> bool:
        if not self and not __value:
            return True
        if self.val == __value.val:
            return True
        return False


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSameTreeIterative(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue: deque[tuple[Optional[TreeNode], Optional[TreeNode]]] = deque([(p, q)])
        while queue:
            node1, node2 = queue.popleft()
            if node1 != node2:
                return False
            if node1 and node2:
                if node1.left and node2.left:
                    queue.append((node1.left, node2.left))
                if node1.right and node2.right:
                    queue.append((node1.right, node2.right))
        return True


@pytest.mark.parametrize(
    "p, q, expected",
    [
        (
            TreeNode(1, TreeNode(2), TreeNode(3)),
            TreeNode(1, TreeNode(2), TreeNode(3)),
            True,
        )
    ],
)
def test_solution(p, q, expected):
    assert Solution().isSameTree(p, q) == expected
    assert Solution().isSameTreeIterative(p, q) == expected

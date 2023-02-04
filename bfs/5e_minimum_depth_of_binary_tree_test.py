"""
Minimum Depth of a Binary Tree (easy)

Find the minimum depth of a binary tree. The minimum depth is the number of nodes along
the shortest path from the root node to the nearest leaf node
"""


from collections import deque
from typing import Optional

import pytest


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_minimum_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    ans = 0
    queue = deque([root])

    while queue:
        ans += 1
        for _ in range(len(queue)):
            curr = queue.popleft()
            if curr.left is None and curr.right is None:
                return ans
            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)

    return ans


@pytest.mark.parametrize(
    "root, expected",
    [
        (
            TreeNode(
                1,
                left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)),
                right=TreeNode(3),
            ),
            2,
        ),
        (
            TreeNode(
                12,
                left=TreeNode(7, left=TreeNode(9)),
                right=TreeNode(
                    1, left=TreeNode(10, left=TreeNode(11)), right=TreeNode(5)
                ),
            ),
            3,
        ),
    ],
)
def test_grokking(root, expected):
    assert find_minimum_depth(root) == expected

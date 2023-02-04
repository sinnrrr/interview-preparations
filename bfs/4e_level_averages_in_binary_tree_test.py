"""
Level Averages in a Binary Tree (easy)

Given a binary tree, populate an array to represent the averages of all of its levels
"""

from collections import deque
from typing import Optional

import pytest


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_level_avarages(root: Optional[TreeNode]) -> list[int]:
    if not root:
        return []

    ans = []
    queue = deque([root])

    while queue:
        lvl_size = len(queue)
        lvl_sum = 0

        for _ in range(lvl_size):
            curr = queue.popleft()
            lvl_sum += curr.val

            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)

        ans.append(lvl_sum / lvl_size)

    return ans


@pytest.mark.parametrize(
    "root, expected",
    [
        (
            TreeNode(
                1,
                left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)),
                right=TreeNode(3, left=TreeNode(6), right=TreeNode(7)),
            ),
            [1, 2.5, 5.5],
        ),
    ],
)
def test_traverse(root, expected):
    assert find_level_avarages(root) == expected

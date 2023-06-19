"""
Reverse Level Order Traversal (easy)

Given a binary tree, populate an array to represent its level-by-level
traversal in reverse order, i.e., the lowest level comes first.
You should populate the values of all nodes in each level from left to right
in separate sub-arrays.
"""


from collections import deque
from typing import Optional

import pytest


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traverse_reverse(root: Optional[TreeNode]) -> list[list[int]]:
    if root is None:
        return []

    ans: deque[list[int]] = deque()
    queue: deque[TreeNode] = deque([root])

    while queue:
        lvl_size = len(queue)
        lvl_values = []

        for _ in range(lvl_size):
            curr = queue.popleft()
            lvl_values.append(curr.val)

            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)

        ans.appendleft(lvl_values)

    return list(ans)


@pytest.mark.parametrize(
    "root, expected",
    [
        (
            TreeNode(
                12,
                left=TreeNode(7, left=TreeNode(9)),
                right=TreeNode(1, left=TreeNode(10), right=TreeNode(5)),
            ),
            [[9, 10, 5], [7, 1], [12]],
        ),
    ],
)
def test_grokking(root, expected):
    assert traverse_reverse(root) == expected

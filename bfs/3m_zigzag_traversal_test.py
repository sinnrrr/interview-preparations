"""
Zigzag Traversal (medium)

Given a binary tree, populate an array to represent its zigzag level order traversal.
You should populate the values of all nodes of the first level from left to right,
then right to left for the next level and keep alternating in the same manner for the
following levels.
"""


from collections import deque
from typing import Optional

import pytest


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traverse_zigzag(root: Optional[TreeNode]) -> list[list[int]]:
    ans = []
    if not root:
        return ans

    queue: deque[TreeNode] = deque()
    queue.append(root)

    appendToEnd = True
    while queue:
        lvl_size = len(queue)
        lvl_values: deque[int] = deque()

        for _ in range(lvl_size):
            curr = queue.popleft()

            if appendToEnd:
                lvl_values.append(curr.val)
            else:
                lvl_values.appendleft(curr.val)

            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)

        ans.append(list(lvl_values))
        appendToEnd = not appendToEnd

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
            [[1], [3, 2], [4, 5, 6, 7]],
        ),
    ],
)
def test_traverse_zigzag(root, expected):
    assert traverse_zigzag(root) == expected

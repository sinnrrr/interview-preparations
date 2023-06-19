"""
All Paths for a Sum (medium)

Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that the
sum of all the node values of each path equals ‘S’.
"""

from typing import Optional

import pytest


class TreeNode:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths(root: Optional[TreeNode], path_sum: int) -> list[list[int]]:
    ans: list[list[int]] = []
    if not root:
        return ans

    stack = [(root, [root.val])]
    while stack:
        curr, path = stack.pop()

        if not curr.left and not curr.right and sum(path) == path_sum:
            ans.append(path)
        if curr.left:
            stack.append((curr.left, path + [curr.left.val]))
        if curr.right:
            stack.append((curr.right, path + [curr.right.val]))

    return ans


@pytest.mark.parametrize(
    "root, sum, expected",
    [
        (
            TreeNode(
                1,
                left=TreeNode(
                    7,
                    left=TreeNode(4),
                    right=TreeNode(5),
                ),
                right=TreeNode(
                    9,
                    left=TreeNode(2),
                    right=TreeNode(7),
                ),
            ),
            12,
            [[1, 9, 2], [1, 7, 4]],
        ),
        (
            TreeNode(
                12,
                left=TreeNode(
                    7,
                    left=TreeNode(4),
                ),
                right=TreeNode(
                    1,
                    left=TreeNode(10),
                    right=TreeNode(5),
                ),
            ),
            23,
            [[12, 1, 10], [12, 7, 4]],
        ),
    ],
)
def test_find_paths(root, sum, expected):
    assert find_paths(root, sum) == expected

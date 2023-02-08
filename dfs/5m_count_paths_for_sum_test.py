"""
Count Paths for a Sum (medium)

Given a binary tree and a number ‘S’, find all paths in the tree such that the sum
of all the node values of each path equals ‘S’.

Please note that the paths can start or end at any node but all paths must follow
direction from parent to child (top to bottom).
"""


from __future__ import annotations

from collections import deque
from typing import Optional

import pytest


class TreeNode:
    def __init__(
        self,
        val: int,
        left: Optional[TreeNode] = None,
        right: Optional[TreeNode] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


def count_paths(root: Optional[TreeNode], target_sum: int) -> int:
    ans = 0
    if not root:
        return ans

    stack = [(root, deque())]
    while stack:
        curr, path = stack.pop()
        path = path.copy()
        path.append(curr.val)

        if curr.left:
            stack.append((curr.left, path))
        if curr.right:
            stack.append((curr.right, path))

        curr_sum = sum(path)
        if abs(curr_sum) > abs(target_sum) and len(path) >= 2:
            path.pop()
            path.popleft()
            stack.append((curr, path))

        if curr_sum == target_sum:
            ans += 1

    return ans


@pytest.mark.parametrize(
    "root, S, expected",
    [
        (
            TreeNode(
                1,
                left=TreeNode(7, left=TreeNode(6), right=TreeNode(5)),
                right=TreeNode(
                    9,
                    left=TreeNode(2),
                    right=TreeNode(3),
                ),
            ),
            12,
            3,
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
            11,
            2,
        ),
    ],
)
def test_grokking(root, S, expected):
    assert count_paths(root, S) == expected


@pytest.mark.parametrize(
    "root, S, expected",
    [
        (
            TreeNode(1, left=TreeNode(2)),
            2,
            1,
        ),
        (
            TreeNode(-2, right=TreeNode(-3)),
            -3,
            1,
        ),
        # (
        #     TreeNode(1, left=TreeNode(-2), right=TreeNode(-3)),
        #     -2,
        #     2,
        # )
    ],
)
def test_leetcode(root, S, expected):
    assert count_paths(root, S) == expected

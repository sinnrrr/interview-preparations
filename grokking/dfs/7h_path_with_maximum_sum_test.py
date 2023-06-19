"""
Path with Maximum Sum (hard)

Find the path with the maximum sum in a given binary tree. Write a function that returns
the maximum sum. A path can be defined as a sequence of nodes between any two nodes and
doesn’t necessarily pass through the root.
"""

from __future__ import annotations

import math
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


def find_maximum_path_sum(root: Optional[TreeNode]):
    max_sum = -math.inf

    def calculate_path_sum(curr: Optional[TreeNode]):
        if not curr:
            return 0
        nonlocal max_sum
        left_tree_sum = calculate_path_sum(curr.left)
        right_tree_sum = calculate_path_sum(curr.right)
        max_sum = max(max_sum, left_tree_sum + right_tree_sum + curr.val)
        # ignore negative sum, fallback to 0
        # since we need the max sum, we won't pay attention to the negative sum subtree
        return max(max(left_tree_sum, right_tree_sum) + curr.val, 0)

    calculate_path_sum(root)
    return max_sum


@pytest.mark.parametrize(
    "root, expected",
    [
        (
            TreeNode(
                1,
                left=TreeNode(2, left=TreeNode(4)),
                right=TreeNode(
                    3,
                    left=TreeNode(5),
                    right=TreeNode(6),
                ),
            ),
            16,
        ),
        (
            TreeNode(
                1,
                left=TreeNode(2, left=TreeNode(1), right=TreeNode(3)),
                right=TreeNode(
                    3,
                    left=TreeNode(
                        5,
                        left=TreeNode(7),
                        right=TreeNode(8),
                    ),
                    right=TreeNode(
                        6,
                        left=TreeNode(9),
                    ),
                ),
            ),
            31,
        ),
        (
            TreeNode(
                -1,
                left=TreeNode(-3),
            ),
            -1,
        ),
    ],
)
def test_grokking(root, expected):
    assert find_maximum_path_sum(root) == expected

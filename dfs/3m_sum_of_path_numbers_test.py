"""
Sum of Path Numbers (medium)

Given a binary tree where each node can only have a digit (0-9) value, each
root-to-leaf path will represent a number. Find the total sum of all the numbers
represented by all paths.
"""

from __future__ import annotations

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


def find_sum_of_path_numbers(root: Optional[TreeNode]) -> int:
    ans = 0
    if not root:
        return ans

    stack = [(root, str(root.val))]
    while stack:
        curr, str_num = stack.pop()

        if not curr.left and not curr.right:
            ans += int(str_num)
        if curr.left:
            stack.append((curr.left, str_num + str(curr.left.val)))
        if curr.right:
            stack.append((curr.right, str_num + str(curr.right.val)))
    return ans


# I like it!
def find_sum_of_path_numbers_leetcode(root: Optional[TreeNode]) -> int:
    stack, res = [], 0
    if root:
        stack.append(root)
    while stack:
        node = stack.pop()
        if not node.left and not node.right:
            res += node.val
        if node.right:
            node.right.val += node.val * 10
            stack.append(node.right)
        if node.left:
            node.left.val += node.val * 10
            stack.append(node.left)
    return res


@pytest.mark.parametrize(
    "root, expected",
    [
        (
            TreeNode(
                1,
                left=TreeNode(
                    7,
                ),
                right=TreeNode(
                    9,
                    left=TreeNode(2),
                    right=TreeNode(9),
                ),
            ),
            408,
        ),
        (
            TreeNode(
                1,
                left=TreeNode(
                    0,
                    left=TreeNode(1),
                ),
                right=TreeNode(
                    1,
                    left=TreeNode(6),
                    right=TreeNode(5),
                ),
            ),
            332,
        ),
    ],
)
def test_grokking(root, expected):
    assert find_sum_of_path_numbers(root) == expected
    assert find_sum_of_path_numbers_leetcode(root) == expected

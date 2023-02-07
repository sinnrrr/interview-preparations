"""
Path With Given Sequence (medium)

Given a binary tree and a number sequence, find if the sequence is present as a
root-to-leaf path in the given tree.
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


def find_path(root: Optional[TreeNode], sequence: list[int]) -> bool:
    stack, n = [], len(sequence)
    if root and root.val == sequence[0]:
        stack.append((root, 1))
    while stack:
        curr, i = stack.pop()
        if not curr.left and not curr.right and i == n:
            return True
        if curr.left and curr.left.val == sequence[i]:
            stack.append((curr.left, i + 1))
        if curr.right and curr.right.val == sequence[i]:
            stack.append((curr.right, i + 1))
    return False


def find_path_better(root: Optional[TreeNode], sequence: list[int]) -> bool:
    if not root or not sequence:
        return False

    stack: list[tuple[TreeNode, int]] = [(root, 0)]
    n = len(sequence)
    while stack:
        curr, i = stack.pop()
        if curr.val != sequence[i]:
            continue

        if not curr.left and not curr.right and i + 1 == n:
            return True
        if curr.left:
            stack.append((curr.left, i + 1))
        if curr.right:
            stack.append((curr.right, i + 1))
    return False


@pytest.mark.parametrize(
    "root, sequence, expected",
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
            [1, 9, 9],
            True,
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
            [1, 0, 7],
            False,
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
            [1, 1, 6],
            True,
        ),
    ],
)
def test_grokking(root, sequence, expected):
    assert find_path(root, sequence) == expected
    assert find_path_better(root, sequence) == expected

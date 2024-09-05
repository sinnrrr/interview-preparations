# Definition for a binary tree node.
from typing import Optional

import pytest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_array(cls, arr):
        if not arr:
            return None

        root = cls(arr[0])
        queue = [root]
        i = 1
        while i < len(arr):
            current = queue.pop(0)

            if i < len(arr) and arr[i] is not None:
                current.left = cls(arr[i])
                queue.append(current.left)
            i += 1

            if i < len(arr) and arr[i] is not None:
                current.right = cls(arr[i])
                queue.append(current.right)
            i += 1

        return root


def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    max_diameter = 0

    def depth(node: Optional[TreeNode]):
        nonlocal max_diameter
        if not node:
            return 0
        left = depth(node.left)
        right = depth(node.right)
        max_diameter = max(max_diameter, left + right)
        return 1 + max(left, right)

    depth(root)
    return max_diameter


@pytest.mark.parametrize(
    "root, expected",
    [
        (TreeNode.from_array([1, 2, 3, 4, 5]), 3),
        (
            TreeNode.from_array(
                [
                    4,
                    -7,
                    -3,
                    None,
                    None,
                    -9,
                    -3,
                    9,
                    -7,
                    -4,
                    None,
                    6,
                    None,
                    -6,
                    -6,
                    None,
                    None,
                    0,
                    6,
                    5,
                    None,
                    9,
                    None,
                    None,
                    -1,
                    -4,
                    None,
                    None,
                    None,
                    -2,
                ]
            ),
            8,
        ),
    ],
)
def test_solution(root, expected):
    assert diameterOfBinaryTree(root) == expected

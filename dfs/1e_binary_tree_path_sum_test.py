"""
Binary Tree Path Sum (easy)

Given a binary tree and a number ‘S’, find if the tree has a path from root-to-leaf
such that the sum of all the node values of that path equals ‘S’.
"""


from typing import Optional

import pytest


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path_grokking(root, sum: int) -> bool:
    if root is None:
        return False

    # if the current node is a leaf and its value equals the sum, we've found a path
    if root.val == sum and root.left is None and root.right is None:
        return True

    # recursively call to traverse the left and right sub-tree
    # return true if any of the two recursive call return true
    return has_path_grokking(root.left, sum - root.val) or has_path_grokking(
        root.right, sum - root.val
    )


def has_path(root: Optional[TreeNode], sum: int) -> bool:
    if not root:
        return False
    stack = [(root, root.val)]
    while stack:
        curr, val = stack.pop()
        if not curr.left and not curr.right and val == sum:
            return True
        if curr.right:
            stack.append((curr.right, val + curr.right.val))
        if curr.left:
            stack.append((curr.left, val + curr.left.val))
    return False


@pytest.mark.parametrize(
    "root, sum, expected",
    [
        (
            TreeNode(
                1,
                left=TreeNode(
                    2,
                    left=TreeNode(4),
                    right=TreeNode(5),
                ),
                right=TreeNode(
                    3,
                    left=TreeNode(6),
                    right=TreeNode(7),
                ),
            ),
            10,
            True,
        ),
        (
            TreeNode(
                12,
                left=TreeNode(
                    7,
                    left=TreeNode(9),
                ),
                right=TreeNode(
                    1,
                    left=TreeNode(10),
                    right=TreeNode(5),
                ),
            ),
            16,
            False,
        ),
    ],
)
def test_has_path(root, sum, expected):
    assert has_path(root, sum) == expected
    assert has_path_grokking(root, sum) == expected

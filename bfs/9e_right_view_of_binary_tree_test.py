"""
Right View of a Binary Tree (easy)

Given a binary tree, return an array containing nodes in its right view.
The right view of a binary tree is the set of nodes visible when the tree is seen
from the right side.
"""


from collections import deque
from typing import Optional

import pytest


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# my code
def tree_right_view_custom(root: Optional[TreeNode]) -> list[int]:
    ans = []
    if not root:
        return ans

    queue = deque([root])
    while queue:
        lvl_size = len(queue)
        for i in range(lvl_size):
            curr = queue.popleft()
            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)
            if i + 1 == lvl_size:
                ans.append(curr.val)

    return ans


def tree_right_view(root: Optional[TreeNode]):
    ans = []
    if not root:
        return ans

    queue = deque([root])
    while queue:
        curr: Optional[TreeNode] = None
        for _ in range(len(queue)):
            curr = queue.popleft()
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        if curr:
            ans.append(curr.val)
    return ans


@pytest.mark.parametrize(
    "root, expected",
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
            [1, 3, 7],
        ),
        (
            TreeNode(
                12,
                left=TreeNode(
                    7,
                    left=TreeNode(9, left=TreeNode(3)),
                ),
                right=TreeNode(
                    1,
                    left=TreeNode(10),
                    right=TreeNode(5),
                ),
            ),
            [12, 1, 5, 3],
        ),
    ],
)
def test_tree_right_view(root, expected):
    assert tree_right_view_custom(root) == expected
    assert tree_right_view(root) == expected

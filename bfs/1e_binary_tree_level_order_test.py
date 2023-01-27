"""
Binary Tree Level Order Traversal (easy)

Given a binary tree, populate an array to represent its level-by-level
traversal. You should populate the values of all nodes of each level from
left to right in separate sub-arrays.
"""


from collections import deque

import pytest


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traverse(root: TreeNode):
    ans = []

    if root is None:
        return ans

    queue: deque[TreeNode] = deque()
    queue.append(root)

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

        ans.append(lvl_values)

    return ans


@pytest.mark.parametrize(
    "root, expected",
    [
        (
            TreeNode(
                12,
                left=TreeNode(7, left=TreeNode(9)),
                right=TreeNode(1, left=TreeNode(10), right=TreeNode(5)),
            ),
            [[12], [7, 1], [9, 10, 5]],
        ),
    ],
)
def test_traverse(root, expected):
    assert traverse(root) == expected

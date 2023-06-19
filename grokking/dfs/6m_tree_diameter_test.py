"""
Tree Diameter (medium)

Given a binary tree, find the length of its diameter. The diameter of a tree is the
number of nodes on the longest path between any two leaf nodes. The diameter of a tree
may or may not pass through the root.

Note: You can always assume that there are at least two leaf nodes in the given tree.
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


# def find_diameter(root: Optional[TreeNode]) -> int:
#     ans = 0
#     if not root:
#         return ans
#     stack: list[tuple[TreeNode, int]] = [(root, 1)]
#     while stack:
#         curr, path_nodes = stack.pop()
#         if not curr.left and not curr.right:
#             ans = max(ans, path_nodes)
#         if curr.left:
#             stack.append((curr.left, path_nodes + 1))
#         if curr.right:
#             stack.append((curr.right, path_nodes + 1))
#     return ans


class TreeDiameter:
    def __init__(self) -> None:
        self.diameter = 0

    def find_diameter(self, root: Optional[TreeNode]):
        self._calculate_depth(root)
        return self.diameter

    def _calculate_depth(self, curr: Optional[TreeNode]):
        if not curr:
            return 0

        left_tree_depth = self._calculate_depth(curr.left)
        right_tree_depth = self._calculate_depth(curr.right)

        curr_diameter = left_tree_depth + right_tree_depth + 1
        self.diameter = max(self.diameter, curr_diameter)

        return max(left_tree_depth, right_tree_depth) + 1


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
            5,
        ),
        (
            TreeNode(
                1,
                left=TreeNode(
                    2,
                ),
                right=TreeNode(
                    3,
                    left=TreeNode(
                        5,
                        left=TreeNode(7),
                        right=TreeNode(
                            8,
                            left=TreeNode(10),
                        ),
                    ),
                    right=TreeNode(
                        6,
                        left=TreeNode(
                            9,
                            left=TreeNode(11),
                        ),
                    ),
                ),
            ),
            7,
        ),
    ],
)
def test_grokking(root, expected):
    assert TreeDiameter().find_diameter(root) == expected

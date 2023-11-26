from typing import Optional

import pytest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     if not root or (not root.left and not root.right):
    #         return True

    #     return self.isValidBST(root.left) and self.isValidBST(root.right)

    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     queue = [root]
    #     root_val = root.val
    #     while queue:
    #         node = queue.pop()
    #         if node.left:
    #             if node.left.val >= node.val or node.left.val >= root_val:
    #                 return False
    #             queue.append(node.left)
    #         if node.right:
    #             if node.right.val <= node.val or node.right.val <= root_val:
    #                 return False
    #             queue.append(node.right)
    #     return True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False
            return valid(node.left, left, node.val) and valid(
                node.right, node.val, right
            )

        return valid(root, float("-inf"), float("inf"))


@pytest.mark.parametrize(
    "root, expected",
    [
        # (
        #     TreeNode(2, TreeNode(1), TreeNode(3)),
        #     True,
        # ),
        (
            TreeNode(5, TreeNode(4, None, None), TreeNode(6, TreeNode(3), TreeNode(7))),
            False,
        ),
    ],
)
def test_solution(root, expected):
    assert Solution().isValidBST(root) == expected

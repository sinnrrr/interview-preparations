import pytest
from typing import Optional


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


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root: Optional[TreeNode]):
            if not root:
                return 0
            left_height, right_height = height(root.left), height(root.right)
            if (
                left_height < 0
                or right_height < 0
                or abs(left_height - right_height) > 1
            ):
                return -1
            return 1 + max(left_height, right_height)

        return height(root) >= 0


@pytest.mark.parametrize(
    "root, expected",
    [
        (TreeNode.from_array([1, None, 2, None, 3]), False),
    ],
)
def test_is_balanced(root, expected):
    assert Solution().isBalanced(root) == expected

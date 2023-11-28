from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float("-inf")

        def dfs(curr: Optional[TreeNode]):
            if not curr:
                return 0
            nonlocal ans
            left_sum = dfs(curr.left)
            right_sum = dfs(curr.right)
            ans = max(ans, left_sum + right_sum + curr.val)
            return max(max(left_sum, right_sum) + curr.val, 0)

        dfs(root)
        return ans

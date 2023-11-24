from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepthDfsRecursive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(
            self.maxDepthDfsRecursive(root.left), self.maxDepthDfsRecursive(root.right)
        )

    def maxDepthBfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        level = 0
        queue = deque([root])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return level

    def maxDepthDfsIterative(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [[root, 1]]
        max_depth = 0
        while stack:
            node, curr_depth = stack.pop()
            max_depth = max(max_depth, curr_depth)
            if node.right:
                stack.append([node.right, curr_depth + 1])
            if node.left:
                stack.append([node.left, curr_depth + 1])
        return max_depth

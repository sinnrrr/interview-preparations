from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        ans = []
        if not root:
            return ans
        queue = deque([root])
        while queue:
            level = []
            new_nodes = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    new_nodes.append(node.left)
                if node.right:
                    new_nodes.append(node.right)
                level.append(node.val)
            ans.append(level)
            queue = deque(new_nodes)
        return ans

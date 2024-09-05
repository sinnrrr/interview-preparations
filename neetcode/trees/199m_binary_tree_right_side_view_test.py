import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideViewWrong(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def traverse(root):
            nonlocal res

            if not root:
                return

            res.append(root.val)

            if not root.right:
                traverse(root.left)
            else:
                traverse(root.right)

        traverse(root)
        return res

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def bfs(root):
            nonlocal res

            if not root:
                return

            queue = [root]
            while queue:
                res.append(queue[-1].val)

                level = collections.deque(queue.copy())
                queue.clear()

                while level:
                    node = level.popleft()
                    if node.left:
                        queue.append(node.left)

                    if node.right:
                        queue.append(node.right)

        bfs(root)
        return res

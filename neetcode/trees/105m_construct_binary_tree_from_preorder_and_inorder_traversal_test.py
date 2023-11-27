from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        return root

    def buildTreeOptimized(
        self, preorder: list[int], inorder: list[int]
    ) -> Optional[TreeNode]:
        def rec(l, r):
            if l > r:
                return

            root = TreeNode(preorder.pop(0))
            mid = inorder_idx[root.val]
            root.left = rec(l, mid - 1)
            root.right = rec(mid + 1, r)
            return root

        inorder_idx = {v: i for i, v in enumerate(inorder)}
        return rec(0, len(inorder) - 1)

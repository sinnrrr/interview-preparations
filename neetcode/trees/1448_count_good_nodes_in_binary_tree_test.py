class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 0

        def traverse(root, max_val):
            nonlocal good_nodes

            if root.val >= max_val:
                max_val = root.val
                good_nodes += 1

            if root.left:
                traverse(root.left, max_val)
            if root.right:
                traverse(root.right, max_val)

        traverse(root, root.val)
        return good_nodes

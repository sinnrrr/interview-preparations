# Definition for a binary tree node.
import collections
from typing import Any, Optional


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


class Codec:
    NULL_VAL = "N"
    DELIMITER = ","

    def serialize(self, root: Optional[TreeNode]):
        res = []

        def dfs(node):
            if not node:
                res.append(self.NULL_VAL)
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    def deserialize(self, data: str):
        vals = data.split(self.DELIMITER)
        self.i = 0

        def dfs():
            if vals[self.i] == self.NULL_VAL:
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

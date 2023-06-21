class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Node | None) -> Node | None:
        if not node:
            return node

        processed: dict[int, Node] = {}

        def dfs(node: Node):
            if node.val in processed.keys():
                return processed[node.val]
            neighbors = node.neighbors
            node = Node(
                node.val, [None] * len(neighbors)
            )  # this will force to create new node
            processed[node.val] = node
            for idx, neighbor in enumerate(neighbors):
                node.neighbors[idx] = dfs(neighbor)
            return node

        return dfs(node)


def test_solution():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.neighbors = [node2, node4]
    node2.neighbors = [node3, node1]
    node3.neighbors = [node4, node2]
    node4.neighbors = [node1, node3]

    Solution().cloneGraph(node1)

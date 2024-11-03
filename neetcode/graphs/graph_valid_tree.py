from collections import defaultdict


class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        adj_map = defaultdict(list)
        for edge in edges:
            adj_map[edge[0]].append(edge[1])
            adj_map[edge[1]].append(edge[0])

        visited = set()

        def dfs(curr: int, prev: int):
            if curr in visited:
                return False

            visited.add(curr)
            for node in adj_map[curr]:
                if node == prev:
                    continue
                if not dfs(node, curr):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n

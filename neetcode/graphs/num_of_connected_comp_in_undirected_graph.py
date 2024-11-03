from collections import defaultdict


class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        adj_map = defaultdict(list)
        for edge in edges:
            adj_map[edge[0]].append(edge[1])
            adj_map[edge[1]].append(edge[0])
        print(adj_map)

        res, visited = 0, set()

        def dfs(curr: int):
            if curr in visited:
                return

            visited.add(curr)
            for node in adj_map[curr]:
                dfs(node)

        for i in range(n):
            if i not in visited:
                print(visited)
                res += 1
                dfs(i)

        return res

from typing import List


class Solution:
    def maxAreaOfIslandWrong(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        i, total_elements = 0, m * n
        max_island_area = 0

        curr_area = 0

        def discover_island(row, col):
            nonlocal curr_area
            is_island = grid[row][col]
            if not is_island:
                return
            curr_area += 1

            discover_island(row + 1, col)
            discover_island(row - 1, col)
            discover_island(row, col + 1)
            discover_island(row, col - 1)

        while i < total_elements:
            row, col = divmod(i, total_elements)

            discover_island(row, col)
            max_island_area = max(max_island_area, curr_area)

            i += 1

        return max_island_area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(row, col):
            if (
                row < 0
                or row == rows
                or col < 0
                or col == cols
                or grid[row][col] == 0
                or (row, col) in visited
            ):
                return 0

            visited.add((row, col))
            return (
                1
                + dfs(row + 1, col)
                + dfs(row - 1, col)
                + dfs(row, col + 1)
                + dfs(row, col - 1)
            )

        area = 0
        for row in range(rows):
            for col in range(cols):
                area = max(area, dfs(row, col))
        return area


def test():
    assert (
        Solution().maxAreaOfIslandWrong(
            [
                [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            ]
        )
        == 6
    )

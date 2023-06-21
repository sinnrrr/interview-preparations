import collections

import pytest


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        islands = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def bfs(r: int, c: int):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (
                        r >= 0
                        and c >= 0
                        and r < rows
                        and c < cols
                        and grid[r][c] == "1"
                        and (r, c) not in visited
                    ):
                        q.append((r, c))
                        visited.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands


@pytest.mark.parametrize(
    "grid, expected",
    [
        (
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ],
            1,
        ),
        (
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ],
            3,
        ),
    ],
)
def test_solution(grid, expected):
    assert Solution().numIslands(grid) == expected

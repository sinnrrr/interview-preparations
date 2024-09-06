class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        rows, cols = len(grid), len(grid[0])

        def fill_cells(row, col, distance=0):
            if (
                row < 0
                or row == rows
                or col < 0
                or col == cols
                or grid[row][col] == -1
                or grid[row][col] < distance
            ):
                return

            if grid[row][col] != 0:
                grid[row][col] = distance

            fill_cells(row + 1, col, distance + 1)
            fill_cells(row - 1, col, distance + 1)
            fill_cells(row, col + 1, distance + 1)
            fill_cells(row, col - 1, distance + 1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    fill_cells(row, col)


def test():
    grid = [
        [2147483647, -1, 0, 2147483647],
        [2147483647, 2147483647, 2147483647, -1],
        [2147483647, -1, 2147483647, -1],
        [0, -1, 2147483647, 2147483647],
    ]

    Solution().islandsAndTreasure(grid)
    assert grid == [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]

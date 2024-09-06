from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        time, fresh = 0, 0
        rotten = deque()

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    rotten.append((row, col))

        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while rotten and fresh > 0:
            for _ in range(len(rotten)):
                row, col = rotten.popleft()

                for delta_row, delta_col in DIRECTIONS:
                    drow, dcol = row + delta_row, col + delta_col
                    if (
                        drow < 0
                        or drow == ROWS
                        or dcol < 0
                        or dcol == COLS
                        or grid[drow][dcol] != 1
                    ):
                        continue

                    grid[drow][dcol] = 2
                    rotten.append((drow, dcol))
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1


def test():
    assert Solution().orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4

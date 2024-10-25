from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [defaultdict(int) for _ in range(9)]
        cols = [defaultdict(int) for _ in range(9)]
        boxes = [[defaultdict(int) for _ in range(3)] for _ in range(3)]

        for i in range(9 * 9):
            row, col = divmod(i, 9)
            curr_numstr = board[row][col]
            if curr_numstr == ".":
                continue
            curr_num = int(curr_numstr)

            if curr_num < 1 or curr_num > 9:
                return False

            rows[row][curr_num] += 1
            if rows[row][curr_num] > 1:
                return False

            cols[col][curr_num] += 1
            if cols[col][curr_num] > 1:
                return False

            box_row, box_col = row // 3, col // 3
            boxes[box_row][box_col][curr_num] += 1
            if boxes[box_row][box_col][curr_num] > 1:
                return False

        return True


def test():
    assert (
        Solution().isValidSudoku(
            [
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ]
        )
        is True
    )

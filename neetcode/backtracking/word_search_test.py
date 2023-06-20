import pytest


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(row, col, i):
            if i == len(word):
                return True
            if (
                row < 0
                or col < 0
                or row >= ROWS
                or col >= COLS
                or word[i] != board[row][col]
                or (row, col) in path
            ):
                return False

            path.add((row, col))
            res = (
                dfs(row + 1, col, i + 1)
                or dfs(row, col + 1, i + 1)
                or dfs(row - 1, col, i + 1)
                or dfs(row, col - 1, i + 1)
            )
            path.remove((row, col))
            return res

        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col, 0):
                    return True

        return False


# class Solution:
#     def exist(self, board: list[list[str]], word: str) -> bool:
#         res = False
#         x_len, y_len = len(board), len(board[0])

#         def dfs(i: int, path: list[tuple[int, int]], curr: str):
#             nonlocal res
#             if res:
#                 return
#             if curr == word:
#                 res = True
#                 return

#             x, y = path[-1][0], path[-1][1]
#             if board[y][x] == word[i]:
#                 curr += word[i]
#             else:
#                 path.pop()
#                 # if not path:
#                 #     if x == x_len - 1:
#                 #         path.append((0, y + 1))
#                 #     else:
#                 #         path.append((x + 1, y))

#                 #     dfs(i + 1, path, curr)
#                 return

#             # left
#             if x > 0 and not (x - 1, y) in path:
#                 path.append((x - 1, y))
#                 dfs(i + 1, path, curr)

#             # top
#             if y > 0 and not (x, y - 1) in path:
#                 path.append((x, y - 1))
#                 dfs(i + 1, path, curr)

#             # right
#             if x < x_len - 1 and not (x + 1, y) in path:
#                 path.append((x + 1, y))
#                 dfs(i + 1, path, curr)

#             # bottom
#             if y < y_len - 1 and not (x, y + 1) in path:
#                 path.append((x, y + 1))
#                 dfs(i + 1, path, curr)

#         dfs(0, [(0, 0)], "")
#         return res


@pytest.mark.parametrize(
    "board, word, expected",
    [
        (
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "ABCCED",
            True,
        ),
        (
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "SEE",
            True,
        ),
        (
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "ABCB",
            False,
        ),
    ],
)
def test_solution(board, word, expected):
    assert Solution().exist(board, word) == expected

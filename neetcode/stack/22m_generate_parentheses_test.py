class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        open = close = n
        res = []

        def dfs(curr_str: str, open: int, close: int):
            nonlocal res
            if open == 0 and close == 0:
                res.append(curr_str)
                return

            if close > open and close > 0:
                dfs(curr_str + ")", open, close - 1)

            if open > 0:
                dfs(curr_str + "(", open - 1, close)

        dfs("", open, close)

        return res


def test():
    assert Solution().generateParenthesis(3) == [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()",
    ]

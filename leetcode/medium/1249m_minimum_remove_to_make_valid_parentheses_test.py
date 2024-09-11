class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_count = 0
        res = []

        for char in s:
            if char == "(":
                open_count += 1
                res.append(char)
            elif char == ")" and open_count > 0:
                open_count -= 1
                res.append(char)
            elif char != ")":
                res.append(char)

        filtered = []
        for char in res[::-1]:
            if char == "(" and open_count > 0:
                open_count -= 1
            else:
                filtered.append(char)

        return "".join(filtered[::-1])


def test():
    assert Solution().minRemoveToMakeValid("))((") == ""

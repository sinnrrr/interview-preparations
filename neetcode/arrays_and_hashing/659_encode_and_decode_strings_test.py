import pytest


class Solution:
    def encode(self, strs):
        ans = ""
        for s in strs:
            ans += f"{len(s)}#{s}"
        return ans

    def decode(self, s):
        ans = []
        curr, n = 0, len(s)
        while n > curr:
            step = int(s[curr])
            ans.append(s[curr + 2 : curr + step + 2])
            curr += step + 2
        return ans


@pytest.mark.parametrize(
    "strs",
    [
        ["lint", "code", "love", "you"],
        ["we", "say", ":", "yes"],
    ],
)
def test_solution(strs):
    encoded_str = Solution().encode(strs)
    decoded_strs = Solution().decode(encoded_str)
    assert decoded_strs == strs

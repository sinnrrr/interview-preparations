import pytest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n, start, end = len(s), 0, 0
        window_chars = set()
        longest = 0
        while n > end:
            if s[end] in window_chars:
                window_chars.remove(s[start])
                start += 1
                continue
            window_chars.add(s[end])
            longest = max(longest, len(window_chars))
            end += 1
        return longest


@pytest.mark.parametrize(
    "s, expected",
    [
        ("qrsvbspk", 5),
    ],
)
def test_solution(s, expected):
    assert Solution().lengthOfLongestSubstring(s) == expected

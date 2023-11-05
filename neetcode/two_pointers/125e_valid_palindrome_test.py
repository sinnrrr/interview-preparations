import pytest


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        s = s.lower()
        l, r = 0, len(s) - 1
        while l <= r:
            are_equal = s[l] == s[r]
            if s[l].isalnum() and s[r].isalnum() and not are_equal:
                return False
            l += int(not s[l].isalnum() or are_equal)
            r -= int(not s[r].isalnum() or are_equal)
        return True


@pytest.mark.parametrize(
    "s, expected",
    [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        (".", True),
        (".,", True),
    ],
)
def test_solution(s, expected):
    assert Solution().isPalindrome(s) == expected

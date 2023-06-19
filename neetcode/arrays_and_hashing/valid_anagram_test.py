import pytest


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        chars = {}
        for char in s:
            chars[char] = 1 + chars.get(char, 0)

        for char in t:
            if not chars.get(char):
                return False
            chars[char] -= 1

        for char_count in chars.values():
            if char_count != 0:
                return False

        return True


@pytest.mark.parametrize(
    "s, k, expected",
    [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
    ],
)
def test_solution(s, k, expected):
    assert Solution().isAnagram(s, k) == expected

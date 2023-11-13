from collections import defaultdict

import pytest


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hmap = defaultdict(list[str])
        a_ord = ord("a")
        for s1 in strs:
            fingerprint = [0] * 26
            for char in s1:
                fingerprint[ord(char) - a_ord] += 1
            hmap[tuple(fingerprint)].append(s1)
        return hmap.values()


@pytest.mark.parametrize(
    "strs, expected",
    [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        ),
        ([""], [[""]]),
        (["a"], [["a"]]),
    ],
)
def test_solution(strs, expected):
    assert Solution().groupAnagrams(strs) == expected

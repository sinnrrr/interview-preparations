from collections import defaultdict

import pytest


class Solution:
    # def characterReplacement(self, s: str, k: int) -> int:
    #     ans = 0
    #     chars_replaced, curr_char, start = set(), s[0], 0
    #     for end in range(len(s)):
    #         if s[end] == curr_char:
    #             continue
    #         if k > 0:
    #             chars_replaced.add(end)
    #             k -= 1
    #         else:
    #             pass
    #         ans = max(ans, end - start + 1)
    #     return ans

    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        start = 0
        char_freq, most_freq = defaultdict(int), 0
        for end in range(len(s)):
            char_freq[s[end]] += 1
            most_freq = max(most_freq, char_freq[s[end]])
            while (end - start + 1) - most_freq > k:
                char_freq[s[start]] -= 1
                start += 1
            ans = max(ans, end - start + 1)
        return ans


@pytest.mark.parametrize(
    "s, k, expected",
    [
        ("ABAB", 2, 4),
        ("AABABBA", 1, 4),
    ],
)
def test_solution(s, k, expected):
    assert Solution().characterReplacement(s, k) == expected

import math

import pytest


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        chars_hmap = {}
        for char in t:
            chars_hmap[char] = chars_hmap.get(char, 0) + 1

        start = 0
        min_window, min_res = math.inf, ""
        have, need = 0, len(chars_hmap.keys())
        for end in range(len(s)):
            end_char_occ = chars_hmap.get(s[end])
            if end_char_occ is not None:
                chars_hmap[s[end]] -= 1
                if chars_hmap[s[end]] == 0:
                    have += 1
            while need == have:
                window_size = end - start + 1
                if window_size < min_window:
                    min_window = window_size
                    min_res = s[start : end + 1]
                start_char_occ = chars_hmap.get(s[start])
                if start_char_occ is not None:
                    new_occ = start_char_occ + 1
                    chars_hmap[s[start]] = new_occ
                    if new_occ > 0:
                        have -= 1
                start += 1
        return min_res

    def minWindowNeetcode(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""


@pytest.mark.parametrize(
    "s, t, expected",
    [
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("a", "aa", ""),
        ("a", "b", ""),
        ("bba", "ab", "ba"),
        ("cabwefgewcwaefgcf", "cae", "cwae"),
    ],
)
def test_solution(s, t, expected):
    assert Solution().minWindow(s, t) == expected
    assert Solution().minWindowNeetcode(s, t) == expected

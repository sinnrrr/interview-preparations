"""
Given a string and a pattern, find the smallest substring in the given string
which has all the character occurrences of the given pattern.
"""

import pytest


def find_substring(str1: str, pattern: str):
    window_start, matched, substr_start = 0, 0, 0
    pattern_char_freq_map = {}
    min_len = len(str1) + 1

    for pattern_char in pattern:
        if pattern_char not in pattern_char_freq_map:
            pattern_char_freq_map[pattern_char] = 0
        pattern_char_freq_map[pattern_char] += 1

    for window_end in range(len(str1)):
        right_char = str1[window_end]

        if right_char in pattern_char_freq_map:
            pattern_char_freq_map[right_char] -= 1
            if pattern_char_freq_map[right_char] >= 0:
                matched += 1

        while matched == len(pattern):
            if min_len > window_end - window_start + 1:
                min_len = window_end - window_start + 1
                substr_start = window_start

            left_char = str1[window_start]
            window_start += 1
            if left_char in pattern_char_freq_map:
                if pattern_char_freq_map[left_char] == 0:
                    matched -= 1
                pattern_char_freq_map[left_char] += 1

    if min_len > len(str1):
        return ""

    return str1[substr_start:substr_start + min_len]


@pytest.mark.parametrize(
    "str1, pattern, expected",
    [("aabdec", "abc", "abdec"), ("aabdec", "abac", "aabdec"),
     ("abdbca", "abc", "bca"), ("adcad", "abc", "")],
)
def test_find_substring(str1, pattern, expected):
    assert find_substring(str1, pattern) == expected

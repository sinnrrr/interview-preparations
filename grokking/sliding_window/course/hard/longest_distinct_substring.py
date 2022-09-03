"""
Given a string, find the length of the longest substring, which
has all distinct characters.
"""

import pytest


def non_repeat_substring(str):
    window_start, max_distinct_substring = 0, 0
    char_pos_map = {}

    for window_end in range(len(str)):
        right_char = str[window_end]

        if right_char in char_pos_map:
            window_start = max(window_start, char_pos_map[right_char] + 1)

        char_pos_map[right_char] = window_end
        max_distinct_substring = max(max_distinct_substring,
                                     window_end - window_start + 1)

    return max_distinct_substring


@pytest.mark.parametrize(
    "str, expected",
    [("aabccbb", 3), ("abbbb", 2), ("abccde", 3)],
)
def test_non_repeat_substring(str, expected):
    assert non_repeat_substring(str) == expected

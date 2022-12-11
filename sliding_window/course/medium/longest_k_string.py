"""
Given a string, find the length of the longest substring
in it with no more than K distinct characters.
"""

from collections import defaultdict

import pytest


def longest_substring_with_k_distinct(str, k):
    window_start, max_length = 0, 0
    char_freq_map = defaultdict(int)

    for window_end in range(len(str)):
        right_char = str[window_end]
        char_freq_map[right_char] += 1

        while len(char_freq_map) > k:
            left_char = str[window_start]
            char_freq_map[left_char] -= 1

            if char_freq_map[left_char] == 0:
                del char_freq_map[left_char]

            # here we go to the next char
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length


@pytest.mark.parametrize(
    "str, k, expected",
    [("araaci", 2, 4), ("araaci", 1, 2), ("cbbebi", 3, 5), ("cbbebi", 10, 6)],
)
def test_longest_substring_with_k_distinct(str, k, expected):
    assert longest_substring_with_k_distinct(str, k) == expected

"""
Given a string and a pattern, find out if the string contains
any permutation of the pattern.

Permutation is defined as the re-arranging of the characters
of the string. For example, “abc” has the following six permutations:
- abc
- acb
- bac
- bca
- cab
- cba

If a string has ‘n’ distinct characters, it will have n! permutations.
"""

import pytest

# def find_permutation(str1: str, pattern: str) -> bool:
#     window_start, max_window_len = 0, 0

#     for window_end in range(len(str1)):
#         right_char = str1[window_end]

#         if right_char in pattern:
#             window_start = window_end

#         max_window_len = max(max_window_len, window_end - window_start + 1)

#     return len(pattern) == max_window_len


def find_permutation(str1: str, pattern: str) -> bool:
    window_start = 0
    pattern_chars_matched = 0
    pattern_char_freq_map = {}

    for pattern_char in pattern:
        if pattern_char not in pattern_char_freq_map:
            pattern_char_freq_map[pattern_char] = 0
        pattern_char_freq_map[pattern_char] += 1

    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in pattern_char_freq_map:
            pattern_char_freq_map[right_char] -= 1
            if pattern_char_freq_map[right_char] == 0:
                pattern_chars_matched += 1

        if pattern_chars_matched == len(pattern_char_freq_map):
            return True

        if window_end >= len(pattern) - 1:
            left_char = str1[window_start]
            window_start += 1
            if left_char in pattern_char_freq_map:
                if pattern_char_freq_map[left_char] == 0:
                    pattern_chars_matched -= 1  # because we moved the window
                pattern_char_freq_map[
                    left_char] += 1  # because we moved the window

    return False


@pytest.mark.parametrize(
    "str1, pattern, expected",
    [("oidbcaf", "abc", True), ("odicf", "dc", False),
     ("bcdxabcdy", "bcdyabcdx", True), ("aaacb", "abc", True)],
)
def test_find_permutation(str1: str, pattern: str, expected: bool):
    assert find_permutation(str1, pattern) == expected

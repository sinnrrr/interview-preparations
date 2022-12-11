"""
Given a string and a pattern, find all anagrams of the pattern in the given
string.

Every anagram is a permutation of a string. As we know, when we are not
allowed to repeat characters while finding permutations of a string, we get N!
permutations (or anagrams) of a string having N characters.

For example, here are the six anagrams of the string “abc”:
abc
acb
bac
bca
cab
cba

Write a function to return a list of starting indices of the anagrams
of the pattern in the given string.
"""

import pytest


def find_string_anagrams(str1: str, pattern: str) -> list[int]:
    pattern_char_freq_map = {
    }  # we meed this to track how many chars have been matched already
    window_start = 0
    matched = 0  # needed to track if all of pattern characters was matched
    result_indices = []

    for pattern_char in pattern:
        if pattern_char not in pattern_char_freq_map:
            pattern_char_freq_map[pattern_char] = 0
        pattern_char_freq_map[pattern_char] += 1

    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in pattern_char_freq_map:
            pattern_char_freq_map[right_char] -= 1
            if pattern_char_freq_map[right_char] == 0:
                matched += 1

        if matched == len(pattern_char_freq_map):
            result_indices.append(window_start)

        if window_end >= len(pattern) - 1:
            left_char = str1[window_start]
            window_start += 1
            if left_char in pattern_char_freq_map:
                if pattern_char_freq_map[left_char] == 0:
                    matched -= 1
                pattern_char_freq_map[left_char] += 1

    return result_indices


@pytest.mark.parametrize(
    "str1, pattern, expected",
    [("ppqp", "pq", [1, 2]), ("abbcabc", "abc", [2, 3, 4])],
)
def test_find_string_anagrams(str1, pattern, expected):
    assert find_string_anagrams(str1, pattern) == expected

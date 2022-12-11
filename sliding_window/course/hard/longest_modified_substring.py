"""
Given a string with lowercase letters only, if you are allowed to
replace no more than k letters with any letter, find
the length of the longest substring having the same letters after replacement.
"""

from collections import defaultdict

import pytest

# def length_of_longest_substring(str, k):
#     window_start, longest_substring = 0, 0
#     char_freq_map = defaultdict(int)

#     for window_end in range(len(str)):
#         right_char = str[window_end]
#         char_freq_map[right_char] += 1

#         left_char = str[window_start]
#         left_char_freq = char_freq_map[left_char]

#         # if window_end is on after k's char and it is not equal to origin char
#         if window_end == window_start + left_char_freq + k and left_char != right_char:
#             window_start = window_start + left_char_freq

#         longest_substring = max(longest_substring,
#                                 window_end - window_start + 1)

#     return longest_substring


def length_of_longest_substring(str1: str, k: int):
    window_start, max_repeated_letters, max_length = 0, 0, 0
    char_freq_map = defaultdict(int)

    for window_end in range(len(str1)):
        right_char = str1[window_end]
        char_freq_map[right_char] += 1

        max_repeated_letters = max(max_repeated_letters,
                                   char_freq_map[right_char])

        if window_end - window_start + 1 > k + max_repeated_letters:
            left_char = str1[window_start]
            char_freq_map[left_char] -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length


@pytest.mark.parametrize(
    "str, k, expected",
    [("aabccbb", 2, 5), ("abbcb", 1, 4), ("abccde", 1, 3), ("bbcba", 2, 5)],
)
def test_length_of_longest_substring(str, k, expected):
    assert length_of_longest_substring(str, k) == expected

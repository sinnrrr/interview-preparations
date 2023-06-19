"""
Given an array containing 0s and 1s, if you are allowed to replace no more
than ‘k’ 0s with 1s, find the length of the longest contiguous subarray
having all 1s.
"""

import pytest


def length_of_longest_substring(arr: list, k: int):
    window_start, one_number_count = 0, 0
    longest_one_number_subarray = 0

    for window_end in range(len(arr)):
        right_num = arr[window_end]
        one_number_count += right_num  # either 0 or 1

        if window_end - window_start + 1 > one_number_count + k:
            left_num = arr[window_start]
            one_number_count -= left_num  # either 0 or 1
            window_start += 1

        longest_one_number_subarray = max(longest_one_number_subarray,
                                          window_end - window_start + 1)

    return longest_one_number_subarray


@pytest.mark.parametrize(
    "arr, k, expected",
    [([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2, 6),
     ([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3, 9)],
)
def test_length_of_longest_substring(arr, k, expected):
    assert length_of_longest_substring(arr, k) == expected

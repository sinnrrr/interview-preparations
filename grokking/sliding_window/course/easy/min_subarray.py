"""
Given an array of positive integers and a number ‘S,’
find the length of the smallest contiguous subarray whose
sum is greater than or equal to ‘S’.

Return 0 if no such subarray exists.
"""

import math

import pytest


def min_subarray(nums, sum):
    window_start, window_sum, min_subarray_len = 0, 0, math.inf

    for window_end in range(len(nums)):
        window_sum += nums[window_end]

        # Making the window smallest possible for current iteration
        while window_sum >= sum:
            min_subarray_len = min(min_subarray_len,
                                   window_end - window_start + 1)
            window_sum -= nums[window_start]
            window_start += 1

    return 0 if min_subarray_len == math.inf else min_subarray_len


@pytest.mark.parametrize(
    "nums, sum, expected",
    [([2, 1, 5, 2, 3, 2], 7, 2), ([2, 1, 5, 2, 8], 7, 1),
     ([3, 4, 1, 1, 6], 8, 3)],
)
def test_min_subarray(nums, sum, expected):
    assert min_subarray(nums, sum) == expected

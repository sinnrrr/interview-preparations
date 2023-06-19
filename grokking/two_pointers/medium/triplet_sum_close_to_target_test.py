"""
Given an array of unsorted numbers and a target number, find a triplet
in the array whose sum is as close to the target number as possible,
return the sum of the triplet.

If there are more than one such triplet, return the sum of the triplet
with the smallest sum.
"""

import math

import pytest


def triplet_sum_close_to_target(arr: list[int], target_sum: int):
    arr.sort()

    n = len(arr)
    smallest_diff = math.inf

    for i in range(n - 2):
        left, right = i + 1, n - 1
        target_sum_comp = target_sum - arr[i]

        while left < right:
            target_diff = target_sum_comp - (arr[left] + arr[right])

            if abs(target_diff) == abs(smallest_diff):
                smallest_diff = max(smallest_diff, target_diff)
            elif abs(target_diff) < abs(smallest_diff):
                smallest_diff = target_diff

            if target_diff == 0:
                break

            if target_diff > 0:
                left += 1
            else:
                right -= 1

    return target_sum - smallest_diff


@pytest.mark.parametrize(
    "arr, target_sum, expected",
    [
        ([-2, 0, 1, 2], 2, 1),
        ([-3, -1, 1, 2], 1, 0),
        ([1, 0, 1, 1], 100, 3),
        ([0, 1, 2], 3, 3),
        ([-1, 2, 1, -4], 1, 2),
        ([0, 1, 2, 3, 10], 10, 11),
    ],
)
def test_triplet_sum_close_to_target(arr, target_sum, expected):
    assert triplet_sum_close_to_target(arr, target_sum) == expected

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
    arr = sorted(arr)
    n = len(arr)
    closest_to_target = math.inf

    for i in range(n):
        left, right = i + 1, n - 1

        while left < right:
            sum = arr[left] + arr[right] + arr[i]

            sum_diff = abs(target_sum - sum)
            closest_to_target_diff = abs(target_sum - closest_to_target)

            if sum_diff < closest_to_target_diff:
                closest_to_target = sum

            if sum == target_sum:
                break

            if sum > target_sum:
                right -= 1

            if sum < target_sum:
                left += 1

    return closest_to_target


@pytest.mark.parametrize(
    "arr, target_sum, expected",
    [
        ([-2, 0, 1, 2], 2, 1),
        ([-3, -1, 1, 2], 1, 0),
        ([1, 0, 1, 1], 100, 3),
        ([0, 1, 2], 3, 3),
    ],
)
def test_triplet_sum_close_to_target(arr, target_sum, expected):
    assert triplet_sum_close_to_target(arr, target_sum) == expected

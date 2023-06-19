"""
Given an array of sorted numbers and a target sum, find a pair in the array
whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair)
such that they add up to the given target.
"""

import pytest


def pair_with_targetsum(arr: list[int], target_sum: int):
    left, right = 0, len(arr) - 1

    while left <= right:
        sum = arr[left] + arr[right]

        if sum == target_sum:
            return [left, right]

        if sum > target_sum:
            right -= 1

        if sum < target_sum:
            left += 1

    return None


def pair_with_targetsum_2(arr: list[int], target_sum: int):
    nums = {}
    for i, num in enumerate(arr):
        if target_sum - num in nums:
            return [nums[target_sum - num], i]

        nums[arr[i]] = i

    return None


@pytest.mark.parametrize(
    "arr, target_sum, expected",
    [([1, 2, 3, 4, 6], 6, [1, 3]), ([2, 5, 9, 11], 11, [0, 2])],
)
def test_pair_with_targetsumpair_with_targetsum(arr, target_sum, expected):
    assert pair_with_targetsum(arr, target_sum) == expected
    assert pair_with_targetsum_2(arr, target_sum) == expected

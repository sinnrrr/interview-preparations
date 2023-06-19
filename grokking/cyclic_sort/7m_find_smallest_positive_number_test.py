"""
Find the Smallest Missing Positive Number (medium)
Problem Challenge 2

Given an unsorted array containing numbers, find the smallest missing positive
number in it.

Example 1
Input: [-3, 1, 5, 4, 2]
Output: 3
Explanation: The smallest missing positive number is '3'

Example 2
Input: [3, -2, 0, 1, 2]
Output: 4

Example 3
Input: [3, 2, 5, 1]
Output: 4
"""


import pytest


def find_first_missing_positive(nums: list[int]):
    i, n = 0, len(nums)

    while i < n:
        j = nums[i] - 1
        if 0 <= j < n and nums[i] != nums[j]:
            nums[j], nums[i] = nums[i], nums[j]
            continue

        i += 1

    for i in range(n):
        supposed = i + 1
        if nums[i] != supposed:
            return supposed

    return n + 1


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([-3, 1, 5, 4, 2], 3),
        ([3, -2, 0, 1, 2], 4),
        ([3, 2, 5, 1], 4),
    ],
)
def test_find_first_smallest_missing_positive(nums, expected):
    assert find_first_missing_positive(nums) == expected


@pytest.mark.parametrize(
    "nums, expected",
    [([1], 2), ([1, 1], 2)],
)
def test_leetcode(nums, expected):
    assert find_first_missing_positive(nums) == expected

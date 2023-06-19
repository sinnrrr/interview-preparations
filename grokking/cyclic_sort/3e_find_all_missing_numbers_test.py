"""
Problem Statement
We are given an unsorted array containing numbers taken from the
range 1 to ‘n’. The array can have duplicates, which means some numbers
will be missing. Find all those missing numbers.

Example 1
Input: [2, 3, 1, 8, 2, 3, 5, 1]
Output: 4, 6, 7
Explanation: The array should have all numbers from 1 to 8, due to
duplicates 4, 6, and 7 are missing.

Example 2
Input: [2, 4, 1, 2]
Output: 3

Example 3
Input: [2, 3, 2, 1]
Output: 4
"""


import pytest


def find_missing_numbers(nums: list[int]) -> list[int]:
    i, n = 0, len(nums)
    while i < n:
        j = nums[i] - 1

        if nums[j] != nums[i]:
            nums[j], nums[i] = nums[i], nums[j]
            continue

        i += 1

    res = []

    for i in range(n):
        if nums[i] - 1 != i:
            res.append(i + 1)

    return res


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([2, 3, 1, 8, 2, 3, 5, 1], [4, 6, 7]),
        ([2, 4, 1, 2], [3]),
        ([2, 3, 2, 1], [4]),
    ],
)
def test_find_missing_numbers(nums, expected):
    assert find_missing_numbers(nums) == expected

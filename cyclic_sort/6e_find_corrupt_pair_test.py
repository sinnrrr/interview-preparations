"""
Find the Corrupt Pair (easy)
Problem Challenge 1

We are given an unsorted array containing ‘n’ numbers taken from the
range 1 to ‘n’. The array originally contained all the numbers
from 1 to ‘n’, but due to a data error, one of the numbers got duplicated
which also resulted in one number going missing. Find both these numbers.

Example 1
Input: [3, 1, 2, 5, 2]
Output: [2, 4]
Explanation: '2' is duplicated and '4' is missing.

Example 2
Input: [3, 1, 2, 3, 6, 4]
Output: [3, 5]
Explanation: '3' is duplicated and '5' is missing.
"""


import pytest


def find_corrupt_numbers(nums: list[int]) -> list[int]:
    i, n = 0, len(nums)
    while i < n:
        j = nums[i] - 1
        if nums[j] != nums[i]:
            nums[j], nums[i] = nums[i], nums[j]
            continue

        i += 1

    for i in range(n):
        num = i + 1
        if nums[i] != num:
            return [nums[i], num]

    return []


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([3, 1, 2, 5, 2], [2, 4]),
        ([3, 1, 2, 3, 6, 4], [3, 5]),
    ],
)
def test_grokking(nums, expected):
    assert find_corrupt_numbers(nums) == expected

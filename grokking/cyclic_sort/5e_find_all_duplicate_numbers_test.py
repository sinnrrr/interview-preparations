"""
Problem Statement
We are given an unsorted array containing ‘n’ numbers taken from the
range 1 to ‘n’. The array has some duplicates, find all the duplicate
numbers without using any extra space.

Example 1
Input: [3, 4, 4, 5, 5]
Output: [4, 5]

Example 2
Input: [5, 4, 7, 2, 3, 5, 3]
Output: [3, 5]
"""


import pytest


def find_all_duplicates(nums: list[int]) -> list[int]:
    i, n = 0, len(nums)
    while i < n:
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    duplicates = []
    for i in range(n):
        if nums[i] - 1 != i:
            duplicates.append(nums[i])

    return duplicates


# my solution for simmilar leetcode problem
def find_all_duplicates_custom(nums: list[int]) -> list[int]:
    i, n = 0, len(nums)
    res = set()
    while i < n:
        j = nums[i] - 1

        if nums[j] != nums[i]:
            nums[j], nums[i] = nums[i], nums[j]
            continue
        elif i != j:
            res.add(nums[i])

        i += 1

    return list(res)


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([3, 4, 4, 5, 5], [4, 5]),
        ([5, 4, 7, 2, 3, 5, 3], [3, 5]),
    ],
)
def test_grokking(nums, expected):
    assert find_all_duplicates_custom(nums) == expected


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([3, 4, 4, 5, 5], [5, 4]),
        ([5, 4, 7, 2, 3, 5, 3], [3, 5]),
    ],
)
def test_custom(nums, expected):
    assert find_all_duplicates(nums) == expected

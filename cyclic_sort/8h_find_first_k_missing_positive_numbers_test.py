"""
Find the First K Missing Positive Numbers (hard)

Given an unsorted array containing numbers and a number ‘k’, find the first
‘k’ missing positive numbers in the array.
"""


import pytest


def find_first_k_missing_positive(nums: list[int], k: int) -> list[int]:
    n = len(nums)
    min_num = min([num for num in nums if num > 0])
    res = []

    start_num = 1
    while k > 0 and start_num < min_num:
        res.append(start_num)
        k -= 1
        start_num += 1

    i = 0
    while i < n:
        j = nums[i] - min_num
        if 0 <= j < n and nums[i] != nums[j]:
            nums[j], nums[i] = nums[i], nums[j]
            continue

        i += 1

    i = 0
    while k > 0 and i < n:
        supposed = i + min_num
        if nums[i] != supposed:
            res.append(supposed)
            k -= 1
        i += 1

    max_num = nums[i - 1]
    start_num = max_num + 1
    while k > 0 and start_num < max_num + k + 1:
        res.append(start_num)
        start_num += 1

    return res


def find_first_k_missing_positive_leetcode(nums: list[int], k: int) -> int:
    return find_first_k_missing_positive(nums, k)[-1]


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([3, -1, 4, 5, 5], 3, [1, 2, 6]),
        ([2, 3, 4], 3, [1, 5, 6]),
        ([-2, -3, 4], 2, [1, 2]),
    ],
)
def test_grokking(nums, k, expected):
    assert find_first_k_missing_positive(nums, k) == expected

"""
Problem Statement
We are given an array containing ‘n’ distinct numbers taken from the range
0 to ‘n’. Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers,
find the missing number.

Example 1
Input: [4, 0, 3, 1]
Output: 2

Example 2
Input: [8, 3, 5, 2, 4, 6, 0, 1]
Output: 7

Great LeetCode solution:
https://leetcode.com/problems/missing-number/solutions/2081185/python-easy-one-liners-with-explanation/?orderBy=most_votes&languageTags=python3
"""


import pytest


# grokking solution: O(N) time, O(1) space
def find_missing_number(nums: list[int]) -> int:
    i, n = 0, len(nums)
    while i < n:
        j = nums[i]
        # we need the first condition since the provided array has n-1 size
        if nums[i] < n and nums[i] != nums[j]:
            # since nums[i] == nums[nums[i]]
            nums[i], nums[j] = nums[j], nums[i]
            continue

        i += 1

    for i in range(n):
        if nums[i] != i:
            return i

    return n


# my solution: O(N) time, O(N) space
def find_missing_number_custom(nums: list[int]) -> int:
    intermediate_arr = [0] * (len(nums) + 1)

    for num in nums:
        intermediate_arr[num] = 1

    for idx in range(len(intermediate_arr)):
        if intermediate_arr[idx] == 0:
            return idx

    return -1


@pytest.mark.parametrize(
    "nums, expected",
    [([4, 0, 3, 1], 2), ([8, 3, 5, 2, 4, 6, 0, 1], 7), ([0, 1, 2, 3], 4)],
)
def test_grokking(nums, expected):
    assert find_missing_number(nums) == expected
    assert find_missing_number_custom(nums) == expected

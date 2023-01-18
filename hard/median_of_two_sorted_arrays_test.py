import math

import pytest


class Solution:

    def findMedianSortedArrays(self, nums1: list[int],
                               nums2: list[int]) -> float:
        nums = sorted(nums1 + nums2)
        n = len(nums)

        if n % 2 != 0:
            return nums[math.floor(n / 2)]

        pivot = math.floor(n / 2)
        return (nums[pivot - 1] + nums[pivot]) / 2


@pytest.mark.parametrize(
    "nums1,nums2,expected",
    [
        ([1, 3], [2], 2.00000),
        ([1, 2], [3, 4], 2.50000),
    ],
)
def test_solution(nums1, nums2, expected):
    assert Solution().findMedianSortedArrays(nums1, nums2) == expected

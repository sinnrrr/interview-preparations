from typing import List

import pytest


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
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
        ([4, 3, 2, 7, 8, 2, 3, 1], [2, 3]),
        ([1, 1, 2], [1]),
        ([1], []),
    ],
)
def test(nums, expected):
    assert Solution().findDuplicates(nums) == expected

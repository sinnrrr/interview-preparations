from typing import List

import pytest


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i in range(len(nums)):
            if v := nums_map.get(nums[i]):
                if v[0] * 2 == target:
                    return [v[1], i]
            else:
                nums_map[nums[i]] = (target - nums[i], i)

        for k in nums_map:
            value, idx = nums_map[k]

            match = nums_map[value]
            if match and match[1] != idx:
                return [idx, match[1]]

        return []


@pytest.mark.parametrize(
    "nums,target,expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ],
)
def test_solution(nums, target, expected):
    assert Solution().twoSum(nums, target) == expected

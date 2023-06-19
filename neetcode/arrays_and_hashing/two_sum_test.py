import pytest


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hmap = {}
        for curr in range(len(nums)):
            num_to_find = target - nums[curr]
            if hmap.get(num_to_find) is not None:
                return [hmap[num_to_find], curr]
            hmap[nums[curr]] = curr
        return []


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ],
)
def test_solution(nums, target, expected):
    assert Solution().twoSum(nums, target) == expected

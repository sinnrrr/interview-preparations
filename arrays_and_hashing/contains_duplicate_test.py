import pytest


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        for num in nums:
            for other_num_idx in range(1, len(nums)):
                if num == nums[other_num_idx]:
                    return True

        return False


@pytest.mark.parametrize(
    "nums, expected",
    [],
)
def test_solution(nums, expected):
    assert Solution().containsDuplicate(nums) == expected

import pytest


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        ans = 0
        nums_set = set(nums)
        for num in nums:
            if num - 1 in nums_set:
                continue
            curr = num + 1
            while curr in nums_set:
                curr += 1
            ans = max(ans, curr - num)
        return ans


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
    ],
)
def test_solution(nums, expected):
    assert Solution().longestConsecutive(nums) == expected

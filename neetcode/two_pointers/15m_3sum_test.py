import pytest


class Solution:
    def threeSumBruteforce(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        ans = []
        nums.sort()

        for i1 in range(n):
            if i1 > 0 and nums[i1] == nums[i1 - 1]:
                continue
            for i2 in range(n):
                for i3 in range(n):
                    if i1 == i2 or i1 == i3 or i2 == i3:
                        continue
                    if nums[i1] + nums[i2] + nums[i3] == 0:
                        ans.append([nums[i1], nums[i2], nums[i3]])
        return ans

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        ans = []
        nums.sort()

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, n - 1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return ans


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
    ],
)
def test_solution(nums, expected):
    assert Solution().threeSum(nums) == expected

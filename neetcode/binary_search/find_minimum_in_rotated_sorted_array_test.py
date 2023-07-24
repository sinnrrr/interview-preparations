import pytest


class Solution:
    def findMin(self, nums: list[int]) -> int:
        # n = len(nums)
        # m = int(n / 2)
        # l, r = 0, n - 1

        # while l != r or nums[l] > nums[r]:
        #     if nums[m] > nums[r]:
        #         l = m
        #     else:
        #         r = m

        # return nums[l]
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])

            # if were in left sorted portion it means all of the values on the left
            # always going to be bigger, than the right sorted portion, because of
            # the dircetion on array rotation
            if nums[l] < nums[m]:
                l = m + 1
            else:
                r = m - 1

        return res


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([3, 4, 5, 1, 2], 1),
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([11, 13, 15, 17], 11),
    ],
)
def test_solution(nums, expected):
    assert Solution().findMin(nums) == expected

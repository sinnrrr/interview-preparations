from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def run(l, r):
            if l > r:
                return -1

            m = (r + l) // 2

            if target == nums[m]:
                return m
            elif target > nums[m]:
                return run(m + 1, r)
            elif target < nums[m]:
                return run(l, m - 1)

            return -1

        return run(0, len(nums) - 1)


def test_solution():
    # assert Solution().search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert Solution().search([-1, 0, 3, 5, 9, 12], 2) == -1

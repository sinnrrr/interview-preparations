from typing import List

import pytest


# O(N^2)
class BruteforceSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)

        for n in range(length):
            for m in range(length):
                if n == m:
                    continue

                if nums[n] + nums[m] == target:
                    return [n, m]

        return []


# O(N)
class HashMapSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            remainder_id = hashmap.get(target - nums[i])
            if remainder_id is not None:
                return [remainder_id, i]

            hashmap[nums[i]] = i

        return []


# O(N * log(N))
class TwoPointersSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)

        for left in range(len(sorted_nums) - 1):
            right = len(sorted_nums) - 1

            while left < right:
                left_value = sorted_nums[left]
                right_value = sorted_nums[right]

                temp_sum = left_value + right_value

                if temp_sum > target:
                    right -= 1
                elif temp_sum < target:
                    left += 1
                else:
                    return [
                        nums.index(left_value),
                        nums.index(right_value, left + 1)
                        if left_value == right_value
                        else nums.index(right_value),
                    ]

        return []


Solution = TwoPointersSolution


@pytest.mark.parametrize(
    "nums,target,expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([-10, -1, -18, -19], -19, [2, 1]),
        ([3, 3], 6, [0, 1]),
    ],
)
def test_solution(nums, target, expected):
    assert Solution().twoSum(nums, target) == expected

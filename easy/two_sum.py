from abc import ABC, abstractmethod
from typing import List

import pytest


class SolutionBase(ABC):
    @abstractmethod
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pass


# O(N^2)
class BruteforceSolution(SolutionBase):
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
class HashMapSolution(SolutionBase):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            remainder_id = hashmap.get(target - nums[i])
            if remainder_id is not None:
                return [remainder_id, i]

            hashmap[nums[i]] = i

        return []


class Solution(HashMapSolution):
    pass


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

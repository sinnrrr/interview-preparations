from typing import DefaultDict, List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = DefaultDict(lambda: [])
        for i in range(len(nums)):
            nums_map[nums[i]].append(i)
        nums.sort()

        left, right = 0, len(nums) - 1

        while left <= right:
            sum = nums[left] + nums[right]

            if sum > target:
                right -= 1
            elif sum == target:
                if len(nums_map[nums[left]]) > 1:
                    return nums_map[nums[left]]
                return [nums_map[nums[left]][0], nums_map[nums[right]][0]]
            else:
                left += 1

        return []

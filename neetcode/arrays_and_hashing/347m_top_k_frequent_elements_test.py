from collections import defaultdict

import pytest


class Solution:
    # O(nlogn)
    def topKFrequentSort(self, nums: list[int], k: int) -> list[int]:
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1
        return sorted(
            freq_map,
            key=freq_map.get,
            reverse=True,
        )[:k]

    # O(n)
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        num_to_freq = defaultdict(int)
        for num in nums:
            num_to_freq[num] += 1

        freq_to_nums = [[] for _ in range(len(nums) + 1)]
        for num, count in num_to_freq.items():
            freq_to_nums[count].append(num)

        ans = []
        for i in range(len(freq_to_nums) - 1, 0, -1):
            for n in freq_to_nums[i]:
                if k == 0:
                    return ans
                ans.append(n)
                k -= 1
        return ans


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([1], 1, [1]),
    ],
)
def test_solution(nums, k, expected):
    assert Solution().topKFrequent(nums, k) == expected

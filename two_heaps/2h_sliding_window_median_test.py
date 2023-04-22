"""
Given an array of numbers and a number ‘k’, find the median of all the ‘k’ sized
sub-arrays (or windows) of the array.

Example 1:
Input: nums=[1, 2, -1, 3, 5], k = 2
Output: [1.5, 0.5, 1.0, 4.0]
Explanation: Lets consider all windows of size ‘2’:
[1, 2, -1, 3, 5] -> median is 1.5
[1, 2, -1, 3, 5] -> median is 0.5
[1, 2, -1, 3, 5] -> median is 1.0
[1, 2, -1, 3, 5] -> median is 4.0

Example 2:
Input: nums=[1, 2, -1, 3, 5], k = 3
Output: [1.0, 2.0, 3.0]
Explanation: Lets consider all windows of size ‘3’:
[1, 2, -1, 3, 5] -> median is 1.0
[1, 2, -1, 3, 5] -> median is 2.0
[1, 2, -1, 3, 5] -> median is 3.0
"""

from heapq import heappop, heappush

import pytest


class MedianFinder:
    def __init__(self) -> None:
        self.max_heap = []
        self.min_heap = []

    def insert_num(self, num: int):
        if not self.max_heap or -self.max_heap[0] >= num:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)
        self._rebalance_heaps()

    def _rebalance_heaps(self):
        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def remove_num(self, num: int):
        if num <= -self.max_heap[0]:
            self.max_heap.remove(-num)
        else:
            self.min_heap.remove(num)
        self._rebalance_heaps()
        # |||||||||||||||||||||
        # This works because whenever you delete something and nothing left in max_heap,
        # it balances it from elements of min_heap. This way you'll never stuck into the
        # situation when top of max_heap has bigger value, than min_heap.

    def find_median(self):
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2

        return -self.max_heap[0]


class Solution:
    def __init__(self) -> None:
        self.median_finder = MedianFinder()

    def find_median_all(self, nums: list[int], k: int):
        ans = []
        window_start = 0
        for window_end in range(len(nums)):
            self.median_finder.insert_num(nums[window_end])

            if window_end - window_start + 1 == k:
                ans.append(self.median_finder.find_median())
                self.median_finder.remove_num(nums[window_start])
                window_start += 1
        return ans


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 2, -1, 3, 5], 2, [1.5, 0.5, 1.0, 4.0]),
        ([1, 2, -1, 3, 5], 3, [1.0, 2.0, 3.0]),
    ],
)
def test_grokking(nums, k, expected):
    assert Solution().find_median_all(nums, k) == expected

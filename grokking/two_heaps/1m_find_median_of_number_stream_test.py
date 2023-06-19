"""
Design a class to calculate the median of a number stream. The class should have the
following two methods:
1. insertNum(int num) : stores the number in the class
2. findMedian() : returns the median of all numbers inserted in the class
If the count of numbers inserted in the class is even, the median will be the average of
the middle two numbers.
"""

from heapq import heappop, heappush


class Solution:
    def __init__(self) -> None:
        self.max_heap = []
        self.min_heap = []

    def insertNum(self, num: int):
        if not self.max_heap or -self.max_heap[0] >= num:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)

        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def findMedian(self):
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2

        return -self.max_heap[0]


def test():
    solution = Solution()
    solution.insertNum(3)
    solution.insertNum(1)
    assert solution.findMedian() == 2
    solution.insertNum(5)
    assert solution.findMedian() == 3
    solution.insertNum(4)
    assert solution.findMedian() == 3.5

from heapq import heappush, heappop


class MedianFinderBruteforce:
    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        self.nums.sort()

        n = len(self.nums)
        i = (n - 1) // 2

        return self.nums[i] if n % 2 != 0 else (self.nums[i] + self.nums[i + 1]) / 2


class MedianFinder:
    def __init__(self):
        self.l_max_heap = []
        self.r_min_heap = []

    def addNum(self, num: int) -> None:
        if not self.l_max_heap or num < -self.l_max_heap[0]:
            heappush(self.l_max_heap, -num)
        else:
            heappush(self.r_min_heap, num)

        if len(self.l_max_heap) - len(self.r_min_heap) > 1:
            heappush(self.r_min_heap, -heappop(self.l_max_heap))
        if len(self.r_min_heap) - len(self.l_max_heap) >= 1:
            heappush(self.l_max_heap, -heappop(self.r_min_heap))

    def findMedian(self) -> float:
        return (
            (-self.l_max_heap[0] + self.r_min_heap[0]) / 2
            if len(self.l_max_heap) == len(self.r_min_heap)
            else -self.l_max_heap[0]
        )

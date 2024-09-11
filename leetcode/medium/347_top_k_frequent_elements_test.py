from collections import Counter
import heapq


class Solution:
    def topKFrequentHeap(self, nums: list[int], k: int) -> list[int]:
        occurances = {}
        for num in nums:
            occurances[num] = occurances.get(num, 0) + 1

        heap = []
        for num, occ in occurances.items():
            heapq.heappush(heap, (-1 * occ, num))

        res = []
        while k > 0:
            res.append(heapq.heappop(heap)[1])
            k -= 1

        return res

    def topKFrequentBetterHeap(self, nums: list[int], k: int) -> list[int]:
        # 1: Use a Counter collection for frequency counts - this produces the same outcome as our verbose implementation in the brute force approach.
        counts = Counter(nums)
        # 2: Initialize a min heap
        min_heap = []

        for element, freq in counts.items():
            # 3: Manage the heap
            # Add each element to the heap
            heapq.heappush(min_heap, (freq, element))
            # If the size of the heap is larger than k, we pop the element at the top.
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # 4: What remains in the heap are the top k most frequent
        return [num for (count, num) in min_heap]

    def topKFrequentBucketSort(self, nums: list[int], k: int) -> list[int]:
        counts = Counter(nums)
        max_count = -1

        hmap = {}
        for num, occ in counts.items():
            max_count = max(max_count, occ)
            occ_list = hmap[occ] = hmap.get(occ, [])
            occ_list.append(num)
            hmap[occ] = occ_list

        res = []
        while k > 0 and max_count > 0:
            if not hmap.get(max_count):
                max_count -= 1
                continue
            res.append(hmap[max_count].pop())
            k -= 1

        return res


def test():
    assert Solution().topKFrequentBucketSort([5, 3, 1, 1, 1, 3, 73, 1], 2) == [1, 2]

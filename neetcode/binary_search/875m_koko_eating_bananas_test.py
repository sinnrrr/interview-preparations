# h - len(piles)


from math import ceil


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = ceil(sum(piles) / h), max(piles)
        while left < right:
            mid = (left + right) // 2
            total_time = 0
            for bananas_num in piles:
                total_time += ceil(bananas_num / mid)
                if total_time > h:
                    break
            if total_time <= h:
                right = mid
            else:
                left = mid + 1
        return right

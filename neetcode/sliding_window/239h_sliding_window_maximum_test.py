import collections


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        output = []
        start, end = 0, 0
        queue = collections.deque()

        while end < n:
            while queue and nums[queue[-1]] < nums[end]:
                queue.pop()
            queue.append(end)

            if start > queue[0]:
                queue.popleft()

            if (end + 1) >= k:
                output.append(nums[queue[0]])
                start += 1

            end += 1

        return output


def test():
    assert Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [
        3,
        3,
        5,
        5,
        6,
        7,
    ]

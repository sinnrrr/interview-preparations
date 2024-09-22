import random

"""
Instead of creating the array with W[i] repetitions to simulate weights:
    [1, 2] -> [1, 2, 2] and generating random out of this
We are calculating prefix sums and searching between the nums:
    [1, 2, 4] -> [1, 3, 7] and binary search to run it optimized
                /  |  |  |
               |_0_|  |  |
                  |_2_|  |
                     |_4_|
"""


class Solution:
    def __init__(self, w: list[int]):
        self.prefix_sums = []
        self.total = 0
        for weight in w:
            self.total += weight
            self.prefix_sums.append(self.total)

    def pickIndex(self) -> int:
        target = random.uniform(0, self.total)
        lp, rp = 0, len(self.prefix_sums)

        while lp < rp:
            mp = (lp + rp) // 2

            if self.prefix_sums[mp] < target:
                lp = mp + 1
            else:
                rp = mp

        return lp


def test():
    assert Solution([1, 1]).pickIndex() == 0

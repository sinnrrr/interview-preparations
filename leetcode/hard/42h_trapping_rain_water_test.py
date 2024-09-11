class Solution:
    def trap(self, height: list[int]) -> int:
        lp, rp = 0, len(height) - 1
        curr_lvl = -1
        volume = 0

        while lp <= rp:
            curr_lvl = max(curr_lvl, min(height[lp], height[rp]))

            # level is lower
            if height[lp] < curr_lvl:
                volume += curr_lvl - height[lp]
                lp += 1
                continue

            if height[rp] < curr_lvl:
                volume += curr_lvl - height[rp]
                rp -= 1
                continue

            # level is equal
            if height[lp] == curr_lvl:
                lp += 1

            if height[rp] == curr_lvl:
                rp -= 1

        return volume


def test():
    assert Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert Solution().trap([4, 2, 0, 3, 2, 5]) == 9
    assert Solution().trap([2, 0, 2]) == 2

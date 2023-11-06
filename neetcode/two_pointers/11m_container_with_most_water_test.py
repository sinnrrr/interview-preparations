import pytest


class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0

        while l < r:
            distance = r - l
            min_height = min(height[l], height[r])
            max_area = max(max_area, distance * min_height)

            if height[l] > height[r]:
                r -= 1
            else:
                # even if they are equal, we don't care
                l += 1
        return max_area

    def maxAreaBrute(self, height: list[int]) -> int:
        n = len(height)
        area = 0
        for l in range(n - 1):
            for r in range(l + 1, n):
                distance = r - l
                min_height = min(height[l], height[r])
                area = max(area, distance * min_height)
        return area


@pytest.mark.parametrize(
    "height, expected",
    [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
    ],
)
def test_solution(height, expected):
    assert Solution().maxArea(height) == expected
    assert Solution().maxAreaBrute(height) == expected

"""
Given an array of unsorted numbers and a target number, find all unique
quadruplets in it, whose sum is equal to the target number.
"""

import math

import pytest


def search_quadruplets(arr, target):
    """same as 3 pointers, just add one more loop"""
    arr.sort()

    ans = []
    n = len(arr)

    for i in range(n - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        for j in range(i + 1, n - 2):
            if j > 0 and arr[j] == arr[j - 1]:
                continue

            lp, rp = j + 1, n - 1

            while lp < rp:
                diff = target - (arr[i] + arr[j] + arr[lp] + arr[rp])

                if diff > 0:
                    lp += 1
                    continue

                if diff < 0:
                    rp -= 1
                    continue

                ans.append([arr[i], arr[j], arr[lp], arr[rp]])
                lp += 1
                rp -= 1

                while lp < rp and arr[lp - 1] == arr[rp]:
                    lp += 1
                while lp < rp and arr[rp + 1] == arr[rp]:
                    rp -= 1

    return ans


def search_quadruplets_ducked(arr, target):
    arr.sort()

    ans = []
    outer_left, outer_right = 0, len(arr) - 1

    while outer_left <= outer_right:
        target_inner_sum = target - (arr[outer_left] + arr[outer_right])
        inner_left, inner_right = outer_left + 1, outer_right - 1
        inner_diff = math.inf

        while inner_left <= inner_right:
            diff = target_inner_sum - (arr[inner_left] + arr[inner_right])

            if diff != 0:
                if abs(diff) < abs(inner_diff):
                    inner_diff = diff

                if diff > 0:
                    inner_right -= 1
                elif diff < 0:
                    inner_left += 1

                continue

            ans.append(
                [
                    arr[outer_right],
                    arr[inner_left],
                    arr[inner_right],
                    arr[outer_left],
                ]
            )

            # does not matter if it is left++ or right--
            inner_left += 1

        if inner_diff > 0:
            outer_right -= 1
        elif inner_diff < 0:
            outer_left += 1

    return ans


@pytest.mark.parametrize(
    "arr, target, expected",
    [
        ([4, 1, 2, -1, 1, -3], 1, [[-3, -1, 1, 4], [-3, 1, 1, 2]]),
        ([2, 0, -1, 1, -2, 2], 2, [[-2, 0, 2, 2], [-1, 0, 1, 2]]),
    ],
)
def test_search_quadruplets(arr, target, expected):
    assert search_quadruplets(arr, target) == expected

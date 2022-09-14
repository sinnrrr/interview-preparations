"""
Given an array arr of unsorted numbers and a target sum, count all triplets in
it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three
different indices.

Write a function to return the count of such triplets.
"""

import pytest


def triplet_with_smaller_sum(arr, target):
    arr.sort()

    n, ans = len(arr), 0

    for i in range(n - 2):
        left, right = i + 1, n - 1
        target_sum = target - arr[i]

        while left < right:
            # smaller than target
            if arr[left] + arr[right] < target_sum:
                ans += right - left
                left += 1
            else:
                right -= 1

    return ans


def triplet_with_smaller_sum_additional(arr, target):
    arr.sort()

    triplets = []

    for i in range(len(arr) - 2):
        _search_pairs_additional(arr, target - arr[i], i, triplets)

    return triplets


def _search_pairs_additional(arr, target_sum, first, triplets):
    left, right = first + 1, len(arr) - 1

    while left < right:
        # smaller than target
        if arr[left] + arr[right] < target_sum:
            for i in range(right, left, -1):
                triplets.append([arr[first], arr[left], arr[i]])
            left += 1
        else:
            right -= 1


@pytest.mark.parametrize(
    "arr, target, expected",
    [([-1, 0, 2, 3], 3, 2), ([-1, 4, 2, 1, 3], 5, 4)],
)
def test_triplet_with_smaller_sum(arr, target, expected):
    assert triplet_with_smaller_sum(arr, target) == expected


@pytest.mark.parametrize(
    "arr, target, expected",
    [
        ([-1, 0, 2, 3], 3, [[-1, 0, 3], [-1, 0, 2]]),
        ([-1, 4, 2, 1, 3], 5, [[-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]]),
    ],
)
def test_triplet_with_smaller_sum_additional(arr, target, expected):
    assert triplet_with_smaller_sum_additional(arr, target) == expected

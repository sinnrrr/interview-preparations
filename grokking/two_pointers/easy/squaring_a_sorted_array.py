"""
Given a sorted array, create a new array containing squares of all the
numbers of the input array in the sorted order.
"""

import collections

import pytest


def make_squares_custom(arr: list[int]):
    left, right = 0, len(arr) - 1
    ans = []

    while left <= right:
        left_squared = arr[left]**2
        right_squared = arr[right]**2

        ans.insert(0, max(left_squared, right_squared))

        if (left != right):
            ans.insert(0, min(left_squared, right_squared))

        left += 1
        right -= 1

    return ans


def make_squares_solution(arr: list[int]):
    n = len(arr)
    left, right = 0, n - 1
    highest_el_idx = n - 1
    ans = [0 for _ in range(n)]

    while left <= right:
        left_el = arr[left]**2
        right_el = arr[right]**2

        if left_el > right_el:
            ans[highest_el_idx] = left_el
            left += 1
        else:
            ans[highest_el_idx] = right_el
            right -= 1

        highest_el_idx -= 1

    return ans


def make_squares_better(arr: list[int]):
    ans = collections.deque()
    left, right = 0, len(arr) - 1

    while left <= right:
        left_abs, right_abs = abs(arr[left]), abs(arr[right])

        if left_abs > right_abs:
            ans.appendleft(left_abs * left_abs)
            left += 1
        else:
            ans.appendleft(right_abs * right_abs)
            right -= 1

    return list(ans)


@pytest.mark.parametrize(
    "arr, expected",
    [([-2, -1, 0, 2, 3], [0, 1, 4, 4, 9]),
     ([-3, -1, 0, 1, 2], [0, 1, 1, 4, 9])],
)
def test_make_squares_custom(arr, expected):
    assert make_squares_custom(arr) == expected


@pytest.mark.parametrize(
    "arr, expected",
    [([-2, -1, 0, 2, 3], [0, 1, 4, 4, 9]),
     ([-3, -1, 0, 1, 2], [0, 1, 1, 4, 9]), ([-5, -3, -2, -1], [1, 4, 9, 25])],
)
def test_make_squares_solution(arr, expected):
    assert make_squares_solution(arr.copy()) == expected
    assert make_squares_better(arr.copy()) == expected

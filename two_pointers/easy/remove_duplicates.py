"""
Given an array of sorted numbers, remove all duplicate number instances from
it in-place, such that each element appears only once. The relative order of
the elements should be kept the same and you should not use any extra space
so that that the solution have a space complexity of O(1).

Move all the unique elements at the beginning of the array and after moving
return the length of the subarray that has no duplicate in it.
"""

import pytest


def remove_duplicates_custom(arr: list[int]):
    next = 0
    available = next + 1

    while next != len(arr):
        if arr[available] != arr[next]:
            if next > available:
                arr[next], arr[available] = arr[available], arr[next]
                available += 1

        next += 1

    return available


def remove_duplicates_solution(arr: list[int]):
    i, next_non_duplicate = 0, 1

    while i < len(arr):
        # because it is sorted, we don't need to know if it is < or >
        if arr[next_non_duplicate - 1] != arr[i]:
            arr[next_non_duplicate] = arr[i]
            next_non_duplicate += 1
        i += 1

    return next_non_duplicate


def remove_element(arr: list[int], key: int):
    next_el = 0
    for i in range(len(arr)):
        if arr[i] != key:
            arr[next_el] = arr[i]
            next_el += 1

    return next_el


@pytest.mark.parametrize(
    "arr, expected",
    [([2, 3, 3, 3, 6, 9, 9], 4), ([2, 2, 2, 11], 2)],
)
def test_remove_duplicates(arr, expected):
    assert remove_duplicates_solution(arr.copy()) == expected
    assert remove_duplicates_custom(arr.copy()) == expected


@pytest.mark.parametrize(
    "arr, key, expected",
    [([3, 2, 3, 6, 3, 10, 9, 3], 3, 4), ([2, 11, 2, 2, 1], 2, 2)],
)
def test_remove_elements(arr, key, expected):
    assert remove_element(arr, key) == expected

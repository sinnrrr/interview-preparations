"""
Given an array containing 0s, 1s and 2s, sort the array in-place. You should
treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s
to recreate the array.

The flag of the Netherlands consists of three colors: red, white and blue; and
since our input array also consists of three different numbers that is why it
is called Dutch National Flag problem.
"""

import pytest


def dutch_flag_sort(arr):
    """
    low points to the end of 0s
    high points to the start of 2s
    i points to the current element

    low and high are bounds on which elements should swapped

    key thing here is why we increment/decrement i, low and high:
    1) i = 1:
       i++ because we ignore the 1s, as we swap the elements
       on low and high positions
    2) i = 0:
       low += 1 because we moved zero on low place and we need to have
       a pointer to the value we can replace on next iteration
       i += 1 because we cannot have 2 there, and since we are ignoring
       1s we increment our main pointer
    3) i = 2:
       we only decrement high, because we swap the elements and on the position
       of i could appear 0 or 1, skipping which would be unwanted thing to do
    """
    low, high = 0, len(arr) - 1

    i = 0
    while i <= high:
        el = arr[i]

        if el == 0:
            swap(arr, i, low)
            low += 1
            i += 1
        elif el == 1:
            i += 1
        elif el == 2:
            swap(arr, i, high)
            high -= 1

    return arr


def swap(A, i, j):
    A[i], A[j] = A[j], A[i]


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 0, 2, 1, 0], [0, 0, 1, 1, 2]),
        ([2, 2, 0, 1, 2, 0], [0, 0, 1, 2, 2, 2]),
    ],
)
def test_dutch_flag_sort(arr, expected):
    assert dutch_flag_sort(arr) == expected

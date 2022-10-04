"""
Given an array, find the length of the smallest subarray in it which when
sorted will sort the whole array.
"""


import math

import pytest

# def shortest_window_sort(arr):
#     left, right = 1, len(arr) - 2
#     max_left_idx, max_right_idx = None, None

#     while left <= right:
# if arr[right] <= arr[max_left_idx]:
#     left = max_left_idx

# if arr[right] > arr[left]:
#     max_left_idx = left
#     left += 1

# if not isinf(max_left_idx):

# right += 1
# ---
# if arr[left] < arr[left + 1]:
#     if max_left_idx is not None:
#         left += 1
# else:
#     max_left_idx = left

# if arr[right - 1] < arr[right]:
#     if max_right_idx is not None:
#         right -= 1
# else:
#     max_right_idx = right

# if max_left_idx is not None and max_right_idx is not None:


# return 0


def shortest_window_sort(arr):
    """
    This problem could be divided into following steps:
        1) Find the outer max left level
        2) Find the outer max right level
        3) Find min and max inner values
        4) Extend the left side while reached inner minimum
        5) Extend the right side while reached inner maximum

    Key rules:
        1) Early exits
        2) Do conditional checks inside while loop to break early

    Notes:
        1) Do not try to put everything into one while.
        2) Two pointers can be not only in one while loop, but
           also in separate ones.
    """
    low, high = 0, len(arr) - 1
    # find the first number out of sorting order from the beginning
    while low < len(arr) - 1 and arr[low] <= arr[low + 1]:
        low += 1

    if low == len(arr) - 1:  # if the array is sorted
        return 0

    # find the first number out of sorting order from the end
    while high > 0 and arr[high] >= arr[high - 1]:
        high -= 1

    # find the maximum and minimum of the subarray
    subarray_max = -math.inf
    subarray_min = math.inf
    for k in range(low, high + 1):
        subarray_max = max(subarray_max, arr[k])
        subarray_min = min(subarray_min, arr[k])

    # extend the subarray to include any number which is bigger than the minimum of the subarray
    while low > 0 and arr[low - 1] > subarray_min:
        low -= 1
    # extend the subarray to include any number which is smaller than the maximum of the subarray
    while high < len(arr) - 1 and arr[high + 1] < subarray_max:
        high += 1

    return high - low + 1


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 2, 5, 3, 7, 10, 9, 12], 5),
        ([1, 3, 2, 0, -1, 7, 10], 5),
        ([1, 2, 3], 0),
        ([3, 2, 1], 3),
    ],
)
def test_shortest_window_sort(arr, expected):
    assert shortest_window_sort(arr) == expected

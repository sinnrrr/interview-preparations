"""
Given an array with positive numbers and a positive target number, find all of
its contiguous subarrays whose product is less than the target number.
"""

from collections import deque

import pytest


def find_subarrays_custom(arr, target):
    """
    this solution does not work with pairs with more than 2 elements
    """
    ans, window_start = [], 0
    window_product = arr[window_start]

    for window_end in range(1, len(arr)):
        left, right = arr[window_start], arr[window_end]
        window_product *= right

        if window_end == 1 and left < target:
            ans.append([left])

        if right < target:
            ans.append([right])

        if window_product < target:
            ans.append([left, right])
            window_product /= left
            window_start += 1
            window_end += 1

    return ans


def find_subarrays_grokking(arr, target):
    """
    works for k > 2, but has n^3 time complexity
    """
    ans = []
    product = 1
    left = 0

    for right in range(len(arr)):
        product *= arr[right]

        # extract left element from window
        while product >= target and left <= right:
            product /= arr[left]
            left += 1

        # add current window elements to answer
        temp_list = deque()
        for i in range(right, left - 1, -1):
            """
            it starts from end, so first will be the ending element
            added to answers and then a pair will be formed in the deque
            and also will be added to answers

            we avoid duplicates as because we start iterating from end,
            this way we will have never duplicates, as the single element
            is added every two elements

            example:
            [1, 2, 3, 4]

            1) [[1]]
            2) [[1], [2], [2, 1]], where left = 0, right = 1,

                from right to left
                do
                    add element to subarray
                    add subarray to answers
                end

                1. subarray = [2], answers = [..., subarray]
                2. subarray = [2] + [1] = [2, 1],
                   answers = [..., subarray_from_first_step, subarray]

            same thing with more than two elements:
            1, 2, 3
            [1], [2], [2, 1], [3], [3, 2], [3, 2, 1]
            """
            temp_list.appendleft(arr[i])
            ans.append(list(temp_list))

    return ans


def find_subarrays_leetcode(arr, target):
    # window_start, product = 0, 1

    # for window_end in range(len(arr)):
    #     product *= arr[window_end]
    ...


def find_subarrays_grokking_better(arr, target):
    ans, temp_pairs = [], deque()
    lp, product = 0, 1

    for rp in range(len(arr)):
        if arr[rp] < target:
            ans.append([arr[rp]])

        product *= arr[rp]

        if product < target and len(temp_pairs) > 1:
            temp_pairs.append(arr[rp])
            ans.append(list(temp_pairs))
        else:
            temp_pairs.append(arr[rp])
            while product >= target:
                product /= arr[lp]
                lp += 1
                temp_pairs.popleft()
            if len(temp_pairs) > 1:
                ans.append(list(temp_pairs))

    while len(temp_pairs) > 2:
        temp_pairs.popleft()
        ans.append(list(temp_pairs))

    return ans


@pytest.mark.parametrize(
    "arr, target, expected",
    [
        ([2, 5, 3, 10], 30, [[2], [5], [2, 5], [3], [5, 3], [10]]),
        ([8, 2, 6, 5], 50, [[8], [2], [8, 2], [6], [2, 6], [5], [6, 5]]),
        (
            [10, 5, 2, 6],
            100,
            [[10], [5], [10, 5], [2], [5, 2], [6], [2, 6], [5, 2, 6]],
        ),
    ],
)
def test_find_subarrays(arr, target, expected):
    # assert find_subarrays_custom(arr, target) == expected  # fails test case 3
    assert find_subarrays_grokking(arr, target) == expected
    # assert (
    #     find_subarrays_grokking_better(arr, target) == expected
    # )  # fails test case 3

"""
You are visiting a farm to collect fruits. The farm has a single
row of fruit trees. You will be given two baskets, and your goal
is to pick as many fruits as possible to be placed in the given baskets.

You will be given an array of characters where each character represents
a fruit tree. The farm has following restrictions:

Each basket can have only one type of fruit. There is no limit to how many
fruit a basket can hold.

You can start with any tree, but you can’t skip a tree once you have started.
You will pick exactly one fruit from every tree until you cannot, i.e., you
will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both baskets.
"""

from collections import defaultdict

import pytest


def fruits_into_baskets(fruits):
    BASKETS_COUNT = 2

    window_start, max_fruits = 0, 0
    fruit_freq_map = defaultdict(int)

    for window_end in range(len(fruits)):
        right_char = fruits[window_end]
        fruit_freq_map[right_char] += 1

        while len(fruit_freq_map) > BASKETS_COUNT:
            left_char = fruits[window_start]
            fruit_freq_map[left_char] -= 1

            if fruit_freq_map[left_char] == 0:
                del fruit_freq_map[left_char]

            window_start += 1

        max_fruits = max(max_fruits, window_end - window_start + 1)

    return max_fruits


@pytest.mark.parametrize(
    "fruits, expected",
    [(["A", "B", "C", "A", "C"], 3), (["A", "B", "C", "B", "B", "C"], 5)],
)
def test_fruits_into_baskets(fruits, expected):
    assert fruits_into_baskets(fruits) == expected

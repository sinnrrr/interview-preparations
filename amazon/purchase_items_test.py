import heapq

import pytest


# time - O(m*i), space - O(i)
def solution(a: list[int], b: list[int], m: int):
    prices = {i: a[i] for i in range(len(a))}

    def purchase_item(i: int):
        temp = prices[i]
        prices[i] += b[i]
        return temp

    total_cost = 0
    while m > 0:
        lowest_value_item_idx = min(prices, key=prices.get)
        total_cost += purchase_item(lowest_value_item_idx)
        m -= 1

    return total_cost


# time - O(m*log(i)), space - O(i)
def heap_solution(a: list[int], b: list[int], m: int):
    heap = [(price, i) for i, price in enumerate(a)]
    heapq.heapify(heap)

    total_cost = 0
    while m > 0:
        lowest_value, lowest_value_item_idx = heapq.heappop(heap)
        total_cost += lowest_value
        heapq.heappush(
            heap, (lowest_value + b[lowest_value_item_idx], lowest_value_item_idx)
        )
        m -= 1

    return total_cost


@pytest.mark.parametrize(
    "a, b, m, expected",
    [([1, 2, 2], [3, 2, 1], 5, 12)],
)
def test_solution(a, b, m, expected):
    assert solution(a, b, m) == expected
    assert heap_solution(a, b, m) == expected

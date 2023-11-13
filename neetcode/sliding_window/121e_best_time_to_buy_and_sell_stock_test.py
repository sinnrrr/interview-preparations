import pytest


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        buy, sell = 0, 1
        while sell < len(prices):
            if prices[sell] < prices[buy]:
                buy = sell
            else:
                profit = max(profit, prices[sell] - prices[buy])
            sell += 1
        return profit

    def maxProfitBruteforce(self, prices: list[int]) -> int:
        profit = 0
        for buy_idx in range(len(prices)):
            for sell_idx in range(buy_idx + 1, len(prices)):
                profit = max(profit, prices[sell_idx] - prices[buy_idx])
        return profit


@pytest.mark.parametrize(
    "prices, expected",
    [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
    ],
)
def test_solution(prices, expected):
    assert Solution().maxProfit(prices) == expected
    assert Solution().maxProfitBruteforce(prices) == expected

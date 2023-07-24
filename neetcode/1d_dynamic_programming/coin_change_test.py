import pytest


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount == 0:
            return 0
        ans = -1
        coins.sort(reverse=True)
        curr_sum = 0
        i, j = 0, 0
        n = len(coins)
        while j != n and curr_sum != amount:
            if coins[i] > amount:
                continue

            if curr_sum + coins[i] > amount:
                i += 1

            if i == n:
                j += 1
                i = 0

        return ans


@pytest.mark.parametrize(
    "coins, amount, expected",
    [
        (),
    ],
)
def test_solution(coins: list[int], amount: int, expected):
    assert Solution().coinChange(coins, amount) == expected

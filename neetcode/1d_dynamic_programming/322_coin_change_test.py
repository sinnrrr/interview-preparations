import pytest


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        pass


@pytest.mark.parametrize(
    "coins, amount, expected",
    [
        (),
    ],
)
def test_solution(coins: list[int], amount: int, expected):
    assert Solution().coinChange(coins, amount) == expected

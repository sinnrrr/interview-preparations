package main

func maxProfit(prices []int) int {
	n := len(prices)
	l, r := 0, 1
	profit := 0

	for l < n && r < n {
		if prices[r] < prices[l] {
			l = r
		}

		curr_profit := prices[l] - prices[r]
		if curr_profit > profit {
			profit = curr_profit
		}

		r += 1
	}

	return profit
}

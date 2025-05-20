class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0

        # First pass: max profit up to day i
        left_profits = [0] * n
        min_price = prices[0]
        for i in range(1, n):
            min_price = min(min_price, prices[i])
            left_profits[i] = max(left_profits[i - 1], prices[i] - min_price)

        # Second pass: max profit from day i to end
        max_price = prices[-1]
        right_profits = [0] * n
        for i in range(n - 2, -1, -1):
            max_price = max(max_price, prices[i])
            right_profits[i] = max(right_profits[i + 1], max_price - prices[i])

        # Combine both: max left + max right
        max_total = 0
        for i in range(n):
            max_total = max(max_total, left_profits[i] + right_profits[i])

        return max_total

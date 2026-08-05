class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # O(n), O(1)
        l = res = 0

        for r in range(len(prices)):

            if prices[r] > prices[l]:
                curr = prices[r] - prices[l]
                res = max(curr, res)
            else:
                l = r

        return res
class Solution:
    def numSquares(self, n: int) -> int:
        
        # coin change, first list all perfect squares:
        # O(n * √n), O(n)
        
        coins = []
        for i in range(1, int((n) ** 0.5) + 1 ):
            if i * i <= n:
                coins.append(i*i)
        
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for c in coins:
                if i >= c:
                    dp[i] = min(dp[i], 1 + dp[i - c])
        
        return dp[n]      

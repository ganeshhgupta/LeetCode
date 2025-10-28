class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7
        
        powers = []
        for i in range(1, int(n**(1/x)) + 2): # start with 1, add +2 in upper bound for safety
            if i**x <= n:
                powers.append(i**x)
        
        return self.change(n, powers) % MOD
    
    def change(self, amount: int, coins: List[int]) -> int: # literally coin change 2, but can't use same coin twice
        
        # O(n . amount), O(amount) 

        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(len(coins) - 1, -1, -1):
            new_dp = [0] * (amount + 1)
            new_dp[0] = 1

            for j in range(1, amount + 1):
                new_dp[j] = dp[j]

                if j - coins[i] >= 0:
                    new_dp[j] += dp[j - coins[i]]
            
            dp = new_dp
        return dp[amount]
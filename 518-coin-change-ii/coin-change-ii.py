class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        # O(amount × n), O(amount × n)

        cache = {}

        def dfs(i, curr):

            if curr > amount or i == len(coins):
                return 0
            
            if curr == amount:
                return 1
            
            if (i, curr) in cache:
                return cache[(i, curr)]
            
            cache[(i, curr)] = dfs(i, curr + coins[i] ) + dfs(i + 1, curr)
        
            return cache[(i, curr)]
    
        return dfs(0, 0)
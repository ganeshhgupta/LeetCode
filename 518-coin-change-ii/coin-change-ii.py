class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        memo = {}

        def dfs(i, cur):

            if i >= len(coins) or cur > amount: 
                return 0

            if cur == amount: 
                return 1

            if (i, cur) in memo: 
                return memo[(i, cur)]
            
            memo[(i, cur)] = dfs(i, cur + coins[i]) + dfs(i + 1, cur)
            return memo[(i, cur)]

        return dfs(0, 0)
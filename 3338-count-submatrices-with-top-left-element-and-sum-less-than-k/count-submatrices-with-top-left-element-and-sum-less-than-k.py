class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        
        # 2d dp, O(mn), O(mn)
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        res = 0

        dp[0][0] = grid[0][0]
        if dp[0][0] <= k:
            res += 1

        # first column
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
            if dp[i][0] <= k:
                res += 1

        # first row
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
            if dp[0][j] <= k:
                res += 1

        # rest
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = (
                    grid[i][j]
                    + dp[i-1][j]
                    + dp[i][j-1]
                    - dp[i-1][j-1]
                )
                if dp[i][j] <= k:
                    res += 1

        return res
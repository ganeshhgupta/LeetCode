class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:

        # O(m.n), O(m.n)
        m, n = len(dungeon), len(dungeon[0])
        dp = [[0] * n for _ in range(m)]
        dp[m-1][n-1] = max(1 - dungeon[m-1][n-1], 1)

        # fill last column (can only go down)
        for i in range(m-2, -1, -1):
            dp[i][n-1] = max(dp[i+1][n-1] - dungeon[i][n-1], 1)

        # fill last row (can only go right)
        for j in range(n-2, -1, -1):
            dp[m-1][j] = max(dp[m-1][j+1] - dungeon[m-1][j], 1)

        # fill the rest bottom-right to top-left
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i][j] = max( min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j], 1)

        return dp[0][0]
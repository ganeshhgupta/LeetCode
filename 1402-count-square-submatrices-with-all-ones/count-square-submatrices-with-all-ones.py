class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        # O(m*n), O(m*n) variation of 221. Maximal Square
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n+1) for _ in range(m+1)]
        res = 0
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if matrix[i][j] == 1:
                    dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])
                    res += dp[i][j]  # add count instead of tracking max
        
        return res  # return sum instead of area
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        # O(M×N), O(M×N)
         
        M, N = len(word1), len(word2)
        dp = [[0] * (N + 1) for _ in range(M + 1)]

        for i in range(M + 1):
            dp[i][N] = M - i
        for j in range(N + 1):
            dp[M][j] = N - j
        
        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(dp[i+1][j+1], dp[i][j+1], dp[i+1][j])
        
        return dp[0][0]
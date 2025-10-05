class Solution:
    def findCoins(self, numWays: List[int]) -> List[int]:
        dp = [1] + numWays
        res = []

        for i in range(1, len(dp)):
            if dp[i] > 1:
                return []
            if dp[i] == 0:
                continue
            res.append(i)

            for j in range(len(dp) - 1, i-1, -1):
                dp[j] -= dp[ j-i ]
                if dp[j] < 0:
                    return []
        return res



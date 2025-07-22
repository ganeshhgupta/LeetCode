class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        index_map = {x: i for i, x in enumerate(arr)}
        dp = [[2] * n for _ in range(n)]
        max_len = 0

        for j in range(n):
            for i in range(j):
                x = arr[j] - arr[i]
                k = index_map.get(x)
                if k is not None and k < i:
                    dp[i][j] = dp[k][i] + 1
                    max_len = max(max_len, dp[i][j])
        
        return max_len if max_len >= 3 else 0

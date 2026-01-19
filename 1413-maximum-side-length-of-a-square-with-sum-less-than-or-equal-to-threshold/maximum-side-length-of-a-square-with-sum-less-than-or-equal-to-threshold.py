class Solution:
    def maxSideLength(self, mat, threshold):
        m, n = len(mat), len(mat[0])

        # Prefix sum matrix
        pref = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pref[i][j] = (
                    mat[i - 1][j - 1]
                    + pref[i - 1][j]
                    + pref[i][j - 1]
                    - pref[i - 1][j - 1]
                )

        max_len = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                k = max_len + 1
                if i >= k and j >= k:
                    curr_sum = (
                        pref[i][j]
                        - pref[i - k][j]
                        - pref[i][j - k]
                        + pref[i - k][j - k]
                    )
                    if curr_sum <= threshold:
                        max_len = k

        return max_len
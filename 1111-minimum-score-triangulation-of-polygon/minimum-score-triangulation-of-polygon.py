class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        # https://www.youtube.com/watch?v=h6MxKmDimhg

        v = values

        @cache
        def dfs(i, j):

            tmp = float('inf')

            for k in range(i+1, j):
                tmp = min(tmp, v[i] * v[k] * v[j] + dfs(i, k) + dfs(k, j))

            if tmp == float('inf'):
                return 0
            return tmp

        return dfs(0, len(v) - 1)
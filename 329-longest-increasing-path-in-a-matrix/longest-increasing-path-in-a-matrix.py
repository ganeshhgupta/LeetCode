class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        # O(M * N), O(M * N)
        
        M, N = len(matrix), len(matrix[0])
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        memo = {}  # (r, c) -> longest path starting here

        def dfs(r, c):
            if (r, c) in memo:
                return memo[(r, c)]

            longest = 1 
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < M and 0 <= nc < N and matrix[nr][nc] > matrix[r][c]:
                    longest = max(longest, 1 + dfs(nr, nc))

            memo[(r, c)] = longest
            return longest

        res = 0
        for r in range(M):
            for c in range(N):
                res = max(res, dfs(r, c))

        return res

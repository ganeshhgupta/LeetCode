class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        N, M = len(grid), len(grid[0])
        dirs = [[0,1], [1,0], [0,-1], [-1,0]]
        v = set()

        def dfs(r, c):
            if 0 <= r < N and 0 <= c < M and (r, c) not in v and grid[r][c] == 0:
                v.add((r, c))

                for dr, dc in dirs:
                    dfs(r + dr, c + dc)

        # Remove islands touching the border
        for i in range(N):
            dfs(i, 0)
            dfs(i, M - 1)

        for j in range(M):
            dfs(0, j)
            dfs(N - 1, j)

        res = 0

        # Count remaining islands
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 0 and (i, j) not in v:
                    res += 1
                    dfs(i, j)

        return res
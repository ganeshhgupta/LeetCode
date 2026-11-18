class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        N, M = len(grid), len(grid[0])
        dirs = [[0,1], [1,0], [-1,0], [0,-1]]
        res = 0

        def dfs(r, c):

            if not (0 <= r < N and 0 <= c < M) or grid[r][c] == '0':
                return
            
            grid[r][c] = '0'

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)
            
            return
        
        for r in range(N):
            for c in range(M):
                if grid[r][c] == '1':
                    dfs(r, c)
                    res += 1
        
        return res

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:

        N, M = len(grid), len(grid[0])
        dirs = [[0,1], [1,0], [0,-1], [-1,0]]
        v = set()

        def dfs(r, c, par_r, par_c, ch):
            if (r, c) in v:
                return True

            v.add((r, c))

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == ch:
                    
                    if (nr, nc) != (par_r, par_c):
                        if (nr, nc) in v:
                            return True
                        if dfs(nr, nc, r, c, ch):
                            return True

            return False

        for i in range(N):
            for j in range(M):
                if (i, j) not in v:
                    if dfs(i, j, -1, -1, grid[i][j]):
                        return True

        return False
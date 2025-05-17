class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        N = len(grid)
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def invalid(r, c):
            return min(r, c) < 0 or max(r, c) == N
        
        def dfs(r, c, label):
            if invalid(r, c) or grid[r][c] != 1:
                return 0
            grid[r][c] = label
            size = 1
            for dr, dc in dirs:
                size += dfs(r+dr, c+dc, label)
            return size
        

        #1. precompute areas
        size = defaultdict(int)
        label = 2
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    size[label] = dfs(r, c, label)
                    label += 1

        # connects all four neis to flipped water
        def connect(r, c):
            visit = set()
            res = 1
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if not invalid(nr, nc) and grid[nr][nc] > 1 and grid[nr][nc] not in visit:
                    res += size[grid[nr][nc]]
                    visit.add(grid[nr][nc])
            return res

        #2. try flipping water
        res = 0 if not size else max(size.values())
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 0:
                    res = max(res, connect(r, c))
        return res
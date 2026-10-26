class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        
        # TC O(mn), SC O(1)
        
        rows, cols = len(grid), len(grid[0])
        dirs = [[0,1], [1,0], [-1,0], [0,-1]]
        count = 0

        def dfs(r, c):

            if not (0 <= r < rows) or not (0 <= c < cols) or grid[r][c] == 0:
                return 0
            
            val = grid[r][c]

            grid[r][c] = 0
            for dr, dc in dirs:
                val += dfs(r +dr , c + dc)
            
            return val

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0:
                    if dfs(r, c) % k == 0:
                        count += 1
        return count 
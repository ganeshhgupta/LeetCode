class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        dirs = [[0,1], [1,0], [-1,0], [0,-1]]
        count = 0

        def dfs(r, c):

            if not (0 <= r < rows) or not (0 <= c < cols):
                return False # not closed
            if grid[r][c] == 1: # closed
                return True

            grid[r][c] = 1
            isClosed = True

            for dr, dc in dirs:
                if not dfs(r + dr, c + dc):
                    isClosed = False

            return isClosed

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    if dfs(r, c):
                        count += 1
        return count




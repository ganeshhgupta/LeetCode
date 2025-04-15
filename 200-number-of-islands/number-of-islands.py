class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        dirs = [[0,1], [1,0], [-1,0], [0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):

            if not ( 0 <= r < ROWS and 0 <= c < COLS ) or grid[r][c] == '0' :
                return

            grid[r][c] = '0'

            for dr, dc in dirs:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' :
                    dfs(r, c)
                    count += 1

        return count
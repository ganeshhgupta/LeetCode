class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        #dfs
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        row, col = len(grid), len(grid[0])
        island_count = 0

        def dfs(r, c):

            if not (0 <= r < row) or not (0 <= c < col) or grid[r][c] == "0": #if water or out of bounds
                return 
            
            grid[r][c] = "0" #turn vistied grid to water

            for dr, dc in directions:   #dfs in all four directions
                dfs(r + dr, c + dc)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    dfs(r, c)
                    island_count += 1

        return island_count


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #dfs
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        row, col = len(grid), len(grid[0])
        curr_area = 0
        max_area = 0

        def dfs(r, c):

            if not (0 <= r < row) or not (0 <= c < col) or grid[r][c] == 0: #if water or out of bounds
                return 0
            
            grid[r][c] = 0 #turn vistied grid to water
            curr_area = 1
            for dr, dc in directions:   #dfs in all four directions
                curr_area += dfs(r + dr, c + dc)
            return curr_area

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    curr_area = dfs(r, c)
                    max_area = max(curr_area, max_area)

        return max_area
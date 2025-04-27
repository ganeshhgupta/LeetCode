class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        rows, cols = len(image), len(image[0])
        dirs = [[0,1],[1,0],[-1,0],[0,-1]]
        visited = set()
        og_color = image[sr][sc]

        def dfs(r, c):
            if not (0 <= r < rows) or not (0 <= c < cols) or image[r][c] != og_color or (r, c) in visited:
                return
            
            image[r][c] = color
            visited.add((r, c))

            for dr, dc in dirs:
                dfs(r + dr, c + dc)

        dfs(sr, sc)
        return image
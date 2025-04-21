from typing import List

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        rows, cols = len(maze), len(maze[0])
        visited = set()
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def invalid(r, c):
            return not (0 <= r < rows and 0 <= c < cols)

        def dfs(r, c):

            if [r, c] == destination:
                return True

            if invalid(r, c) or maze[r][c] == 1 or (r, c) in visited:
                return False

            visited.add((r, c))

            for dr, dc in dirs:
                nr, nc = r, c
                while not invalid(nr + dr, nc + dc) and maze[nr + dr][nc + dc] == 0:
                    nr += dr
                    nc += dc

                if dfs(nr, nc):
                    return True

            return False

        return dfs(start[0], start[1])

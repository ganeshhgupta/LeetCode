class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        # O(mn), O(mn)
        R, C = len(grid), len(grid[0])
        dirs = [(dr, dc) for dr in [-1,0,1] for dc in [-1,0,1]]

        q = deque([(0, 0, 1)])
        v = set()

        while q:

            r, c, dist = q.popleft()

            if (r, c) in v or grid[r][c] == 1:
                continue

            if r == R-1 and c == C-1:
                return dist

            v.add((r, c))

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if 0 <= nr < R and 0 <= nc < C:
                    q.append((nr, nc, dist + 1))

        return -1
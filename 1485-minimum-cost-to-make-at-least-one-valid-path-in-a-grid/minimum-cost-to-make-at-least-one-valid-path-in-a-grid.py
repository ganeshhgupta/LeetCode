class Solution:
    def minCost(self, grid):

        # O(mn), O(mn)
        # O/1 bfs: make cost += 1 when cell dir != traversal dir
        # traverse low cost cells first

        m, n = len(grid), len(grid[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]

        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0

        dq = deque([(0,0)])

        while dq:
            r, c = dq.popleft()

            for k, (dr, dc) in enumerate(dirs):
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n: # isvalid
                    if grid[r][c] == k + 1:
                        cost = 0 
                    else:
                        cost = 1

                    if dist[r][c] + cost < dist[nr][nc]:
                        dist[nr][nc] = dist[r][c] + cost

                        if cost == 0:
                            dq.appendleft((nr, nc))
                        else:
                            dq.append((nr, nc))

        return dist[m-1][n-1]
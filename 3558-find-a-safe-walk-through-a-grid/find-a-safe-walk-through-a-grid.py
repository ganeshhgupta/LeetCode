class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:

        # O(n·m), O(n·m)
        
        n, m = len(grid), len(grid[0])
        dist = [[float('inf')] * m for _ in range(n)] #  min cost to reach any (r, c) from (0,0)
        dist[0][0] = grid[0][0]  # cost of starting cell itself
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]

        q = deque([(0, 0)])

        while q:
            r, c = q.popleft()

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m:

                    curr_cost = dist[r][c]
                    nei_cost = dist[r][c] + grid[nr][nc]

                    if  nei_cost < dist[nr][nc]:
                        dist[nr][nc] = nei_cost

                        if grid[nr][nc] == 0:
                            q.appendleft((nr, nc))
                        else:
                            q.append((nr, nc))

        return health - dist[n-1][m-1] > 0



        
    '''
    0-1 BFS

    Use deque; When you move to a neighbor:

    If it costs 0 (safe cell) → push it to the front of the deque.
    If it costs 1 (unsafe cell) → push it to the back of the deque.

    This keeps cheaper (0-cost) options always processed first, mimicking Dijkstra's "always expand smallest distance" behavior — but without needing a heap.
    '''

            

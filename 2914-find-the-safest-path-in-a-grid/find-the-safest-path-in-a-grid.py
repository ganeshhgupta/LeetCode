class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:

        # 1. use multi-bfs to do distance mapping
        # 2. use modified dijkstra to find shortest + safest path in that map
        # O (n^2) + (n^2 log n), O(n^2)
        
        N = len(grid)

        def valid(r, c):
            return 0 <= r < N and 0 <= c < N

        def precompute():
            q = deque()
            min_dist = {}

            # Multi-source BFS from thieves
            for r in range(N):
                for c in range(N):
                    if grid[r][c] == 1:
                        q.append((r, c, 0))
                        min_dist[(r, c)] = 0

            while q:
                r, c, dist = q.popleft()
                for r2, c2 in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                    if valid(r2, c2) and (r2, c2) not in min_dist:
                        min_dist[(r2, c2)] = dist + 1
                        q.append((r2, c2, dist + 1))

            return min_dist

        min_dist = precompute()

        # Max heap (negative values)
        maxh = [(-min_dist[(0, 0)], 0, 0)]
        visited = set()
        visited.add((0, 0))

        while maxh:
            dist, r, c = heapq.heappop(maxh)
            dist = -dist

            if (r, c) == (N - 1, N - 1):
                return dist

            for r2, c2 in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if valid(r2, c2) and (r2, c2) not in visited:
                    visited.add((r2, c2))
                    new_dist = min(dist, min_dist[(r2, c2)])
                    heapq.heappush(maxh, (-new_dist, r2, c2))

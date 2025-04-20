class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        N = len(grid)
        dirs = [[0,1], [0,-1], [-1,0], [1,0]]
        visit = set()

        def invalid(r,c):
            if min(r,c) < 0 or max(r,c) == N:
                return True
            else:
                return False

        def dfs(r, c):
            if invalid(r, c) or not grid[r][c] or (r, c) in visit:
                return
            visit.add((r,c))
            for dr, dc in dirs:
                dfs(r + dr, c + dc)

        def bfs():
            res = 0
            q = deque(visit)
            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in dirs:
                        curr_r, curr_c = r + dr, c + dc
                        if invalid(curr_r, curr_c) or (curr_r, curr_c) in visit:
                            continue
                        if grid[curr_r][ curr_c]:
                            return res
                        q.append([curr_r, curr_c])
                        visit.add((curr_r, curr_c))
                res += 1

        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    dfs(r, c)
                    return bfs()


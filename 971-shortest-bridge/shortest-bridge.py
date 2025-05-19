class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        #revise
        #1. bruteforce untill finds a single '1'
        #2. dfs out the entire island and add to visited
        #3. use visit hashset as a queue
        #4. do bfs from queue untill second island is reached

        N = len(grid)
        dirs = [[0,1], [0,-1], [-1,0], [1,0]]
        visit = set()

        def invalid(r, c):
            if min(r, c) < 0 or max(r, c) == N:
                return True
            return False
        
        def dfs(r, c):
            if invalid(r, c) or grid[r][c] == 0 or (r, c) in visit:
                return
            visit.add((r, c))
            for dr, dc in dirs:
                dfs(r + dr, c + dc)
        
        def bfs():
            q = deque(visit)
            res = 0
            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in dirs:
                        nr, nc = r + dr, c + dc
                        if invalid(nr, nc) or (nr, nc) in visit:
                            continue
                        if grid[nr][nc] == 1: #2nd island found
                            return res
                        q.append([nr, nc])
                        visit.add((nr, nc))
                res += 1
                
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    dfs(r, c)
                    return bfs()



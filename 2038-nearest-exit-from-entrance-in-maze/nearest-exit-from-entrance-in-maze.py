class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        # O(M·N), O(M·N)
        M, N = len(maze), len(maze[0])
        dirs = [[0,1], [1,0], [0,-1], [-1,0]]

        q = deque([(entrance[0], entrance[1], 0)]) # start and steps
        v = {(entrance[0], entrance[1])}

        while q:
            r, c, steps = q.popleft()
            if ( r == M-1 or r == 0 or c == 0 or c == N-1 ) and [r, c] != entrance:
                return steps
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < M and 0 <= nc < N and maze[nr][nc] == '.' and (nr, nc) not in v:
                    v.add((nr, nc))
                    q.append((nr, nc, steps + 1))
        
        return -1
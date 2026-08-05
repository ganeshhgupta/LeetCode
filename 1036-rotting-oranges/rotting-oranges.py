class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # O(M × N), O(M × N)
        M, N = len(grid), len(grid[0])
        dirs = [[0,1], [1,0], [0,-1], [-1,0]]
        q = deque()
        res = fresh = 0

        # first pass, add all rotten orgs to q, all fresh to counter 'fresh' :

        for r in range(M):
            for c in range(N):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        # check whether there are fresh orgs left at all:

        if fresh == 0:
            return 0

        # now, run bfs from all orgs in q:

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < M and 0 <= nc < N and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))

            res += 1

        return res - 1 if fresh == 0 else -1
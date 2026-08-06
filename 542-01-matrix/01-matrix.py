class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        # O(mn), O(mn)

        R, C = len(mat), len(mat[0])

        q = deque()
        dist = [[-1] * C for _ in range(R)]

        # add all zeros as starting points
        for r in range(R):
            for c in range(C):
                if mat[r][c] == 0:
                    q.append((r, c))
                    dist[r][c] = 0

        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        while q:

            r, c = q.popleft()

            for dr, dc in dirs:

                nr, nc = r + dr, c + dc

                if 0 <= nr < R and 0 <= nc < C and dist[nr][nc] == -1:

                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

        return dist
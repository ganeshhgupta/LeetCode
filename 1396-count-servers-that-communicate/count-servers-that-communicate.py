class Solution:
    def countServers(self, grid: list[list[int]]) -> int:

        # O(mn), O(m+n)
        
        rows = defaultdict(int)
        cols = defaultdict(int)

        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1

        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if rows[i] > 1 or cols[j] > 1:
                        ans += 1

        return ans
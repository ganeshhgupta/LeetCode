class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        # O(n!), O(n^2)
        
        col, diag, anti_diag = set(), set(), set()
        b = [["."] * n for _ in range(n)]
        res = []

        def dfs(r):
            if r == n:
                copy = ["".join(row) for row in b]
                res.append(copy)
                return
            
            for c in range(n):
                if c not in col and (r-c) not in diag and (r+c) not in anti_diag:

                    col.add(c)
                    diag.add(r-c)
                    anti_diag.add(r+c)
                    b[r][c] = 'Q'

                    dfs(r + 1)

                    col.remove(c)
                    diag.remove(r-c)
                    anti_diag.remove(r+c)
                    b[r][c] = '.'
        dfs(0)
        return res



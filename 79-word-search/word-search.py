from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True

            if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != word[i] or (r, c) in path:
                return False

            path.add((r, c))
            res = False
            for dr, dc in dirs:
                if dfs(r + dr, c + dc, i + 1):
                    res = True
                    break
            path.remove((r, c))
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False

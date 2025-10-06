class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        # O(RC), O(RC)
        R, C = len(matrix), len(matrix[0])
        cache = {}

        def helper(r, c):
            if r >= R or c >= C: return 0
            
            if (r, c) not in cache:
                right = helper(r, c+1)
                down = helper(r+1, c)
                diag = helper(r+1, c+1)
                cache[(r, c)] = 0
                if matrix[r][c] == '1': cache[(r, c)] = 1 + min(right, down, diag)
            return cache[(r, c)]

        helper(0, 0)
        return max(cache.values()) ** 2
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        
        rz, cz = set(), set()
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    rz.add(r)
                    cz.add(c)
        
        #Second pass: zero out the marked rows
        for r in rz:
            for c in range(cols):
                matrix[r][c] = 0
        
        #Third pass: zero out the marked columns
        for c in cz:
            for r in range(rows):
                matrix[r][c] = 0

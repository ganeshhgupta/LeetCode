from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        rows, cols = len(matrix), len(matrix[0])
        rz, cz = set(), set()

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    rz.add(r)
                    cz.add(c)
        for r in rz:
            for c in range(cols):
                matrix[r][c] = 0
        for r in range(rows):
            for c in cz:
                matrix[r][c] = 0

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        # O(n^2), O(1)
        
        m, n = len(matrix), len(matrix[0])

        firstRow = False
        for j in range(n):
            if matrix[0][j] == 0:
                firstRow = True
                break

        firstCol = False
        for i in range(m):
            if matrix[i][0] == 0:
                firstCol = True
                break

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0

        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0

        if firstRow:
            for j in range(n):
                matrix[0][j] = 0

        if firstCol:
            for i in range(m):
                matrix[i][0] = 0

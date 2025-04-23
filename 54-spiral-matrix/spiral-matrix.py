class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        re = len(matrix)
        ce = len(matrix[0])
        l = len(matrix) *  len(matrix[0])
        rs, cs = 0, 0
        r, c = 0, 0
        li = []

        while len(li) < l:

        #if len(li) <  l:
            for c in range(cs, ce):
                li.append(matrix[r][c])
            rs += 1

        #if len(li) <  l:
            for r in range(rs, re):
                li.append(matrix[r][c])
            ce -= 1

        #if len(li) <  l:
            for c in range(ce - 1, cs - 1, -1):
                li.append(matrix[r][c])
            re -= 1

        #if len(li) <  l:
            for r in range(re - 1, rs - 1, -1):
                li.append(matrix[r][c])
            cs += 1

        return li[:l]

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        rows, cols = len(mat), len(mat[0])
        res = []
        r = c = 0
        dir = 1  #1 means moving up-right, -1 means down-left

        for _ in range(rows * cols):
            res.append(mat[r][c])
            if dir == 1:
                if c == cols - 1:
                    r, dir = r+1, -1
                elif r == 0:
                    c, dir = c+1, -1
                else:
                    r, c = r-1, c+1
            else:
                if r == rows - 1:
                    c, dir = c+1, 1
                elif c == 0:
                    r, dir = r+1, 1
                else:
                    r, c = r+1, c-1
        return res

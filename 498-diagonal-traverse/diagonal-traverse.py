from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        rows, cols = len(mat), len(mat[0])
        res = []
        r = c = 0
        direction = 1  #1 means moving up-right, -1 means down-left

        for _ in range(rows * cols):
            res.append(mat[r][c])
            if direction == 1:
                #priority : right bound, top bound
                if c == cols - 1:
                    r += 1
                    direction = -1
                elif r == 0:
                    c += 1
                    direction = -1
                else:
                    r -= 1
                    c += 1
            else:
                #priority : bottom bound, left bound
                if r == rows - 1:
                    c += 1
                    direction = 1
                elif c == 0:
                    r += 1
                    direction = 1
                else:
                    r += 1
                    c -= 1

        return res

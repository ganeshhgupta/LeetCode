class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:

        res = 0
        resCount = 0

        for r in range(len(mat) - 1, -1, -1):

            count = mat[r].count(1)

            if count >= resCount:
                res = r
                resCount = count

        return [res, resCount]
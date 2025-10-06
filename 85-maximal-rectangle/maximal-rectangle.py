class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
       
        # O(R*C), O(C)
        R, C = len(matrix), len(matrix[0])
        h = [0] * (C + 1)
        res = 0

        def maxRec(heights):
            s = [-1]
            max_area = 0
            for i, ht in enumerate(heights):
                while s and heights[s[-1]] > ht:
                    height = heights[s.pop()]
                    width = i - s[-1] - 1
                    max_area = max(max_area, height * width)
                s.append(i)
            return max_area

        for row in matrix:
            for i in range(C):
                h[i] = h[i] + 1 if row[i] == "1" else 0
            res = max(res, maxRec(h))

        return res

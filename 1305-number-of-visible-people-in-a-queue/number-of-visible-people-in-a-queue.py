class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        h, n = heights, len(heights)
        res = [0] * n 
        s = [] #ms

        for i in range(n-1, -1, -1):
            v = 0
            while s and h[i] > s[-1]:
                v += 1
                s.pop()

            if s: v += 1
            res[i] = v
            s.append(h[i])
        
        return res
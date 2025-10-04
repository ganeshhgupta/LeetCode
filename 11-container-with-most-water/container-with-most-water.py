class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        h = height
        l, r = 0, len(h) - 1
        curr = maxx = 0
        while l < r:
            curr = min(h[l], h[r]) * (r - l)
            maxx = max(maxx, curr)
            if h[l] < h[r]:
                l += 1
            else:
                r -= 1
        return maxx

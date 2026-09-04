class Solution:
    def trap(self, height: List[int]) -> int:
        
        # O(n), O(1)
        
        # For any position i, the water above it is:
        # min(max height on left, max height on right) - height[i]

        if not height: 
            return 0

        n = len(height)
        l, r = 0, n-1
        res = 0
        lmax, rmax = height[l], height[r]

        while l < r:
            
            if lmax < rmax:
                l += 1
                lmax = max(lmax, height[l])
                res += lmax - height[l]
            else:
                r -= 1
                rmax = max(rmax, height[r])
                res += rmax - height[r]
        
        return res
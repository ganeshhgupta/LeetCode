class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # O(n⋅logm) m = max(piles), O(1)
        l, r = 1, max(piles)

        def canEat(k):
            c = 0
            for p in piles:
                c += ceil( p / k)
            
            return c <= h

        while l <= r:
            m = l + ( r - l) // 2

            k = m
            if canEat(k):
                r = m - 1
            else:
                l = m + 1

        return l
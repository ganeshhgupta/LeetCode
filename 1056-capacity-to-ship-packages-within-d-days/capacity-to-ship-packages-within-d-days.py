class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def carry(cap):
            total = 1
            curr = 0
            for w in weights:
                if curr + w > cap:
                    total += 1
                    curr = 0
                curr += w
            return total

        l, r = max(weights), sum(weights)
        
        while l <= r:
            m = (l + r) // 2
            if carry(m) <= days:
                r = m - 1
            else:
                l = m + 1
        
        return l

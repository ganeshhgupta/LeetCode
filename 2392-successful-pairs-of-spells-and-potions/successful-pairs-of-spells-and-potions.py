class Solution: 
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        # O(n log m), O(1)
        potions.sort()

        def min_i(s):
            l, r = 0, len(potions) - 1
            while l <= r:
                m = l + (r - l) // 2
                if s * potions[m] >= success:
                    r = m - 1
                else:
                    l = m + 1
            # l is first index where s * potions[l] >= success
            return len(potions) - l

        res = []
        for s in spells:
            res.append(min_i(s))
        return res

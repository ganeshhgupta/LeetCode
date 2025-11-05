class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # O(n), O(n)
        
        unq = set()
        l = res = 0

        for r in range(len(s)):

            while s[r] in unq:
                unq.remove(s[l])
                l += 1
            
            unq.add( s[r] )
            res = max(res, r - l + 1)
        
        return res
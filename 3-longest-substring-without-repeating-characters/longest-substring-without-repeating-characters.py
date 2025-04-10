class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        sset = set()
        l, r, maxx = 0, 0 , 0

        for r in range(len(s)):

            while s[r] in sset: #we use whlie and not if, to keep moving l pointer for as many duplicates we find of the same element
                sset.remove(s[l])
                l += 1
            sset.add(s[r])
            maxx = max(maxx, r-l +1)

        return maxx
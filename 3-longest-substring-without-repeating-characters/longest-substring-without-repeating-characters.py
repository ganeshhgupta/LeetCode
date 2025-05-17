class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        unique = set()
        l, maxx = 0, 0
        for r in range(len(s)):
            while s[r] in unique:
                unique.remove(s[l])
                l += 1
            unique.add(s[r])
            maxx = max(maxx, r - l + 1)
        return maxx
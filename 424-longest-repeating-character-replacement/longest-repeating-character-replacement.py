class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # O(n), O(1)
        c = defaultdict(int)
        l = r = res = 0
        maxf = 0

        while r < len(s):
            c[s[r]] += 1
            maxf = max(maxf, c[s[r]])

            while ( r- l + 1) - max(c.values()) > k:
                c[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
            r += 1
        return res
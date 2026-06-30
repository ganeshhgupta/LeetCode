class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        # O(n), O(1), two pointer sliding window
        
        n = len(s)
        count = { 'a': 0 , 'b': 0 , 'c': 0 }
        res = 0
        l = 0

        for r in range(n):

            count[s[r]] += 1

            while count['a'] and count['b'] and count['c']:
                res += n - r

                count[s[l]] -= 1
                l += 1
        
        return res
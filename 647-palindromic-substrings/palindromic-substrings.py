class Solution:
    def countSubstrings(self, s: str) -> int:
                    
        res = 0

        for i in range(len(s)):

            #At every index, expand checking across left and right
            #For odd, start with l, r on the same character
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

            #For even, start with l, r on the ith and i+1th character (easy tweak)
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        return res
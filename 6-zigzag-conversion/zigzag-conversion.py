class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        # O(n^2), 
        if numRows == 1: return s
        res = ""
        inc = 2 * (numRows - 1) # increment
        
        for r in range(numRows):
            for i in range(r, len(s), inc):
                res += s[i]
                if (0 < r < numRows - 1 and
                i + inc - 2 * r < len(s)):
                    res += s[i + inc - 2 * r]
        return res
class Solution:
    def checkValidString(self, s: str) -> bool:
        
        lmin, lmax = 0, 0

        for c in s:
            if c == '(':
                lmin, lmax = max(0, lmin + 1), lmax + 1
            elif c == ')':
                lmin, lmax = max(0, lmin - 1), lmax - 1
            else:
                lmin, lmax = max(0, lmin - 1), lmax + 1
            
            if lmax < 0:
                return False
        
        return lmin == 0
            
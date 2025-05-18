class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        
        m = {}

        def pal(i, j, k):
            if (i, j, k) in m:
                return m[(i, j, k)]
            
            while i < j:
                if s[i] != s[j]:
                    if k == 0:
                        m[(i, j, k)] = False
                        return False
                    m[(i, j, k)] = pal(i+1, j, k-1) or pal(i, j-1, k-1)
                    return m[(i, j, k)]
                i, j = i+1, j-1
            
            m[(i, j, k)] = True
            return True
        
        return pal(0, len(s)-1, k)
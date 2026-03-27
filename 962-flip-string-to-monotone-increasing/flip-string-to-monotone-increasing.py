class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        
        # O(n), O(n)
        n = len(s)
        
        # no. of ones to the left of i and no. of zeroes to the right of i
        ones_left = 0
        zeros_right = s.count('0')

        res = zeros_right # and not min(zero_right, n - zero_right) cause that's redudant, the loop will check that anyway

        for i in range(n):
            if s[i] == '0':
                zeros_right -= 1
            else:
                ones_left += 1
            
            res =  min(res, ones_left + zeros_right)
        
        return res
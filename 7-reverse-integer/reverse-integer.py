class Solution:
    def reverse(self, x: int) -> int:
        
        if x == 0:
            return 0
        
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        
        res = int(str(x)[::-1])
        
        res *= sign
        
        if res < -2**31 or res > 2**31 - 1:
            return 0
        
        return res

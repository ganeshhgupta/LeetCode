class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        # O((log(a/b))2), O(1)
        # youtube.com/watch?v=xefkgtd44hg

        if dividend == 0: return 0
        
        a, b = abs(dividend), abs(divisor)
        sign = (dividend//a) * (divisor//b)
        res = 0

        while a >= b:
            c, d = 1, b # counter and decrement

            while a >= d:
                a -= d

                res += c
                c += c
                d += d
        
        res = res * sign
        return min( max( -2**31, res), 2**31 - 1)


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        if divisor == 0:
            return -1

        if dividend == divisor:
            return 1
        if dividend == -2**31 and divisor == -1:
            return (2**31) - 1 
        
        if divisor == 1:
            return dividend

        q = 0
        sign = ( abs(divisor)//divisor )
        if dividend != 0:
            sign *= ( abs(dividend)//dividend ) 

        divisor, dividend = abs(divisor), abs(dividend)
        while dividend >= divisor:
            temp = divisor
            mul = 1
            while dividend >= temp:
                dividend -= temp
                q += mul
                temp += temp
                mul *= 2
        print(q * sign)
        print(2**31)
        #return q*sign
        return min (2**31, max(- 2**31,  q * sign))
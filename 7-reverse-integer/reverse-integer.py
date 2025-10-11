class Solution:
    def reverse(self, x: int) -> int:
        
        # O(n), O(n)
        MAX, MIN =  (2 ** 31) -1  , (2 ** 31) * -1 
        sign = -1 if x < 0 else 1

        x = list (str( abs(x) ))
        x = x[::-1]
        
        i = 0
        while i < len(x) and x[i] == '0':
            i += 1
        
        x = x[i:]
        if x == []: return 0
        x = int("".join(x)) * sign

        return x if MIN <= x <= MAX else 0




    
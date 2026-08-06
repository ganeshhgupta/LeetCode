class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        while True:

            li = list(str(n)) 

            ans = 1
            for i in li:
                ans *= int(i)
            
            if ans % t == 0:
                return n
            
            n += 1
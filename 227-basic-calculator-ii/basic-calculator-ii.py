class Solution:
    def calculate(self, s: str) -> int:

        curr = prev = res = 0 # prev holds sec last seen no. ; curr holds last seen no.
        op = '+' # holds last seen operator
        s += '+'

        for ch in s:

            if ch in '1234567890':
                curr = curr * 10 + int(ch)
            
            elif ch in '+-*/': 
                
                if op == '+':
                    res += prev
                    prev = curr
                
                if op == '-':
                    res += prev
                    prev = -curr
                
                if op == '*':
                    prev *= curr
                
                if op == '/':
                    prev = int(prev/curr) #truncate to int
            
                op = ch # load next operator
                curr = 0 # empty curr
            
        res += prev
        return res
        


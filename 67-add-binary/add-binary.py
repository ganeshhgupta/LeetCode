class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        res = ""
        carry = 0

        a, b = a[::-1], b[::-1] #reversing

        for i in range(max(len(a), len(b))):
             
             A = int(a[i]) if i < len(a) else 0
             B = int(b[i]) if i < len(b) else 0

             total = A + B + carry
             res += str( total % 2)
             carry = total // 2

        if carry:
            res += "1"

        return res[::-1]
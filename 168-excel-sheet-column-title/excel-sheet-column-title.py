class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber > 0:
            columnNumber -= 1  
            res.append(chr(columnNumber % 26 + 65))  
            columnNumber //= 26  
        
        return "".join(res[::-1]) 

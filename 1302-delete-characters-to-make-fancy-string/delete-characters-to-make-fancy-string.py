class Solution:
    def makeFancyString(self, s: str) -> str:
        res = [s[0]]
        
        for i in range(1, len(s)):
            if len(res) >= 2 and res[-1] == res[-2] == s[i]:
                continue
            res.append(s[i])        
        return "".join(res)

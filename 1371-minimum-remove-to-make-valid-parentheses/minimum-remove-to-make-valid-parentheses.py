class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        res = []
        c = 0

        for i in s:
            if i == '(':
                c += 1
                res.append(i)
            elif i == ')' and c > 0:
                c -= 1
                res.append(i)
            elif i != ')' :
                res.append(i)

        res[:] = res[::-1]
        ans = []
        for i in res:
            if i == '(' and c > 0:
                c -= 1
            else:
                ans.append(i)
        
        return "".join(ans[::-1])
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        res = []
        li = []
        s = s.lower()

        def dfs(i):
            
            if i == len(s):
                res.append("".join(li.copy()))
                return

            if s[i].isalpha():
                li.append(s[i].upper())
                dfs(i+1)
                li.pop()

            li.append(s[i])
            dfs(i+1)
            li.pop()

        dfs(0)
        return res

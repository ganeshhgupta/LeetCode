class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        res = []

        #girl are you backtracking, cause idk when to pop out
        def dfs(i, li):
            
            if i == len(s):
                res.append("".join(li))
                return
            else:
                if s[i].isalpha():
                    li.append(s[i].upper())
                    dfs(i+1, li)
                    li.pop()
                    li.append(s[i].lower())
                    dfs(i+1, li)
                    li.pop()

                else:
                    li.append(s[i])
                    dfs(i+1, li)
                    li.pop()

        dfs(0, [])
        return res

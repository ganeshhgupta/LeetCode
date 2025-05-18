class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        st = []

        def dfs(o, c):
            if o == c == n:
                res.append("".join(st))
                return 
            if o < n:
                st.append('(')
                dfs(o+1, c)
                st.pop()
            if c < o:
                st.append(')')
                dfs(o, c+1)
                st.pop()
        dfs(0, 0)
        return res
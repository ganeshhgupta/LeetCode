class Solution:
    def isValid(self, s: str) -> bool:
        
        par = { ')':'(' , '}':'{', ']':'['}
        st = []

        for i in s:
            if i in par and st and st[-1] == par[i]:
                st.pop()
            else:
                st.append(i)
        
        return len(st) == 0
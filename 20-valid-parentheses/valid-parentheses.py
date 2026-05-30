class Solution:
    def isValid(self, s: str) -> bool:
        
        par = {
            ')':'(', '}':'{', ']':'['
        }
        st = []

        for i in s:
            if i not in par:
                st.append(i)
            else:
                if st and st[-1] == par[i]:
                    st.pop()
                else:
                    return False
    
        return len(st) == 0

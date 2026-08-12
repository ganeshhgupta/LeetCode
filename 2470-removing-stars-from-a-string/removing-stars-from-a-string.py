class Solution:
    def removeStars(self, s: str) -> str:
        
        st = []

        for c in s:

            if st and st[-1].isalpha() and c == '*':
                st.pop()
            
            else:
                st.append(c)
        
        return "".join(st)
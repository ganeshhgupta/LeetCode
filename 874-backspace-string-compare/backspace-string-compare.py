class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def build(string):
            st = []
            
            for c in string:
                if c == '#':
                    if st:
                        st.pop()
                else:
                    st.append(c)
            return st
        
        return build(s) == build(t)
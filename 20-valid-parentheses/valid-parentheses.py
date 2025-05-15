class Solution:
    def isValid(self, s: str) -> bool:
        
        st = []
        map = {')':'(' , '}':'{' , ']':'['}

        for i in s:
            if i in map:
                if st and st[-1] == map[i]:
                    st.pop()
                else:
                    return False
            else:
                st.append(i)
        
        return True if not st else False
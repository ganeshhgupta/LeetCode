class Solution:
    def simplifyPath(self, path: str) -> str:
        
        # O(n), O(n)
        
        st = []
        path = path.split('/')

        for p in path:
            if p == '' or p == '.':
                continue
            
            elif p == '..':
                if st:
                    st.pop()
            
            else:
                st.append(p)
        
        return "/" + "/".join(st)
            
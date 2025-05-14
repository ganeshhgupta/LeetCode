class Solution:
    def simplifyPath(self, path: str) -> str:

        li = path.split('/')
        st = []
        for i in li:
            if i == '' or i == '.':
                continue
            elif i == "..":
                if st:
                    st.pop()
            else:
                st.append(i)

        return "/" + "/".join(st)
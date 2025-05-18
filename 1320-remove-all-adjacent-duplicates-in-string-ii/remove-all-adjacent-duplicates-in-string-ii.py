class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        st = []
        for c in s:
            if st and st[-1][0] == c:
                st[-1][1] += 1
                if st[-1][1] == k:
                    st.pop()
            else:
                st.append([c, 1])
        
        res = []
        for i, j in st:
            res.append(i*int(j))
        return ''.join(res)
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if not s:
            return None

        st = []
        i = 0

        def toNum(i):
            negative = False
            if s[i] == '-':
                negative = True
                i += 1
            num = 0
            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i]) 
                i += 1
            return (-num if negative else num), i - 1

        while i < len(s):
            c = s[i]
            if c == '-' or c.isdigit():
                num, i = toNum(i)
                st.append(TreeNode(num))
            elif c == ')':
                top = st.pop()
                if not st[-1].left:
                    st[-1].left = top
                else:
                    st[-1].right = top
            i += 1

        return st[-1] if st else None
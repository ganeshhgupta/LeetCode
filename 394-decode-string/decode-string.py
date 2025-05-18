class Solution:
    def decodeString(self, s: str) -> str:

        st = []
        for i in s:
            if i != ']':
                st.append(i)
            else:
                substr = ""
                while st[-1] != '[':
                    substr = st.pop() + substr
                st.pop()  # remove the '['

                k = ''
                while st and st[-1].isdigit():
                    k = st.pop() + k

                st.append(int(k) * substr)
        return ''.join(st)

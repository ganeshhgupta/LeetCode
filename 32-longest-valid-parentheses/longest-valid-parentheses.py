class Solution:
    def longestValidParentheses(self, s: str) -> int:

        # O(n), O(n)
        
        st = [-1]
        res = 0

        for i in range(len(s)):
            if s[i] == '(':
                st.append(i)
            else:
                st.pop()
                if not st:
                    st.append(i)
                else:
                    res = max(res, i - st[-1])
        
        return res
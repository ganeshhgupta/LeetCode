class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        # O(n), O(n), MS 
        
        st = []

        for ch in s:

            if ch == ')':
                sub = ''
                while st and st[-1] != '(':
                    sub += st.pop()
                
                st.pop()
                st.extend(sub)
            
            else:
                st.append(ch)

        return ''.join(st)

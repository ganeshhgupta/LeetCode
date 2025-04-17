class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        stack = []
        for i in s:
            stack.append(i)
            if len(stack) >= 2:
                if stack[-2] == '(' and stack[-1] == ')':
                    stack.pop()
                    stack.pop()

        return len(stack)
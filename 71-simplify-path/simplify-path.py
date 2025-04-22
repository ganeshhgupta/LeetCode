class Solution:
    def simplifyPath(self, path: str) -> str:
        li = path.split('/')
        stack = []
        
        for i in li:
            if i == '' or i == '.':
                continue
            elif i == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        
        return  '/' + '/'.join(stack)
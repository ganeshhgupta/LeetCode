# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if not s:
            return None

        stack = []
        i = 0

        def toNum(i): #extract no. from string of digits
            sign = 1

            if s[i] == '-':
                sign = -1
                i += 1

            num = 0
            while i < len(s) and s[i].isdigit():
                num = 10 * num + int(s[i])
                i += 1

            return sign * num, i - 1

        while i < len(s):

            if s[i] == '-' or s[i].isdigit(): #add to stack

                num, i = toNum(i)
                stack.append(TreeNode(num))

            elif s[i] == ')': #if ')' digit is l/r child of prev no. in stack

                child = stack.pop()
                parent = stack[-1]

                if not parent.left:
                    parent.left = child
                else:
                    parent.right = child

            i += 1

        return stack[0]

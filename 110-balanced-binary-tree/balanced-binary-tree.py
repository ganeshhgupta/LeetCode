# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # O(n), O(h)
        
        self.res = True

        def dfs(n, curr):

            if not n:
                return 0
            
            left = 1 + dfs(n.left, curr)
            right = 1 + dfs(n.right, curr)

            if abs(left - right) > 1:
                self.res = False

            return max(left, right)
        
        dfs(root, 0)
        return self.res

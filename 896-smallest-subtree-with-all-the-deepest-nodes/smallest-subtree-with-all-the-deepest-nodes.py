# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # O(n), O(n)
        # return (LCA, height) https://www.youtube.com/watch?v=bMXHK-ASQV0
        # LCA with most height keeps bubbling up, but height keeps getting +1 at every step.

        def dfs(n):
            if not n: 
                return (None, 0)
            
            left_n, left_h = dfs(n.left)
            right_n, right_h = dfs(n.right)

            if left_h == right_h:
                return n, 1 + left_h

            elif left_h > right_h:
                return left_n, 1 + left_h
            
            else:
                return right_n, 1 + right_h
        
        node, _ = dfs(root)
        return node
        

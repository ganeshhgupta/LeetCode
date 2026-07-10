# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        self.res = []

        def dfs(n):

            if not n: 
                return
            
            dfs(n.left)
            self.res.append(n.val)
            dfs(n.right)

        dfs(root)
        return self.res

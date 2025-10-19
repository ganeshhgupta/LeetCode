# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        # O(N), O(N)
        
        res = []
        li = []

        def dfs(n):
            nonlocal li

            if not n:
                return

            li.append(str(n.val))
            if not ( n.left or n.right ):
                res.append( "->".join(li.copy()) )
            
            dfs(n.left)
            dfs(n.right)

            li.pop()

            return 

        dfs(root)
        return res

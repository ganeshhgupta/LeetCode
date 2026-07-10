# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        self.res = []

        def dfs(n, li, curr):

            if not n:
                return

            li = li + [n.val]
            curr += n.val

            if not n.left and not n.right:
                if curr == targetSum:
                    self.res.append(tuple(li))
                return
            
            dfs(n.left, li, curr)
            dfs(n.right, li, curr)
        
        dfs(root, [], 0)
        return self.res
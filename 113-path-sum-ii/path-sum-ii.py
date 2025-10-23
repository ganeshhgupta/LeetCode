# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        res = []
        def dfs(n, li, cur):

            if not n: return

            if not n.left and not n.right:
                if cur + n.val == targetSum:
                    res.append(li + [n.val])
                    return
            
            dfs(n.left, li + [n.val], cur + n.val)
            dfs(n.right, li + [n.val], cur + n.val)
        
        dfs(root, [], 0)
        return res



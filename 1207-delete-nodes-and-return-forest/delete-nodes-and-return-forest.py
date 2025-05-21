# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        res_set = set([root])
        del_set = set(to_delete)

        def dfs(n):
            if not n:
                return
            
            res = n
            if n.val in del_set:
                res = None
                res_set.discard(n)
                if n.left: res_set.add(n.left)
                if n.right: res_set.add(n.right)

            n.left = dfs(n.left)
            n.right = dfs(n.right)

            return res
        dfs(root)
        return res_set
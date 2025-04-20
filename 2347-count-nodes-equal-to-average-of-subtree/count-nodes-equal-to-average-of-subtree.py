# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        
        self.res = 0

        def dfs(node):

            if not node:
                return (0, 0)
            
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            sum = left_sum + node.val + right_sum
            count = left_count + 1 + right_count

            if sum//count == node.val:
                self.res += 1
            
            return (sum, count)

        dfs(root)
        return self.res


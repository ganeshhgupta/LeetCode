# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        max_val = float('-inf')
        q = deque([root])
        res, level = 1, 0
        
        while q:
            total = 0
            level += 1

            for i in range(len(q)):

                node = q.popleft()
                total += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            if total > max_val:
                max_val = total
                res = level

        return res
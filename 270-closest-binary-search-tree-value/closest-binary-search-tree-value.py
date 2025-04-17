# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        self.closest = root.val 

        def dfs(node):
            if not node:
                return
            
            #if abs(target - node.val) == abs(target - self.closest):
            #    self.closest = min( self.closest , node.val)
            print( node.val,abs(target - node.val) , abs(target - self.closest))

            if abs(target - node.val) == abs(target - self.closest):
                self.closest = min(node.val, self.closest)

            elif abs(target - node.val) < abs(target - self.closest):
                self.closest = node.val
                print(self.closest)

            if node.val > target:
                dfs(node.left)
            else:
                dfs(node.right)

        dfs(root)
        return self.closest
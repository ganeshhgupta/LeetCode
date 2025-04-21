class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def depth(root):

            if root is None:
                return 0

            left = depth(root.left)
            right = depth(root.right)

            if abs(left - right) > 1:
                return -1

            if left == -1 or right == -1:
                return -1

            return 1 + max(left, right)

        return depth(root) != -1

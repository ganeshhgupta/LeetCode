class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def diff(root):

            if root is None:
                return 0

            left = diff(root.left)
            right = diff(root.right)

            if abs(left - right) > 1:
                return -1

            if left == -1 or right == -1:
                return -1

            return 1 + max(left, right)

        return diff(root) != -1

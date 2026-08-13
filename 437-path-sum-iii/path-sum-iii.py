class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        self.count = 0

        def dfs(n, curr):
            if not n:
                return

            curr += n.val

            if curr == targetSum:
                self.count += 1

            dfs(n.left, curr)
            dfs(n.right, curr)

        def start(n):
            if not n:
                return

            dfs(n, 0)          # start path here
            start(n.left)
            start(n.right)

        start(root)

        return self.count
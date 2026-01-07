class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        ans = 0

        def sumTree(node):
            if not node:
                return 0
            return node.val + sumTree(node.left) + sumTree(node.right)

        total = sumTree(root)

        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            ans = max(ans, s * (total - s))
            return s

        dfs(root)
        return ans % MOD

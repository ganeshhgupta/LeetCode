class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:

        self.res = 0

        def dfs(n):
            if not n:
                return (0 ,0)
            
            ls, lc = dfs(n.left)
            rs, rc = dfs(n.right)

            sum = ls + n.val + rs
            c = lc + 1 + rc

            if sum // c == n.val:
                self.res += 1
                
            return (sum, c)
        
        dfs(root)
        return self.res
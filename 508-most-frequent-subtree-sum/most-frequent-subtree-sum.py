class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        
        # O(n), O(n)
        sum_count = defaultdict(int)

        def dfs(n):
            if not n: return 0

            
            curr = dfs(n.left) + n.val + dfs(n.right)

            sum_count[curr] += 1

            return curr
        
        dfs(root)
        
        res = max(sum_count.values())
        return [s for s, freq in sum_count.items() if freq == res]
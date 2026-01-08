class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        # 2D-DP O(n^2), O(n^2)
        
        n, m = len(nums1), len(nums2)
        NEG_INF = -10**9
        
        dp = [[NEG_INF] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                prod = nums1[i] * nums2[j]
                
                take = prod
                if i > 0 and j > 0:
                    take = max(take, prod + dp[i-1][j-1])
                
                skip1 = dp[i-1][j] if i > 0 else NEG_INF
                skip2 = dp[i][j-1] if j > 0 else NEG_INF
                
                dp[i][j] = max(take, skip1, skip2)
        
        return dp[n-1][m-1]

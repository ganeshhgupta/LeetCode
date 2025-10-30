class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        # O(n), O(n)
        
        n = len(ratings)
        dp = [1] * n

        for i in range(1, n):
            if ratings[i-1] < ratings[i]:
                dp[i] = dp[i-1] + 1

        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                dp[i] = max( dp[i], dp[i+1] + 1 )
                # in cases where both left and right slopes apply (like a mountain), 
                # we need to keep the maximum of both directions, not just overwrite.
        
        return sum(dp)
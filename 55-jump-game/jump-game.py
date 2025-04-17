class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums) - 1
        dp = [False] * (n + 1)
        dp[n] = True
        last_true = n

        for i in range(len(nums) - 2, -1, -1, ):
            if nums[i] >= last_true - i:
                dp[i] = True
                last_true = i
        
        return dp[0]
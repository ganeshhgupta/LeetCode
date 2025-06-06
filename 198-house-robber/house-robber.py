class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)

        if n < 2:
            return nums[0]

        if n == 2:
            return max(nums[0], nums[1])

        #Recurrecnce relation: Max loot at i = max( Max loot till i-2 + Loot at i , Max loot till i-1)

        dp = [0]*n 
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max( dp[i-2] + nums[i], dp[i-1])

        return dp[n-1]

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 2:
            return nums[0]

        if n == 2:
            return max(nums[0], nums[1])

        if n == 3:
            return max(nums[0], nums[1], nums[2])

        #Recurrecnce relation: Max loot at i = max( Max loot till i-2 + Loot at i , Max loot till i-1)

        def rob_1(nums):
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            
            for i in range(2, len(nums)):
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
            
            return dp[-1]

        # Case 1: Include the first house and exclude the last house
        max1 = rob_1(nums[:-1])

        # Case 2: Exclude the first house and include the last house
        max2 = rob_1(nums[1:])

        return max(max1, max2)
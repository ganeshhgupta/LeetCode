class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = {} 
        n = len(nums)
        def dfs(i, val):

            if i == n:
                return 1 if val == target else 0

            if (i, val) in dp:
                return dp[(i, val)]

            dp[(i, val)] = ( dfs(i + 1, val  - nums[i]) + dfs(i + 1, val  + nums[i]) )

            return dp[(i, val)]

        return dfs(0, 0)
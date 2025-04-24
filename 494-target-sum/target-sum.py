class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
       
        dp = {}
        def dfs(i, sum):
            if i == len(nums):
                if sum == target:
                    return 1
                else:
                    return 0 
            
            if (i, sum) in dp:
                return dp[(i ,sum)]

            dp[(i, sum)] = dfs( i + 1, sum + nums[i]) + dfs( i + 1, sum - nums [i] )

            
            return dp[(i, sum)]
        return dfs(0, 0)
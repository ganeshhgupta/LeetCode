class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = {} 
        n = len(nums)
        def dfs(i, val):

            #if array ends, check if sum == target, ret 1
            if i == n:
                return 1 if val == target else 0

            #if (i, val) combo already in dp, return answer already
            if (i, val) in dp:
                return dp[(i, val)]

            #all possible valid sign combinations from (i,val):
            dp[(i, val)] = ( dfs(i + 1, val  - nums[i]) + dfs(i + 1, val  + nums[i]) )

            return dp[(i, val)]

        res = dfs(0, 0)
        print(dp)
        return res
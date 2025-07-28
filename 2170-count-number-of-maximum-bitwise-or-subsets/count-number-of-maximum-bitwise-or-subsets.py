class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:

        maxx = 0
        for num in nums:
            maxx |= num
        
        def dfs(i, curr):
            if i == len(nums):
                return 1 if curr == maxx else 0
                
            return dfs(i+1, curr | nums[i]) + dfs(i+1, curr)
        
        return dfs(0, 0)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr, maxx = nums[0], nums[0]
        for i in range(1, len(nums)):
            curr = max(nums[i], curr + nums[i])
            maxx = max(maxx, curr)
        return maxx
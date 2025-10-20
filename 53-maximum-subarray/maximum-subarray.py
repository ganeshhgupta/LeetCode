class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # O(n), O(1)
        
        curr = res = nums[0]

        for i in range(1, len(nums)):
            curr = max( nums[i], curr + nums[i] )
            res = max(res, curr)
            #print(i, nums[i], curr, res)
        
        return res
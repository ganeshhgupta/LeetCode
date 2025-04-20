class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        
        for i in range(len(nums) - 1):
            if ( nums[i] + nums[i+1] ) % 2 != 1:
                return False
        return True
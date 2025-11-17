class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        for i in range(len(nums) - k + 1):
            #print(nums[i:i + k + 1])
            if sum(nums[i:i + k + 1]) > 1:
                return False
        
        return True
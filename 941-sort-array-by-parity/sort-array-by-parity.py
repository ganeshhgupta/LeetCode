class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        prev = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i], nums[prev] = nums[prev], nums[i]
                prev += 1
        
        return nums
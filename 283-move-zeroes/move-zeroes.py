class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last], nums[i] = nums[i], nums[last]
                last += 1
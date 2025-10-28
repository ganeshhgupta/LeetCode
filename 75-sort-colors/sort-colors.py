class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # O(n), O(1), easy peasy 
        
        zeros = ones = 0

        for i in nums:
            if i == 0:
                zeros += 1
            elif i == 1:
                ones += 1
        
        i = 0
        while i < len(nums):
            if zeros > 0:
                nums[i] = 0
                zeros -= 1
            elif ones > 0: 
                nums[i] = 1
                ones -= 1
            else:
                nums[i] = 2
            i += 1

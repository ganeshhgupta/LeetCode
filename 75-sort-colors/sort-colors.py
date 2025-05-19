class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        l, i, r = 0, 0, len(nums) - 1
        
        while i < r + 1:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
            i += 1
        i = r
        while i >= l:
            if nums[i] == 2:
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
            i -= 1
        return nums
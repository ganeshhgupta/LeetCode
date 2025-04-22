class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        left, i, right = 0, 0, len(nums) - 1

        #bubble all 0s to left, 2s to right
        while i <= right:
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            else:  # nums[i] == 1
                i += 1

    #Why no i += 1 after swapping with right?
    #Because you don't know what nums[i] is after the swap — it could be a 0 or 2 that still needs to be sorted.
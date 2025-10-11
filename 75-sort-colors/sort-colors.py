class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # O(n), O(1) Dutch National Flag algorithm
        i, l, r = 0, 0, len(nums) - 1

        while i <= r:

            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                i += 1
                l += 1

            elif nums[i] == 1:
                i += 1

            else:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1


        
        
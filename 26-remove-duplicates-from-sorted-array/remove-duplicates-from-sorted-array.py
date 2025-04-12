class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]: #[1, 1, 2] when nums[0] 
                nums[j] = nums[i]
                j += 1
        return j

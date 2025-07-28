class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        res = 0
        i, j = 1, 0
        while i < len(nums) - 1:

            if nums[i] == nums[i+1]:
                i += 1
                continue

            if nums[j] < nums[i] > nums[i+1] or nums[j] > nums[i] < nums[i+1]:
                res += 1
                j = i
                i += 1
            else:
                j = i
                i += 1

        return res

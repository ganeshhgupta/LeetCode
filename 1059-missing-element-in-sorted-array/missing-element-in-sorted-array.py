class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        for i in range(len(nums) - 1):
            # missing numbers between nums[i] and nums[i+1]
            diff = nums[i + 1] - nums[i] - 1
            if diff >= k:
                return nums[i] + k
            k -= diff
        return nums[-1] + k

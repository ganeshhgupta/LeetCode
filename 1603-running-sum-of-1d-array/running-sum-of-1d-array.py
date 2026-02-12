class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            res.append(total)
        return res
from typing import List

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        res = []
        
        if not nums:
            return [[lower, upper]]
        
        if nums[0] > lower:
            res.append([lower, nums[0] - 1])
        
        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i] + 1:
                res.append([nums[i] + 1, nums[i + 1] - 1])
        
        if nums[-1] < upper:
            res.append([nums[-1] + 1, upper])
        
        return res

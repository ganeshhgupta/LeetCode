class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        
        return min(max(nums.index(min(nums)), nums.index(max(nums))) + 1, len(nums) - min(nums.index(min(nums)), nums.index(max(nums))), min(nums.index(min(nums)), nums.index(max(nums))) + 1 + len(nums) - max(nums.index(min(nums)), nums.index(max(nums))))


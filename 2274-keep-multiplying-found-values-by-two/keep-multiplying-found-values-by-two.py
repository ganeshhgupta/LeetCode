class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        nums = set(nums)
        n = original

        while n in nums:
            nums.remove(n)
            n *= 2
        
        return n
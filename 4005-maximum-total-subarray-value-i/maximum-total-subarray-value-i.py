class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        
        # O(n), O(1)
        return ( max(nums) - min(nums)) * k
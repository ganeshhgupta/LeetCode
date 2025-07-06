from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        
        def is_distinct(arr):
            return len(set(arr)) == len(arr)
        
        for removed in range(0, n + 3, 3):
            if removed > n:
                return removed // 3
            if is_distinct(nums[removed:]):
                return removed // 3
        
        return n // 3

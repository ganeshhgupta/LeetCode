class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        
        # O(n), O(1)
        if not nums:
            return 0
            
        nums.sort()
        count = 0
        prev = nums[0] - k - 1 
        
        for num in nums:
            x = max(prev + 1, num - k)
            
            if x <= num + k:
                count += 1
                prev = x
                
        return count
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        nums = list(set(nums))
        
        if len(nums) < 3:
            return max(nums)
        
        nums = [-num for num in nums]
        heapq.heapify(nums)
        
        heapq.heappop(nums)
        heapq.heappop(nums)
        
        return -heapq.heappop(nums)

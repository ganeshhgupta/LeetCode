from sortedcontainers import SortedList

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        c = 0
        s_nums = SortedList(nums)
        
        while s_nums[0] < k and len(s_nums) > 1:   
            c += 1 
            s_nums.add((s_nums[0] * 2) + s_nums[1])
            s_nums.pop(0)
            s_nums.pop(0)
        
        return c

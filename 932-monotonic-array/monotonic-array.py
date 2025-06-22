class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        id = 0
        while id + 1 < len(nums) and nums[id] == nums[id+1]:
            id += 1
        
        if id == len(nums) - 1:
            return True
        
        if nums[id] <= nums[id+1]:
            for i in range(id, len(nums) - 1):
                if nums[i] > nums[i+1]:
                    return False
        else:
            for i in range(id, len(nums) - 1):
                if nums[i] < nums[i+1]:
                    return False
        
        return True

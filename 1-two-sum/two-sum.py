class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        map = {}
        for i in range(len(nums)):
            c = target - nums[i]
            
            if c in map:
                return [map[c], i]
            else:
                map[nums[i]] = i

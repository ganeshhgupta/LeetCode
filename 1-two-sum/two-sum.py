class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # O(n), O(n)
        map = defaultdict(int) # merely store the indices

        for i in range(len(nums)):

            c = target - nums[i]
            if c in map:
                return [i, map[c]]
            else:
                map[nums[i]] = i
        
        return [-1, -1]
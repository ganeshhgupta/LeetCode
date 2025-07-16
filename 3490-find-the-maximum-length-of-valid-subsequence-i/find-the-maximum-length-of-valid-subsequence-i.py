class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 2: return 2
        z = nums[0] & 1
        Len = [1 - z, z, 1]
        
        for num in nums[1:]:
            p = num & 1
            Len[p & 1] += 1
            if p != z:
                Len[2] += 1
                z = 1 - z
        
        return max(Len)

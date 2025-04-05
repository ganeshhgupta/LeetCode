class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        xor_sum = 0        
        n = len(nums)
        
        for i in range(1 << n):
            current_xor = 0
            for j in range(n):
                if i & (1 << j):
                    current_xor ^= nums[j]
            xor_sum += current_xor
        
        return xor_sum

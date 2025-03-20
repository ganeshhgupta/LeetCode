class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        i, n, c = 0, len(nums), 0

        while i < n - 2:
            if nums[i] == 0:
                nums[i] ^= 1
                nums[i+1] ^= 1
                nums[i+2] ^= 1
                c += 1
            i += 1
        print(nums)
        if nums[-1] == 0 or nums[-2] == 0:
            return -1
        return c
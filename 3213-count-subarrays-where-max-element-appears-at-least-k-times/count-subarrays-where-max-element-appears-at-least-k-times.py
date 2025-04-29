class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        m = max(nums)
        n = len(nums)
        res = 0
        c = 0
        l = 0
        
        for r in range(n):
            if nums[r] == m:
                c += 1
            while c >= k:
                res += n - r
                if nums[l] == m:
                    c -= 1
                l += 1
        return res

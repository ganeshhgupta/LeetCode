class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        # O(n), O(n)

        total = sum(nums)
        if total % p == 0:
            return 0
        
        k = total % p

        # prefix sum mod p
        pre = {0: -1}
        curr = 0
        res = len(nums)

        for i, n in enumerate(nums):

            curr = (curr + n) % p
            diff = (curr - k) % p
            
            if diff in pre:
                res = min(res, i - pre[diff])
            
            pre[curr] = i
        
        return res if res != len(nums) else -1

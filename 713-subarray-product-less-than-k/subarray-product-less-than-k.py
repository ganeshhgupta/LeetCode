class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        # kadane's prod variation, O(n), O(1)

        if k <= 1:
            return 0

        res = 0
        curr = 1
        l = 0
        r = 0

        while r < len(nums):
            curr *= nums[r]

            while curr >= k and l <= r:
                curr //= nums[l]
                l += 1

            res += r - l + 1

            r += 1

        return res

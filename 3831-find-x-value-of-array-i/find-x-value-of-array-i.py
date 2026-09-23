class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:

        # O(n), O(n) mix of  Subarray Sum Divisible by K and DP
        
        ans = [0] * k
        pre = [0] * k

        for n in nums:
            n %= k
            curr = [0] * k

            # Subarray consisting only of nums[i]
            curr[n] += 1

            # Extend every subarray ending at i - 1
            for r in range(k):
                curr[(r * n) % k] += pre[r]

            # Count all subarrays ending at i
            for r in range(k):
                ans[r] += curr[r]

            pre = curr

        return ans

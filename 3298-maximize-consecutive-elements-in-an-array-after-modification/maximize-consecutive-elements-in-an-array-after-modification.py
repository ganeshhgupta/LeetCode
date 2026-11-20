class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:

        # O(nlogn), O(n)

        # Sort nums.
        # dp[n] stores the longest consecutive sequence ending at n.
        # Either keep n (extend dp[n-1]) or increment n (extend dp[n]).
        # Track the maximum length across both choices.

        nums.sort()
        dp = [0] * (max(nums) + 2)

        res = 0

        for n in nums:
            dp[n + 1] = dp[n] + 1
            dp[n] = dp[n - 1] + 1

            res = max(res, dp[n], dp[n + 1])

        return res
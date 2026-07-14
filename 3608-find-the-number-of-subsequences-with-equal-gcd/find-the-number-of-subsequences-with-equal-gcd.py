class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:

        # O(n * M^2 * log M), O(n * M^2)
        # tree dp 
        
        MOD = 10**9 + 7
        memo = {}

        def dp(i, gcd1, gcd2):
            if i == len(nums):
                return 1 if gcd1 == gcd2 else 0

            if (i, gcd1, gcd2) in memo:
                return memo[(i, gcd1, gcd2)]

            curr = 0

            curr += dp(i + 1, gcd1, gcd2)                 # Don't select nums[i], i moves forward
            curr += dp(i + 1, gcd(gcd1, nums[i]), gcd2)   # Put nums[i] in first subsequence
            curr += dp(i + 1, gcd1, gcd(gcd2, nums[i]))   # Put nums[i] in second subsequence


            memo[(i, gcd1, gcd2)] = curr % MOD
            return memo[(i, gcd1, gcd2)]

        return (dp(0, 0, 0) - 1) % MOD
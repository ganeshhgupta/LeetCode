class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        # O(n), O(n)
        count = 0

        left = Counter() # numbers to the left of target
        right = Counter(nums) # numbers to the left of target

        for j in nums:
            target = j * 2

            right[j] -= 1 # since j is mid now

            count = (count + left[target] * right[target]) % MOD

            left[j] += 1

        return count
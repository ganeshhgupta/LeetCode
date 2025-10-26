class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:

        # O(n), O(1) Kadane's variation

        even, odd = 0, 0  # even = add, odd = subtract
        for num in nums:
            even = max(even, odd + num) # even -> stores max sum uptill last even index
            odd = max(odd, even - num) # odd -> stores max sum uptill last odd index
        return even

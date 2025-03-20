class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        i, n = 0, len(nums)
        max_count = 0
        bit_mask = 0  # To track the OR of elements in the window

        for j in range(n):

            while (bit_mask & nums[j]) != 0:
                bit_mask ^= nums[i]  # Remove nums[i] from the set
                i += 1  # Move left pointer forward
            
            # Add nums[j] to the bitwise OR tracking
            bit_mask |= nums[j]
            
            # Update max_count with current window length
            max_count = max(max_count, j - i + 1)

        return max_count

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # O(N), O(1)
        ones = 0  # bits seen once
        twos = 0  # bits seen twice
        
        for n in nums:
            ones = (ones ^ n) & ~twos # ~ : BITWISE NOT operator , ^ : BITWISE XOR operator
            twos = (twos ^ n) & ~ones
            
        return ones

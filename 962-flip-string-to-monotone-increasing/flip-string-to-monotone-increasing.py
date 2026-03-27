class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        
        # O(n), O(n)
        n = len(s)
        
        # Count 1s from the left (ones that need to become 0s)
        ones_left = 0
        # Count 0s from the right (zeros that need to become 1s)
        zeros_right = s.count('0')
        
        min_flips = zeros_right  # Case: entire string becomes all 1s
        
        for i in range(n):
            if s[i] == '0':
                zeros_right -= 1  # This 0 is now on the left, no longer needs flipping
            else:
                ones_left += 1    # This 1 is on the left, needs to be flipped to 0
            
            min_flips = min(min_flips, ones_left + zeros_right)
        
        return min_flips
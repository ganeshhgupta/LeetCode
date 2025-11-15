class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        
        # Find all zero positions
        zeros = [i for i in range(n) if s[i] == '0']
        total_zeros = len(zeros)
        
        count = 0
        
        # The key insight: zeros² <= ones, so zeros <= sqrt(ones) <= sqrt(n)
        # We iterate over all possible numbers of zeros (at most sqrt(n))
        max_zeros = int(n ** 0.5) + 2
        
        for num_zeros in range(min(max_zeros, total_zeros + 1)):
            if num_zeros == 0:
                # Handle substrings with no zeros (all ones)
                i = 0
                while i < n:
                    if s[i] == '1':
                        j = i
                        while j < n and s[j] == '1':
                            j += 1
                        length = j - i
                        # All substrings in this segment are valid
                        count += length * (length + 1) // 2
                        i = j
                    else:
                        i += 1
            else:
                # For each sliding window containing exactly num_zeros zeros
                for start_idx in range(total_zeros - num_zeros + 1):
                    end_idx = start_idx + num_zeros - 1
                    
                    # Position of leftmost and rightmost zero in this window
                    left_zero = zeros[start_idx]
                    right_zero = zeros[end_idx]
                    
                    # Determine boundaries for substring start and end positions
                    # Start position can extend left to just after previous zero
                    left_boundary = 0 if start_idx == 0 else zeros[start_idx - 1] + 1
                    
                    # End position can extend right to just before next zero
                    right_boundary = n - 1 if end_idx == total_zeros - 1 else zeros[end_idx + 1] - 1
                    
                    # Count ones in different regions
                    left_ones = left_zero - left_boundary  # ones available on left
                    right_ones = right_boundary - right_zero  # ones available on right
                    middle_ones = (right_zero - left_zero + 1) - num_zeros  # ones between first and last zero
                    
                    # We need: middle_ones + extra_left + extra_right >= num_zeros²
                    min_ones_needed = num_zeros * num_zeros
                    
                    if middle_ones >= min_ones_needed:
                        # All combinations of left and right extensions work
                        count += (left_ones + 1) * (right_ones + 1)
                    else:
                        # We need additional ones from left and/or right
                        needed = min_ones_needed - middle_ones
                        
                        # Count valid combinations where extra_left + extra_right >= needed
                        # Extra_left can be 0 to left_ones
                        # Extra_right can be 0 to right_ones
                        for take_left in range(left_ones + 1):
                            min_right = max(0, needed - take_left)
                            if min_right <= right_ones:
                                count += right_ones - min_right + 1
        
        return count
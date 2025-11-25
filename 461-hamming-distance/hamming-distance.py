class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bx = bin(x)[2:]
        by = bin(y)[2:]
        
        # Pad the shorter one with leading zeros
        max_len = max(len(bx), len(by))
        bx = bx.zfill(max_len)
        by = by.zfill(max_len)
        
        # Count differing bits
        count = 0
        for a, b in zip(bx, by):
            if a != b:
                count += 1
        return count

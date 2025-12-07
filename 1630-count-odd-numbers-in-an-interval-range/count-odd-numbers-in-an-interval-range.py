class Solution:
    def countOdds(self, low: int, high: int) -> int:
        res = (high - low) >> 1
        if (low & 1) or (high & 1):
            res += 1
        return res
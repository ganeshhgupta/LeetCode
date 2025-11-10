class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Keep only positive numbers
        res = [n for n in nums if n > 0]
        if not res:
            return 1
        
        res = list(set(res))  # remove duplicates
        res.sort()
        
        # Scan for the first missing positive
        expected = 1
        for num in res:
            if num == expected:
                expected += 1
            elif num > expected:
                return expected
        
        return expected

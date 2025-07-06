class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        
        max_val = num
        for d in set(s):
            candidate = int(s.replace(d, '9'))
            max_val = max(max_val, candidate)
        
        min_val = num
        for d in set(s):
            candidate = int(s.replace(d, '0'))
            min_val = min(min_val, candidate)
        
        return max_val - min_val
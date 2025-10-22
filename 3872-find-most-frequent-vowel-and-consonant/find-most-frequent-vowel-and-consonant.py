class Solution:
    def maxFreqSum(self, s: str) -> int:
        
        c = Counter(s)
        max_v = max_c = 0 
        for i in c:
            if i in ('aeiou'):
                max_v = max(max_v, c[i])
            else:
                max_c = max(max_c, c[i])

        return max_v + max_c
             
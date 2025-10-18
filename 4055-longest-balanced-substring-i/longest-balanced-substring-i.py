class Solution:
    def longestBalanced(self, s: str) -> int:

        # O(n^2), O(1)
        n = len(s)
        res = 0
        
        for i in range(n):
            freq = defaultdict(int)
            
            for j in range(i, n):
                freq[s[j]] += 1
                
                if len(set(freq.values())) == 1:
                    res = max(res, j - i + 1)
        
        return res
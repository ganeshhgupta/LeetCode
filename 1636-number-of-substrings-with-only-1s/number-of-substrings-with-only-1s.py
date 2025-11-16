class Solution:
    def numSub(self, s: str) -> int:

        # O(n), O(n)
        
        s = s.split('0')
        li = []
        for i in s:
            if i != '':
                li.append([i])
        
        res = 0
        for segment in li:
            length = len(segment[0])
            res += length * (length + 1) // 2
            res %= 10**9 + 7
            
        return res

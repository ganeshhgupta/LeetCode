class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        # same thing, make two [0] * 26, curr and target, keep sliding
        # O(n), O(1)

        if len(p) > len(s):
            return []
        
        target = [0] * 26
        for char in p:
            target[ord(char) - ord('a')] += 1
            
        res = []
        curr = [0] * 26
        
        for i in range(len(p)):
            curr[ord(s[i]) - ord('a')] += 1
            
        if target == curr:
            res.append(0)
            
        for i in range(len(p), len(s)):
            curr[ord(s[i]) - ord('a')] += 1
            curr[ord(s[i - len(p)]) - ord('a')] -= 1
            
            if target == curr:
                start_index = i - len(p) + 1
                res.append(start_index)
                
        return res
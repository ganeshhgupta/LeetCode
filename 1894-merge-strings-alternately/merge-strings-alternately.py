class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        # O(n), O(n)
        res = []
        for i in range(len(word1)):
            res.append(word1[i])
            if i < len(word2):
                res.append(word2[i]) 
        
        res.append(word2[i+1:])
        return "".join(res)
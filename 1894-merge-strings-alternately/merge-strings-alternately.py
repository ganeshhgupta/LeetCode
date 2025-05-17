class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        li = []
        l = min(len(word1), len(word2))
        i = 0
        while i < l:
            li.append(word1[i])
            li.append(word2[i])
            i += 1
        
        li.append(word1[i:])
        li.append(word2[i:])

        return ''.join(li)

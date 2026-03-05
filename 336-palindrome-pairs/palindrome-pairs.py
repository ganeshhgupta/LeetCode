class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        # O(N · K²), O(N · K)
        '''
        If A + B is palindrome, then:
        For some split of A: prefix is palindrome, reverse(suffix) exists in map
        OR
        For some split of A: suffix is palindrome, reverse(prefix) exists in map
        '''

        def isPal(s):
            return s == s[::-1]
        
        word_map = {w: i for i, w in enumerate(words)}
        res = []
        
        for i, w in enumerate(words):
            for cut in range(len(w) + 1):
                
                prefix = w[:cut]
                suffix = w[cut:]
                
                # Case 1: prefix is palindrome
                if isPal(prefix):
                    rev = suffix[::-1]
                    if rev in word_map and word_map[rev] != i:
                        res.append([word_map[rev], i])
                
                # Case 2: suffix is palindrome
                if cut != len(w) and isPal(suffix):
                    rev = prefix[::-1]
                    if rev in word_map and word_map[rev] != i:
                        res.append([i, word_map[rev]])
        
        return res  

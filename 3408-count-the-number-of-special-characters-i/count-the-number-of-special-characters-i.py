class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        
        res = set()

        for i in word:

            if ord(i) in range(65, 91) and chr(ord(i) + (97 - 65)) in word:
                res.add(i.lower())
        
        return len(res)
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        
        bl = list(brokenLetters)
        print(bl)
        t = list(text.split(" "))
        c = 0
        for i in t:
            for j in bl:
                print(i, j)
                if j in i:
                    c += 1
                    break
        
        return len(t) - c
                    
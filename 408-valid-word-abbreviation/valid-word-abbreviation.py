class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0  # pointer for word
        j = 0  # pointer for abbr

        def toNum(j):
            num = 0
            while j < len(abbr) and abbr[j].isdigit():
                num = num * 10 + int(abbr[j])
                j += 1
            return num, j
        
        while i < len(word) and j < len(abbr):

            if word[i] == abbr[j]:
                i += 1
                j += 1

            elif abbr[j].isdigit():
                if abbr[j] == '0':
                    return False
                
                num, j = toNum(j)
                
                i += num
            else:
                return False
        
        return i == len(word) and j == len(abbr)
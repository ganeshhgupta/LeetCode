from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)        
        count = sorted(count.items(), key=lambda x: -x[1])
        
        if count[0][1] > (len(s) + 1) // 2:
            return ""
        
        res = []
        while count:
            char, freq = count.pop(0)
            res.append(char)
            
            if freq > 1:
                count.append((char, freq - 1))
            
            if not count:
                break
            
            char2, freq2 = count.pop(0)
            res.append(char2)
            
            if freq2 > 1:
                count.append((char2, freq2 - 1))
            
            count = sorted(count, key=lambda x: -x[1])

        return "".join(res)

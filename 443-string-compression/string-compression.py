class Solution:
    def compress(self, chars: List[str]) -> int:
        
        chars += " " #hack, huehue
        c = 0
        p = 0
        for i in range(len(chars) -1):
            c += 1

            if chars[i] != chars[i + 1]:
                if c == 1:
                    chars[p] = chars[i]
                    p += 1
                    c = 0
                else:
                    chars[p] = chars[i]
                    p += 1
                    c = str(c)
                    for j in c:
                        chars[p] = j
                        p += 1
                    c = 0
        return p
class Solution:
    def kthCharacter(self, k: int) -> str:
        char = 'a'
        
        def op(s):
            while len(s) < k:
                temp = []
                for c in s:
                    if c == 'z':
                        temp.append('a')
                    else:
                        temp.append(chr(ord(c) + 1))
                s = s + ''.join(temp)
            return s[k - 1]
        
        return op(char)

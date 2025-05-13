class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        if t == 0:
            return len(s)
        
        freq = Counter(s)
        
        for i in range(t):
            f = {}
            for c in freq:
                if c == 'z':
                    if 'a' in f:
                        f['a'] += freq[c]
                    else:
                        f['a'] = freq[c]
                    if 'b' in f:
                        f['b'] += freq[c]
                    else:
                        f['b'] = freq[c]
                else:
                    next_char = chr(ord(c) + 1)
                    if next_char in f:
                        f[next_char] += freq[c]
                    else:
                        f[next_char] = freq[c]
            freq = f
        return sum(freq.values()) % (10**9 + 7)
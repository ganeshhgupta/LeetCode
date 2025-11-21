class Solution: 
    def countPalindromicSubsequence(self, s: str) -> int:

        idx = defaultdict(list)
        res = set()

        for i, ch in enumerate(s):
            idx[ch].append(i)
        
        for ch, v in idx.items():
            if len(v) >= 2:
                left = v[0]
                right = v[-1]

                # middle must be strictly between first and last
                for i in range(left + 1, right):
                    res.add(ch + s[i] + ch)

        return len(res)

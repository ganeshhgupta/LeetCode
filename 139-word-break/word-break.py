class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n = len(s)
        dp_cahce = [False] * (n + 1)
        dp_cahce[n] = True

        for i in range(n - 1, -1, -1):
            for w in wordDict:
                w_length = len(w)
                if i + w_length <= n and s[i:i+w_length] == w:
                    dp_cahce[i] = dp_cahce[i + w_length]
                if dp_cahce[i]:
                    break

        return dp_cahce[0]
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # O(n × W × L), O(n)

        # dp[i] = can s[i:] be broken into words?
        # start from the end because dp[i] depends on dp[i + word_length]
        # if a word matches at i, check whether the remaining suffix is breakable
        # dp[n] = True because an empty suffix is successfully broken

        n = len(s)
        dp = [False] * (n + 1)
        dp[-1] = True
    
        for i in range(n - 1, -1, -1):

            for w in wordDict:

                w_len = len(w)

                if i + w_len <= n  and s[i:i+w_len] == w:
                    dp[i] = dp[i + w_len]
                
                if dp[i]:
                    break
        
        return dp[0]

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # O(m.n), O(m.n)
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True
        
        for j in range(1, len(p) + 1):
            if p[j-1] == "*":
                dp[0][j] = dp[0][j-2]

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                
                if p[j-1] == "." or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                    
                elif p[j-1] == "*":
                    dp[i][j] = dp[i][j-2] # zero occurence of p[i-1]

                    if p[j-2] == "." or p[j-2] == s[i-1]: 
                        # if '.*' come together, they accomodate any/all characters
                        # character preceding '*' matches the current text character s[i-1]

                        dp[i][j] = dp[i][j] or dp[i-1][j]
                        
        return dp[len(s)][len(p)]
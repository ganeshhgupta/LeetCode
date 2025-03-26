class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n = len(s)
        dp_cahce = [False] * (n + 1)
        #create a dp cache for the entire length of s = [False, False, False .... n times]
        dp_cahce[n] = True
        #set last index to be True, we assume the end of string s is a break

        for i in range(n - 1, -1, -1):
            for w in wordDict:
                w_length = len(w)
                #for eg. s = "leetcode", the code will only enter this condition at i=4 'code' and i=0 'leet'
                if i + w_length <= n and s[i:i+w_length] == w:
                    dp_cahce[i] = dp_cahce[i + w_length]
                if dp_cahce[i]:
                    #as soon as we find a word match, no need to check rest of the dict
                    break
        #if we can successfully break s, dp[0] has to be True
        return dp_cahce[0]
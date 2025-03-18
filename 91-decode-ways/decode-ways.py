class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp = { len(s) : 1}   #memoization set that will contain no. of possible combinations at ith index
                              #hence at last index (None) only one possible combination hence, len(s) = 3 for "121" -> 1


        def checkValidCharacter(i):

            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                return dfs(i + 2)  # Compute number of ways starting at i+2
            return 0  # If the two-character substring isn't valid, return 0

        def dfs(i):

            if i in dp:
                return dp[i] #base case (will start working from the end of the list back towards the front and return cahced result)
            if s[i] == "0":
                return 0  # "0" cannot be decoded

            res = dfs(i + 1) + checkValidCharacter(i)  # Check if a two-character decoding is valid
            #essentially dp[i] = dp[i+1] + dp[i+2]
            
            dp[i] = res  # Store result in memoization dictionary
            return res

        return dfs(0)
